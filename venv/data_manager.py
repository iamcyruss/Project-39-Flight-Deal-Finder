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


    def users_sheety_add(self, SHEETY_BEARER_TOKEN, user):
        SHEETY_ENDPOINT_USERS = "https://api.sheety.co/34bae8c41413bf248912bfb89813a84e/flightDeals/users"
        SHEETY_HEADERS = {
            "Content-Type": "application/json",
            "Authorization": SHEETY_BEARER_TOKEN
        }
        new_user_data = {
            'user': {
                "firstName": user['firstname'],
                "lastName": user['lastname'],
                "email": user['email']
            }
        }
        new_user_post = requests.post(url=SHEETY_ENDPOINT_USERS, headers=SHEETY_HEADERS, json=new_user_data)
        new_user_response = new_user_post.json()
        new_user_post.raise_for_status()
        print(new_user_response)


    def get_user_datails(self, SHEETY_BEARER_TOKEN):
        SHEETY_ENDPOINT_USERS = "https://api.sheety.co/34bae8c41413bf248912bfb89813a84e/flightDeals/users"
        SHEETY_HEADERS = {
            "Content-Type": "application/json",
            "Authorization": SHEETY_BEARER_TOKEN
        }
        get_user_details = requests.get(url=SHEETY_ENDPOINT_USERS, headers=SHEETY_HEADERS)
        get_user_details.raise_for_status()
        get_user_details_json = get_user_details.json()
        print(get_user_details_json)


#data = DataManager.sheety_get()
#print(DataManager.sheety_get()['prices'])
