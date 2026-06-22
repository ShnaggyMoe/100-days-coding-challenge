import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, twilio_message):
        message = self.client.messages.create(
            to="+14084138270",
            from_="+17372583742",
            body=twilio_message)