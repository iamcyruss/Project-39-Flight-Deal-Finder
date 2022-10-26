from notification_manager import NotificationManager
import os

class FlightData:
    #This class is responsible for structuring the flight data.

    def flight_data_formatter(self, i, flight_data_json, SMTPTOKEN, USERS):

        print(f"Fly To Raw Data: {flight_data_json['data']}")
        EMAILS = []
        for u in USERS:
            EMAILS.append(u['email'])
        for count, price_to in enumerate(flight_data_json['data']):
            departure_date = price_to['route'][0]['utc_departure'].split('T')
            departure_time = departure_date[1].split('.')
            #print(f"Departure dates: {departure_date[0]} {departure_time[0]}")
            arrival_date = price_to['route'][0]['utc_arrival'].split('T')
            arrival_time = arrival_date[1].split('.')
            #print(f"Arrival dates: {arrival_date[0]} {arrival_time[0]}")
            if len(price_to['route']) == 1 and count == 0:
                """print(
                    f"Price To: ${price_to['price']} Low Price: ${i['lowestPrice']}\n"
                    f"Bag Prices To: {price_to['bags_price']}\n"
                    f"From: {price_to['route'][0]['cityFrom']} To: {price_to['route'][0]['cityTo']}\n"
                    f"Depart: {price_to['route'][0]['utc_departure']}\nArrive: {price_to['route'][0]['utc_arrival']}\n"
                    f"-------------------------------------------------------------------")"""
                if int(price_to['price']) < int(i['lowestPrice']):
                    sms_list = f"-\nFrom: {price_to['route'][0]['cityFrom']}\n" \
                               f"To: {price_to['route'][0]['cityTo']}\n" \
                               f"Price: ${price_to['price']}\n" \
                               f"Depart: {departure_date[0]} {departure_time[0]}\n" \
                               f"Arrive: {arrival_date[0]} {arrival_time[0]}\n" \
                               f"-------------------------------\n"
                    print(f"sms_list: {sms_list}")
                    #NotificationManager.send_sms(self, sms_list)
            elif len(price_to['route']) > 1:
                #print(f"Price To: ${price_to['price']} Low Price: ${i['lowestPrice']}\n"
                      #f"Bag Prices To: ${price_to['bags_price']}")
                sms_list = ''
                depart_counter = 0
                return_counter = 0
                for route_count, route in enumerate(price_to['route']):
                    #print(f"Stop {route_count + 1}: From: {route['cityFrom']} To: {route['cityTo']}\n"
                          #f"Depart: {route['utc_departure']}\nArrive: {route['utc_arrival']}\n"
                          #f"-------------------------------------------------------------------")
                    departure_date = price_to['route'][route_count]['utc_departure'].split('T')
                    departure_time = departure_date[1].split('.')
                    # print(f"Departure dates: {departure_date[0]} {departure_time[0]}")
                    arrival_date = price_to['route'][route_count]['utc_arrival'].split('T')
                    arrival_time = arrival_date[1].split('.')
                    # print(f"Arrival dates: {arrival_date[0]} {arrival_time[0]}")
                    if int(price_to['price']) < int(i['lowestPrice']):
                        if price_to['route'][route_count]['return'] == 0:
                            depart_counter += 1
                            sms_list = f"{sms_list}\nDeparting Flight #{depart_counter}:\n" \
                                       f"From: {price_to['route'][route_count]['cityFrom']}\n" \
                                       f"To: {price_to['route'][route_count]['cityTo']}\n" \
                                       f"Price: ${price_to['price']}\n" \
                                       f"Depart: {departure_date[0]} {departure_time[0]}\n" \
                                       f"Arrive: {arrival_date[0]} {arrival_time[0]}\n" \
                                       f"-------------------------------\n"
                        else:
                            return_counter += 1
                            sms_list = f"{sms_list}\nReturning Flight #{return_counter}:\n" \
                                       f"From: {price_to['route'][route_count]['cityFrom']}\n" \
                                       f"To: {price_to['route'][route_count]['cityTo']}\n" \
                                       f"Price: ${price_to['price']}\n" \
                                       f"Depart: {departure_date[0]} {departure_time[0]}\n" \
                                       f"Arrive: {arrival_date[0]} {arrival_time[0]}\n" \
                                       f"-------------------------------\n"
                    else:
                        pass
                if len(sms_list) > 0:
                    print(f"Round Trip Flights: {sms_list}")
                    NotificationManager.send_emails(self, sms_list, SMTPTOKEN, EMAILS)
                else:
                    pass
                # NotificationManager.send_sms(self, sms_list=f"Departing Flights: {sms_list}")
                """if len(sms_list) > 0 and flight_data_json['data'][0]['flyFrom'] == 'DEN':
                    print(f"Departing Flights: {sms_list}")
                    #print(len(sms_list))
                    #NotificationManager.send_sms(self, sms_list=f"Departing Flights: {sms_list}")
                elif len(sms_list) > 0 and flight_data_json['data'][0]['flyTo'] == 'DEN':
                    print(f"Returning Flights: {sms_list}")
                    #print(len(sms_list))
                    #NotificationManager.send_sms(self, sms_list=f"Returning Flights: {sms_list}")
                else:
                    pass"""
            else:
                pass