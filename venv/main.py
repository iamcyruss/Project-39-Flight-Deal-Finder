#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from flight_search import FlightSearch


FS = FlightSearch()
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
FS.grab_flight_data(KIWI_API_KEY)
