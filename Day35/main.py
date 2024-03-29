import requests
import datetime
from twilio.rest import Client

account_sid = ''
auth_token = ''
OWM_Endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
api_Key = ''

weather_params = {
    "lat": -23.550520,
    "lon": -46.633308,
    "appid": api_Key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring an umbrella.",
        from_='whatsapp:+14155238886',
        to='whatsapp:+15005550006'
    )