import os
from twilio.rest import Client
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, sms_list):

        SMS_ACCOUNT_SID = os.environ.get("SMS_ACCOUNT_SID")
        SMS_AUTH_TOKEN = os.environ.get("SMS_AUTH_TOKEN")
        FROM_ = +19474652240
        client = Client(SMS_ACCOUNT_SID, SMS_AUTH_TOKEN)
        message = client.messages.create(body=sms_list, from_=FROM_, to='+14253810699')
        print(message.sid)


    def send_emails(self, sms_list, SMTPTOKEN, EMAILS):
        my_gmail = "russnicosia.auto@gmail.com"
        for email in EMAILS:
            with smtplib.SMTP("smtp.gmail.com", 587) as gmail_connection:
                gmail_connection.starttls()
                gmail_connection.login(user=my_gmail, password=SMTPTOKEN)
                gmail_connection.sendmail(
                    from_addr=my_gmail,
                    to_addrs=email,
                    msg=f"Subject: !!!!!! Flight Deal FOUND !!!!!!\n\n"
                        f"{sms_list}\n\n- Automated Russ"
                )

