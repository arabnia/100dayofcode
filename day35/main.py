from dotenv import load_dotenv
import os
from datetime import datetime, timezone
import requests
# My location data
LATITUDE = 33.540250
LONGITUDE = 54.337667
load_dotenv()

current_time = datetime.now(timezone.utc).timestamp()
payload = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": os.getenv("API_TOKEN"),
    "units": "metric"
}
def weather_status():
    data = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=payload)
    data.raise_for_status()
    return  data.json()["list"]

if_rain = False
for item in weather_status():
    if item["dt"] <= current_time + 86400:
        # print(f"{item["dt"]} and {current_time + 86400}")
        # print(item["weather"][0]["id"])
        if item["weather"][0]["id"] < 700:
            if_rain = True
print(if_rain)