#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from flight_search import FlightSearch
from data_manager import DataManager


SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
DM = DataManager()
todo = input("Press a to search users.\nPress b to add new user.\n")
if todo.lower() == 'a':
    firstname = input("What's your first name? ")
    lastname = input("What's your last name? ")
    email = input("What's your email address? ")
    user = {
        'firstname': firstname,
        'lastname': lastname,
        'email': email
    }

    DM.users_sheety_add(SHEETY_BEARER_TOKEN, user)
elif todo.lower() == 'b':
    DM.get_user_datails(SHEETY_BEARER_TOKEN)
else:
    FS = FlightSearch()
    KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
    FS.grab_flight_data(KIWI_API_KEY)
