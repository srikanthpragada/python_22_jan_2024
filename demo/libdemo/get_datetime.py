
import requests

resp = requests.get("https://worldtimeapi.org/api/timezone/asia/kolkata")

details = resp.json()  # convert JSON to Dict

print(details['datetime'])
print(details['utc_datetime'])

