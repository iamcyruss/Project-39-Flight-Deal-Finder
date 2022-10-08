import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def sheety_get(SHEETY_BEARER_TOKEN):
        SHEETY_ENDPOINT = "https://api.sheety.co/34bae8c41413bf248912bfb89813a84e/flightDeals/prices"
        SHEETY_HEADERS = {
            "Content-Type": "application/json",
            "Authorization": SHEETY_BEARER_TOKEN
        }
        sheety_response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        sheety_response.raise_for_status()
        sheety_json = sheety_response.json()
        return sheety_json


#data = DataManager.sheety_get()
#print(DataManager.sheety_get()['prices'])
