import plivo
import json

def send_plivo_messages(auth_id, auth_token, json_file, sender_number, recipient_numbers):
    # Load the message details from the JSON file
    with open(json_file, 'r') as file:
        message_data = json.load(file)

    # Initialize the Plivo client
    client = plivo.RestClient(auth_id, auth_token)

    # Send each SMS message from the loaded data
    responses = []
    for message_text in message_data["sms_messages"]:
        for recipient_number in recipient_numbers:
            response = client.messages.create(
                src=sender_number,
                dst=recipient_number,
                text=message_text
            )
            responses.append(response)

    return responses

# Usage example
if __name__ == "__main__":
    auth_id = '<YOUR_AUTH_ID>'
    auth_token = '<YOUR_AUTH_TOKEN>'
    json_file = 'message.json'
    sender_number = 'YOUR_SENDER_PHONE_NUMBER'
    recipient_numbers = ['RECIPIENT_PHONE_NUMBER_1', 'RECIPIENT_PHONE_NUMBER_2', 'RECIPIENT_PHONE_NUMBER_3']  # Add recipient numbers here

    responses = send_plivo_messages(auth_id, auth_token, json_file, sender_number, recipient_numbers)
    for response in responses:
        print(response)
