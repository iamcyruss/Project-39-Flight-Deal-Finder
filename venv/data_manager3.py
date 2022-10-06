import os
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/34bae8c41413bf248912bfb89813a84e/flightDeals/prices"
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
print(SHEETY_BEARER_TOKEN)
SHEETY_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_BEARER_TOKEN
}
print(SHEETY_HEADERS)

sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
print(sheety_response)


