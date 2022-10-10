import os
import requests
from datetime import date, timedelta
from data_manager import DataManager


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
    KIWI_FLYTO_PAYLOAD = {
        "fly_from": 'DEN',
        "fly_to": i['iataCode'],
        "date_from": NINETY_FROM_TODAY,
        "date_to": ONETWENTY_FROM_TODAY,
        "curr": "USD",
        "locale": "en",
        "limit": 5
    }
    KIWI_FLYBACK_PAYLOAD = {
        "fly_from": i['iataCode'],
        "fly_to": "DEN",
        "date_from": NINETY_FROM_TODAY,
        "date_to": ONETWENTY_FROM_TODAY,
        "curr": "USD",
        "locale": "en",
        "limit": 5
    }
    KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search/"
    kiki_flyto_response = requests.get(url=KIWI_ENDPOINT, headers=KIWI_HEADERS, params=KIWI_FLYTO_PAYLOAD)
    kiki_flyto_response.raise_for_status()
    kiwi_flyto_json = kiki_flyto_response.json()
    kiwi_flyback_response = requests.get(url=KIWI_ENDPOINT, headers=KIWI_HEADERS, params=KIWI_FLYBACK_PAYLOAD)
    kiwi_flyback_response.raise_for_status()
    kiwi_flyback_json = kiwi_flyback_response.json()
    print(f"Fly To Raw Data: {kiwi_flyto_json['data']}")
    print(f"Fly Back Raw Data:{kiwi_flyback_json['data']}")
    for count, price_to in enumerate(kiwi_flyto_json['data']):
        if len(price_to['route']) == 1 and count == 0:
            print(f"Price To: ${price_to['price']} \nBag Prices To: {price_to['bags_price']}\n"
                  f"From: {price_to['route'][0]['cityFrom']} To: {price_to['route'][0]['cityTo']}\n"
                  f"Depart: {price_to['route'][0]['utc_departure']}\nArrive: {price_to['route'][0]['utc_arrival']}\n"
                  f"-------------------------------------------------------------------")
        elif len(price_to['route']) > 1:
            print(f"Price To: ${price_to['price']}\nBag Prices To: ${price_to['bags_price']}")
            for route_count, route in enumerate(price_to['route']):
                print(f"Stop {route_count + 1}: From: {route['cityFrom']} To: {route['cityTo']}\n"
                      f"Depart: {route['utc_departure']}\nArrive: {route['utc_arrival']}\n"
                      f"-------------------------------------------------------------------")
        else:
            pass
    for count, price_back in enumerate(kiwi_flyback_json['data']):
        if len(price_back['route']) == 1 and count == 0:
            print(f"Price Back: ${price_back['price']} \nBag Prices Back: {price_back['bags_price']}\n"
                  f"From: {price_back['route'][0]['cityFrom']} To: {price_back['route'][0]['cityTo']}\n"
                  f"Depart: {price_back['route'][0]['utc_departure']}\nArrive: {price_back['route'][0]['utc_arrival']}\n"
                  f"-------------------------------------------------------------------")
        elif len(price_back['route']) > 1:
            print(f"Price Back: ${price_back['price']}\nBag Prices Back: ${price_back['bags_price']}")
            for route_count, route in enumerate(price_back['route']):
                print(f"Stop {route_count + 1}: From: {route['cityFrom']} To: {route['cityTo']}\n"
                      f"Depart: {route['utc_departure']}\nArrive: {route['utc_arrival']}\n"
                      f"-------------------------------------------------------------------")
        else:
            pass


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass