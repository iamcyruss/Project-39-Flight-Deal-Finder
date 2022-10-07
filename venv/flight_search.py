import os
import requests
from datetime import date, timedelta
from data_manager import DataManager
from requests_toolbelt.utils import dump


SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
DATA = DataManager.sheety_get(SHEETY_BEARER_TOKEN)['prices']
TODAY = date.today().strftime('%d/%m/%Y')
NINETY_FROM_TODAY = (date.today() + timedelta(days=90)).strftime('%d/%m/%Y')
ONETWENTY_FROM_TODAY = (date.today() + timedelta(days=120)).strftime('%d/%m/%Y')
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "apikey": KIWI_API_KEY
}

for i in DATA:
    KIWI_PAYLOAD = {
        "fly_from": 'DEN',
        "fly_to": i['iataCode'],
        "date_from": NINETY_FROM_TODAY,
        "date_to": ONETWENTY_FROM_TODAY,
        "curr": "USD",
        "limit": 5
    }
    KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search/"
    kiwi_response = requests.get(url=KIWI_ENDPOINT, headers=KIWI_HEADERS, params=KIWI_PAYLOAD)
    #kiwi_response.raise_for_status()
    kiwi_json = kiwi_response.json()
    print(kiwi_json['data'])
    for price in kiwi_json['data']:
        print(price['price'])


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass