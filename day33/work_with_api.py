import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
location_tuple = (response.json()["iss_position"]["latitude"], response.json()["iss_position"]["longitude"])
print(location_tuple)
