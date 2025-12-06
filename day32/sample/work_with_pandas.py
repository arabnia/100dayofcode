#!/usr/bin/env python3
import sys
import json
import pandas as pd
import re

# ------------------------------------------------------
# Configurable filters
# ------------------------------------------------------
INCLUDE_PATTERN = None      # r"frontend"
EXCLUDE_PATTERN = None      # r"test|debug"


def include_deployment(name):
    if INCLUDE_PATTERN and not re.search(INCLUDE_PATTERN, name):
        return False
    if EXCLUDE_PATTERN and re.search(EXCLUDE_PATTERN, name):
        return False
    return True


# ------------------------------------------------------
# Helpers: Convert CPU/Memory to normalized units
# ------------------------------------------------------
def cpu_to_m(cpu):
    if not cpu:
        return 0
    cpu = str(cpu).lower()
    if cpu.endswith("m"):
        return int(cpu[:-1])
    return float(cpu) * 1000


def mem_to_mi(mem):
    if not mem:
        return 0
    mem = str(mem).lower()
    units = {
        "ki": 1 / 1024,
        "mi": 1,
        "gi": 1024,
        "ti": 1048576,
        "m": 1 / 1048576,
        "g": 1024
    }
    for u, v in units.items():
        if mem.endswith(u):
            return float(mem.replace(u, "")) * v
    return float(mem) / (1024 * 1024)  # bytes → Mi


# ------------------------------------------------------
# Read input JSON
# ------------------------------------------------------
data = json.load(sys.stdin)
rows = []

# ------------------------------------------------------
# Parse each deployment
# ------------------------------------------------------
for item in data.get("items", []):
    ns = item["metadata"]["namespace"]
    dep = item["metadata"]["name"]

    if not include_deployment(dep):
        continue

    replicas = item["spec"].get("replicas", 1)

    cpu_req = cpu_lim = mem_req = mem_lim = 0

    for c in item["spec"]["template"]["spec"].get("containers", []):
        res = c.get("resources", {})
        r = res.get("requests", {})
        l = res.get("limits", {})

        cpu_req += cpu_to_m(r.get("cpu"))
        cpu_lim += cpu_to_m(l.get("cpu"))
        mem_req += mem_to_mi(r.get("memory"))
        mem_lim += mem_to_mi(l.get("memory"))

    # Multiply values by replica count
    rows.append({
        "namespace": ns,
        "deployment": dep,
        "replicas": replicas,
        "cpu_request_m": cpu_req,
        "cpu_limit_m": cpu_lim,
        "mem_request_mi": mem_req,
        "mem_limit_mi": mem_lim,
        "total_cpu_request_m": cpu_req * replicas,
        "total_cpu_limit_m": cpu_lim * replicas,
        "total_mem_request_mi": mem_req * replicas,
        "total_mem_limit_mi": mem_lim * replicas,
    })


# ------------------------------------------------------
# Build Pandas DataFrame
# ------------------------------------------------------
df = pd.DataFrame(rows)

# ------------------------------------------------------
# Namespace totals
# ------------------------------------------------------
ns_totals = (
    df.groupby("namespace")[[
        "total_cpu_request_m", "total_cpu_limit_m",
        "total_mem_request_mi", "total_mem_limit_mi"
    ]]
    .sum()
    .reset_index()
)
ns_totals["deployment"] = "NAMESPACE_TOTAL"
ns_totals["replicas"] = ""

# ------------------------------------------------------
# Global totals
# ------------------------------------------------------
global_data = df[[
    "total_cpu_request_m", "total_cpu_limit_m",
    "total_mem_request_mi", "total_mem_limit_mi"
]].sum()

global_df = pd.DataFrame([{
    "namespace": "ALL",
    "deployment": "GLOBAL_TOTAL",
    "replicas": "",
    "total_cpu_request_m": global_data["total_cpu_request_m"],
    "total_cpu_limit_m": global_data["total_cpu_limit_m"],
    "total_mem_request_mi": global_data["total_mem_request_mi"],
    "total_mem_limit_mi": global_data["total_mem_limit_mi"]
}])

# ------------------------------------------------------
# Final combined data
# ------------------------------------------------------
final_df = pd.concat([df, ns_totals, global_df], ignore_index=True)
final_df = final_df.sort_values(["namespace", "deployment"])

# ------------------------------------------------------
# Output CSV
# ------------------------------------------------------
final_df.to_csv(sys.stdout, index=False)
