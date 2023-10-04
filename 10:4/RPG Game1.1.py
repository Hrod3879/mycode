import json

# Load game data from the JSON file
with open('game_data1.1.json', 'r') as file:
    game_data = json.load(file)

# Initialize player's inventory
inventory = []

# Set the starting room
current_room = 'entrance'

# Game loop
while True:
    # Display the current room description
    print(game_data['rooms'][current_room]['description'])

    # Check if there are items in the current room
    if 'items' in game_data['rooms'][current_room]:
        items_in_room = game_data['rooms'][current_room]['items']
        print("You see the following items in the room:", ', '.join(items_in_room))

    # Prompt the player for input
    action = input('What do you want to do? (north/east/south/west/pick up/equip/quit): ').lower()

    # Check for valid actions
    if action in game_data['rooms'][current_room]:
        current_room = game_data['rooms'][current_room][action]
    elif action == 'quit':
        print('You quit the game. Goodbye!')
        break
    elif action == 'pick up':
        if 'items' in game_data['rooms'][current_room]:
            item_to_pick_up = input('Enter the name of the item you want to pick up: ')
            if item_to_pick_up in items_in_room:
                inventory.append(item_to_pick_up)
                items_in_room.remove(item_to_pick_up)
                print(f'You picked up the {item_to_pick_up}.')
            else:
                print(f'The {item_to_pick_up} is not in this room.')
        else:
            print('There are no items in this room to pick up.')
    elif action == 'equip':
        if inventory:
            item_to_equip = input('Enter the name of the item you want to equip: ')
            if item_to_equip in inventory:
                if game_data['items'][item_to_equip]['equipable']:
                    print(f'You have equipped the {item_to_equip}.')
                else:
                    print(f'You cannot equip the {item_to_equip}.')
            else:
                print(f'You do not have a {item_to_equip} in your inventory.')
        else:
            print('Your inventory is empty.')
    else:
        print('Invalid action. Try again.')
