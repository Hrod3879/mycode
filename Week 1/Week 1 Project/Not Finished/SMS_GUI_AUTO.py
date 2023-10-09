# added automation for send sms when needed
# also added the ability to configure automation thru the GUI
# **credit goes to chatgpt for creating the modifiaction code for inserting into GUI**


import json
import random
import re
from twilio.rest import Client
import PySimpleGUI as sg
import schedule
import time

def send_random_sms_message(recipient_phone_number):
    # Load configuration from config.json
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    # Extract values from the loaded configuration
    account_sid = config["account_sid"]
    auth_token = config["auth_token"]
    twilio_phone_number = config["twilio_phone_number"]

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
        sg.popup(f"Your message has been sent to {recipient_phone_number}!!! Here is your SID: {message.sid}")
    except Exception as e:
        sg.popup_error(f"An error occurred: {str(e)}")

def schedule_sms_messages():
    # Schedule the SMS messages to be sent at 8 am and 8 pm
    schedule.every().day.at("08:00").do(send_random_sms_message, recipient_phone_number="RECIPIENT_PHONE_NUMBER_HERE")
    schedule.every().day.at("20:00").do(send_random_sms_message, recipient_phone_number="RECIPIENT_PHONE_NUMBER_HERE")
    schedule.every().day.at(send_time).do(send_random_sms_message, recipient_phone_number=recipient_phone_number)

# GUI CONFIG



# Define the initial layout for the PySimpleGUI window
initial_layout = [
    [sg.Text("Welcome to my the Random SMS Sender!")],
    [sg.Text("Please review the terms and conditions below:")],
    [sg.Multiline("1. This program sends random SMS messages using Twilio.\n"
                  "2. This account is on a trial that will expire in a few days.\n"
                  "3. By clicking 'Accept,' you agree to the terms and conditions, as well as the limitations of the program.\n"
                  "4. You also agree to buy me a few beers of my choice, maybe shots as well.", size=(80, 10))],
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
            [sg.Checkbox("Automate SMS Sending", key="-AUTOMATE_SMS-", default=False)],
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
                automate_sms = values["-AUTOMATE_SMS-"]

                if automate_sms:
                    # Open a new window for setting the automation schedule
                    automation_layout = [
                        [sg.Text("Set the time and date for automated SMS sending:")],
                        [sg.CalendarButton("Select Date", target="-DATE-", key="-CALENDAR-", format="%Y-%m-%d")],
                        [sg.InputText(key="-TIME-", size=(8, 1), justification="center")],
                        [sg.Button("Schedule SMS")],
                    ]

                    automation_window = sg.Window("Automation Schedule", automation_layout)

                    while True:
                        automation_event, automation_values = automation_window.read()

                        if automation_event == sg.WINDOW_CLOSED:
                            break
                        elif automation_event == "-CALENDAR-":
                            selected_date = automation_values["-CALENDAR-"]
                            program_window["-DATE-"].update(selected_date)
                        elif automation_event == "Schedule SMS":
                            selected_date = automation_values["-DATE-"]
                            selected_time = automation_values["-TIME-"]
                            send_time = f"{selected_date} {selected_time}"

                            if selected_date and selected_time:
                                schedule_sms_messages(send_time, recipient_phone_number)
                                sg.popup("SMS automation has been scheduled.")
                                automation_window.close()
                            else:
                                sg.popup_error("Please select both date and time.")
                elif recipient_phone_number:
                    send_random_sms_message(recipient_phone_number)

        program_window.close()  # Close the program window when done

window.close()  # Close the initial window

# Run the scheduled tasks in the background
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
