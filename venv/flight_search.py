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
    for count, price in enumerate(kiwi_json['data']):
        if len(price['route']) == 1 and count == 0:
            print(f"Price: ${price['price']}\nBag Prices: {price['bags_price']}\n"
                  f"From: {price['route'][0]['cityFrom']} To: {price['route'][0]['cityTo']}\n"
                  f"Depart: {price['route'][0]['utc_departure']}\nArrive: {price['route'][0]['utc_arrival']}\n"
                  f"-------------------------------------------------------------------")
        elif len(price['route']) > 1:
            print(f"Price: ${price['price']}\nBag Prices: ${price['bags_price']}")
            for route_count, route in enumerate(price['route']):
                print(f"Stop {route_count + 1}: From: {route['cityFrom']} To: {route['cityTo']}\n"
                      f"Depart: {route['utc_departure']}\nArrive: {route['utc_arrival']}\n"
                      f"-------------------------------------------------------------------")
        else:
            pass


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass