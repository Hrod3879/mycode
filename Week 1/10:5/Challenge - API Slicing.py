#!/usr/bin/env python3

import requests

def main():
    pokenum = input("Pick a number between 1 and 151!\n>")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # Slicing (NO for loop!)
    front_default_url = pokeapi["sprites"]["front_default"]
    print("Front Default Image URL:", front_default_url)

    # Slicing WITH a for loop!
    print("Moves:")
    for move in pokeapi["moves"]:
        move_name = move["move"]["name"]
        print(move_name)

    # Loop or **NOT** to Loop
    game_indices_count = len(pokeapi["game_indices"])
    print("Total Games:", game_indices_count)

if __name__ == "__main__":
    main()
