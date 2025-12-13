import requests
import json
import os
import datetime

# Get exercise data
exersise_data = {"text":"Ran and walked"}
exersise_headers = {"content-type": "application/json"}
exersise_response = requests.post(url=os.environ["EXERCISE_SERVER"], json=exersise_data, headers=exersise_headers)
workout_row = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "exercise": exersise_response.json()["exercises"][0]["name"],
            "duration": exersise_response.json()["exercises"][0]["duration_min"],
            "calories": exersise_response.json()["exercises"][0]["nf_calories"]
    }
}


sheety_headers = {
    "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}",
    "Content-Type": "application/json"
}

sheety_addrow = requests.post(
    url=os.environ["SHEETY_ENDPOINT"],
    headers=sheety_headers,
    json=workout_row
    )

print(sheety_addrow.text)
print(sheety_addrow.status_code)

#
# sheety_getrow = requests.get(url=os.environ["SHEETY_ENDPOINT"], headers=sheety_headers)
# print(sheety_getrow.text)
