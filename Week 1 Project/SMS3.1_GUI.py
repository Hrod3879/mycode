# created relative path for the config.json and Quote_Bank.json files


import os
import json
import random
from twilio.rest import Client
import PySimpleGUI as sg

def send_random_sms_message(recipient_phone_number):
    # Get the current working directory where the python script is located
    current_dir = os.getcwd()

    # Construct the path to config.json and Quote_Bank.json relative to the current directory
    config_path = os.path.join(current_dir, "config.json")
    quote_bank_path = os.path.join(current_dir, "Quote_Bank.json")

    # Load configuration from config.json
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    # Extract values from the loaded configuration
    account_sid = config["account_sid"]
    auth_token = config["auth_token"]
    twilio_phone_number = config["twilio_phone_number"]

    # Load quotes from JSON file
    with open(quote_bank_path, "r") as file:
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
        sg.popup(f"Your message has been sent to {recipient_phone_number}!!! Here is your SID: {message.sid}")
    except Exception as e:
        sg.popup_error(f"An error occurred: {str(e)}")
        
# **GUI CONFIG**

# Define the initial layout for the PySimpleGUI window
initial_layout = [
    [sg.Text("Welcome to my the Random SMS Sender!")],
    [sg.Text("Please review the terms and conditions below:")],
    [sg.Multiline("1. This program sends random SMS messages using Twilio.\n"
                  "2. This account is on a trial that will expire in a few days.\n"
                  "3. By clicking 'Accept,' you agree to the terms and conditions, as well as the limitations of the program.\n"
                  "4. You also agree to buy me a few beers of my choice, maybe shots as well lol.", size=(80, 10))],
    [sg.Button("Accept"), sg.Button("Decline")]
]

# Create the initial window
window = sg.Window("Random SMS Sender", initial_layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Accept":
        window.close()  # Close the initial window

        # Define the layout for the program window after accepting terms
        program_layout = [
            [sg.Text("You have accepted the terms and conditions.")],
            [sg.Text("Enter the recipient's phone number:")],
            [sg.InputText(key="-PHONE_NUMBER-")],
            [sg.Button("Send SMS")],
            [sg.Text("", key="-RESULT-", size=(70, 1), text_color="green")]
        ]

        # Create the program window
        program_window = sg.Window("Random SMS Sender", program_layout)

        while True:
            event, values = program_window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Send SMS":
                recipient_phone_number = values["-PHONE_NUMBER-"]
                if recipient_phone_number:
                    send_random_sms_message(recipient_phone_number)

        program_window.close()  # Close the program window when done

window.close()  # Close the initial window
