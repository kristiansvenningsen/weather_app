import requests
import os
from twilio.rest import Client


MY_LAT = 48.224440 # Your latitude
MY_LONG = 16.392054 # Your longitude
COUNT = 4


api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": COUNT,
}

url = "https://pro.openweathermap.org/data/2.5/forecast"
response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()


print(data)

rain_list =  [item["weather"][0]["id"] for item in data["list"]]
print(rain_list)

if any(x < 800 for x in rain_list):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's gonna rain today 🌧️ Remember to bring an umbrella!",
        from_="+19069702708",
        to= ‭"+436645333346"‬ #os.environ.get("YOUR_TWILIO_VERIFIED_REAL_NUMBER"),
    )
    print("It's gonna rain 🌧️")
    print(message.status)
else:
    print("No rain today")




