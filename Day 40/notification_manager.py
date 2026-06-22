import os
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_email(self, receiver_email, message_body):
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        SENDER_EMAIL = os.environ.get("EMAIL")
        SENDER_PASSWORD = os.environ.get("EMAIL_PASSWORD")
        RECEIVER_EMAIL = receiver_email

        msg = EmailMessage()
        msg["Subject"] = "Cheap Flight Alert"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg.set_content(message_body)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(SENDER_EMAIL, SENDER_PASSWORD)
            connection.send_message(msg)