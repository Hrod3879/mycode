import json

def load_json(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        list or None: The loaded JSON data as a list of dictionaries or None if the file doesn't exist.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None

def get_user_choice(options, prompt):
    """
    Display a menu and get user choice.

    Args:
        options (list): List of options to display.
        prompt (str): The prompt message to inform the user about their choice.

    Returns:
        str: The selected option chosen by the user.
    """
    while True:
        print(prompt)  # Inform the user what they are choosing
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = input("Enter the number corresponding to your choice: ")  # Get user's choice
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]  # Return the user's choice
        else:
            print("Invalid choice. Please enter a valid number.")

# Load computer model data from the JSON file
computer_models = load_json('computer_models.json')

if computer_models is None:
    print("Error: Could not load computer model data.")
else:
    # User input for OS selection
    unique_os = list(set(model["os"] for model in computer_models))  # Extract unique OS values
    selected_os = get_user_choice(unique_os, "Available operating systems:")  # Get user's OS choice

    # User input for vendor selection
    os_vendors = [model["vendor"] for model in computer_models if model["os"] == selected_os]
    selected_vendor = get_user_choice(os_vendors, f"Available vendors for {selected_os}:")

    # Create a dictionary to map selected computer models to their prices
    purchase = {model["model"]: model["price"] for model in computer_models if model["os"] == selected_os and model["vendor"] == selected_vendor}

    # Modify the purchase dictionary to include models that do not depend on the selected vendor
    purchase.update({model["model"]: model["price"] for model in computer_models if model["os"] == selected_os and model["vendor"] == "Apple"})

    # Check if there are any matching models
    matching_models = [model["model"] for model in computer_models if model["os"] == selected_os and (model["vendor"] == selected_vendor or model["vendor"] == "Apple")]

    # User input for quantity
    while True:
        quantity = input(f"Enter the quantity of {selected_vendor} laptops with {selected_os}: ")
        if quantity.isdigit():
            quantity = int(quantity)
            break
        else:
            print("Invalid quantity input. Please enter a valid number.")

    # Check if any matching models were found
    if matching_models:
        # Calculate the total cost based on the quantity
        if quantity < 10:
            total_cost = quantity * purchase[selected_vendor]
        elif 10 <= quantity <= 20:
            total_cost = quantity * purchase[selected_vendor] * 0.95
        else:
            total_cost = quantity * purchase[selected_vendor] * 0.9

        print(f"Total cost for {quantity} {selected_vendor} laptops with {selected_os}: ${total_cost:.2f}")
    else:
        print(f"No laptops found for {selected_vendor} with {selected_os}.")
