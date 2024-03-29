import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = ""
MY_PASSWORD = ""
MY_LAT = -23.550520
MY_LONG = -46.633308
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data_iss_position = response.json()["iss_position"]

    latitude = float(data_iss_position["latitude"])
    longitude = float(data_iss_position["longitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= MY_LONG <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="",
                msg=f"Subject:LOOK UP SKY\n\n The ISS is above you in the sky."
            )