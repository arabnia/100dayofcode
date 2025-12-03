import datetime

import requests
# my location
LATITUDE = 35.758736
LONGITUDE = 51.396499

payload = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=payload)
response.raise_for_status()
print(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
print(response.json()["results"]["sunset"].split("T")[1].split(":")[0])
print(datetime.datetime.now().hour) 