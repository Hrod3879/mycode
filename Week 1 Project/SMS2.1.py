import json
import random
import re
from twilio.rest import Client

def send_random_sms_message():
    # Load configuration from config.json
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    # Extract values from the loaded configuration
    account_sid = config["account_sid"]
    auth_token = config["auth_token"]
    twilio_phone_number = config["twilio_phone_number"]   
     
    # Get user input for recipient's phone number
    recipient_phone_number = input("Enter the recipient's phone number: ")

    # Validate the phone number format using regex
    phone_number_pattern = re.compile(r'^\d{10}$')  # Assumes 10-digit phone number format
    if not phone_number_pattern.match(recipient_phone_number):
        print("Invalid phone number format. Please enter a 10-digit phone number.")
        return
    
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

# Call the function to send a random SMS message
send_random_sms_message()
