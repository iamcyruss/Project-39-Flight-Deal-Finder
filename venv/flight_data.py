from notification_manager import NotificationManager
import os

class FlightData:
    #This class is responsible for structuring the flight data.

    def flight_data_formatter(self, i, flight_data_json):

        print(f"Fly To Raw Data: {flight_data_json['data']}")
        print(f"Fly Back Raw Data:{flight_data_json['data']}")
        for count, price_to in enumerate(flight_data_json['data']):
            if len(price_to['route']) == 1 and count == 0:
                print(
                    f"Price To: ${price_to['price']} Low Price: ${i['lowestPrice']}\nBag Prices To: {price_to['bags_price']}\n"
                    f"From: {price_to['route'][0]['cityFrom']} To: {price_to['route'][0]['cityTo']}\n"
                    f"Depart: {price_to['route'][0]['utc_departure']}\nArrive: {price_to['route'][0]['utc_arrival']}\n"
                    f"-------------------------------------------------------------------")
                if int(price_to['price']) < int(i['lowestPrice']):
                    sms_list = f"-\nFrom: {price_to['route'][0]['cityFrom']}\n" \
                               f"To: {price_to['route'][0]['cityTo']}\n" \
                               f"Price: ${price_to['price']}\n" \
                               f"Depart: {price_to['route'][0]['utc_departure']}\n" \
                               f"Arrive: {price_to['route'][0]['utc_arrival']}\n" \
                               f"-------------------------------\n"
                    NotificationManager.send_sms(self, sms_list)
            elif len(price_to['route']) > 1:
                print(
                    f"Price To: ${price_to['price']} Low Price: ${i['lowestPrice']}\nBag Prices To: ${price_to['bags_price']}")
                sms_list = []
                for route_count, route in enumerate(price_to['route']):
                    print(f"Stop {route_count + 1}: From: {route['cityFrom']} To: {route['cityTo']}\n"
                          f"Depart: {route['utc_departure']}\nArrive: {route['utc_arrival']}\n"
                          f"-------------------------------------------------------------------")
                    if int(price_to['price']) < int(i['lowestPrice']):
                        sms_list.append(f"-\nFrom: {price_to['route'][0]['cityFrom']}\n"
                                        f"To: {price_to['route'][0]['cityTo']}\n"
                                        f"Price: ${price_to['price']}\n"
                                        f"Depart: {price_to['route'][0]['utc_departure']}\n"
                                        f"Arrive: {price_to['route'][0]['utc_arrival']}\n"
                                        f"-------------------------------\n")
                    if len(sms_list) > 1:
                        NotificationManager.send_sms(self, sms_list)
                    else:
                        pass
            else:
                pass