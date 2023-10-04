# Basic RPG Game
# By Hrod

import json

# load game rooms from a JSON file
def load_rooms_from_json(file_name):
    with open(file_name, 'r') as json_file:
        return json.load(json_file)

# JSON file name
json_config = 'game_rooms.json'

# check if the JSON file exists and load rooms to variable
try:
    rooms = load_rooms_from_json(json_config)
except FileNotFoundError:
    print(f'The JSON file "{json_config}" does not exist.')
    exit()

# Set starting room
current_room = 'entrance'

# Game loop
while True:
    # Display current room desc
    print(rooms[current_room]['description'])

    # Prompt for input
    action = input('What do you want to do? Choose wisely! (north/east/south/west/quit): ').lower()

    # Check for valid actions
    if action in rooms[current_room]:
        current_room = rooms[current_room][action]
    elif action == 'quit':
        print('Goodbye my friends!')
        break
    else:
        print('Invalid action. Try again.')
