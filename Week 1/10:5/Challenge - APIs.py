#!/usr/bin/env python3
""" 
   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   Documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# Imports always go at the top of your code
import requests
import json



# Define our "base" API
API = "https://api.magicthegathering.io/v1/"

def main():
    """Run time code"""

    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()

    # Create resp, which is our request object
    resp = requests.get(f"{API}cards?set={setcode}")

    # The .json() method will dump a JSON string into Pythonic data structures.
    cards = resp.json()

    # Create a file name based on the set code
    filename = f"{setcode}_cards.json"

    # Open the file for writing
    with open(filename, "w") as file:
        # Write the card data to the file in a more readable format (using indentation)
        file.write(json.dumps(cards, indent=4))

    print(f"Card data has been written to {filename}")

if __name__ == "__main__":
    main()
