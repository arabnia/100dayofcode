import requests
from datetime import datetime
import math
import smtplib

MY_LAT = 35.624948 # Your latitude
MY_LONG = 51.429346 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Tehran",
}
def check_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if ((time_now.hour <= sunrise or time_now.hour <= 24) and (time_now.hour >= sunset)):
        return True
    else:
        return False

def check_status():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if check_night():
        if (math.isclose(iss_latitude, MY_LAT, abs_tol=5) and math.isclose(iss_longitude, MY_LONG, abs_tol=5)):
            return True
        else:
            return False

#Your position is within +5 or -5 degrees of the ISS position.

def send_email(text):
    with smtplib.SMTP("192.168.100.150") as connection:
        connection.sendmail(from_addr="hossein@raspberrypi", to_addrs="hossien.arabnia@gmail.com",
                            msg=f"python code status:{text}\n")

print(check_status())


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



