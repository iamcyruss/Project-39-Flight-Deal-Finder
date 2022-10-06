import os
import requests
from datetime import date, timedelta
from data_manager import DataManager


SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
DATA = DataManager.sheety_get(SHEETY_BEARER_TOKEN)['prices']
print(DATA[0]['city'])
TODAY = date.today().strftime('%m/%d/%Y')
NINETY_FROM_TODAY = (date.today() + timedelta(days=90)).strftime('%m/%d/%Y')
ONETWENTY_FROM_TODAY = (date.today() + timedelta(days=120)).strftime('%m/%d/%Y')
print(f"Todays date: {TODAY}\n90 days from now: {NINETY_FROM_TODAY}\n120 days from now: {ONETWENTY_FROM_TODAY}")

for i in DATA:
    KIWI_PAYLOAD = {
        "fly_from": 'Denver',
        "fly_to": i['city'],
        "dateFrom": NINETY_FROM_TODAY,
        "dateTo": ONETWENTY_FROM_TODAY
    }
    print(KIWI_PAYLOAD)
    KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass