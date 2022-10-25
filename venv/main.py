#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from flight_search import FlightSearch
from data_manager import DataManager


SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
SMTPTOKEN = os.environ.get("SMTPTOKEN")
DM = DataManager()
running = True
while running:
    todo = input("\nPress b to search users.\n"
                 "Press a to add new user.\n"
                 "Press c to delete a user.\n"
                 "Press d to edit a user.\n"
                 "Press z to quit.\n")
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
    elif todo.lower() == 'c':
        DM.get_user_datails(SHEETY_BEARER_TOKEN)
        user_id = input("What user ID would you like to delete? \n")
        DM.delete_user_details(SHEETY_BEARER_TOKEN, user_id)
    elif todo.lower() == 'd':
        DM.get_user_datails(SHEETY_BEARER_TOKEN)
        user_id = input("What user ID would you like to edit? \n")
        firstname = input("What should the First Name be? ")
        lastname = input("What should the Last Name be? ")
        email = input("What should be the correct Email? ")
        user_details = {
            'user': {
                'firstName': firstname,
                'lastName': lastname,
                'email': email
            }
        }
        DM.edit_user_details(SHEETY_BEARER_TOKEN, user_id, user_details)
    elif todo.lower() == 'z':
        running = False
    else:
        begin_window = input("What date do you want to head out by?\n")
        end_window = input("What date do you want to be back by?\n")
        FS = FlightSearch()
        KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
        FS.grab_flight_data(KIWI_API_KEY, begin_window, end_window, SMTPTOKEN)
