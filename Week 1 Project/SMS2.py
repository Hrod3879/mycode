# added two JSON files to the project
# one for security, while presenting hide my config from others
# second import a quote bank for messages to be sent

import json
import random
from twilio.rest import Client

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    

# Extract values from the loaded configuration
account_sid = config["account_sid"]
auth_token = config["auth_token"]
twilio_phone_number = config["twilio_phone_number"]
recipient_phone_number = "12672358528"

# Load quotes from JSON file
with open("Quote_Bank.json", "r") as file:
    data = json.load(file)
    sms_messages = data.get("sms_messages", [])

# Choose a random quote from the list of quotes
random_quote = random.choice(sms_messages)
message_body = random_quote["text"]

# Create a Twilio client
client = Client(account_sid, auth_token)

try:
    # Send the SMS message
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"Message sent with SID: {message.sid}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

