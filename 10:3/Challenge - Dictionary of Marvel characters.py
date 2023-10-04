# Dictionary of Marvel characters and their information
marvelchars = {
    "starlord": {
        "real name": "Peter Quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "mystique": {
        "real name": "Raven Darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "hulk": {
        "real name": "Bruce Banner",
        "powers": "super strength",
        "archenemy": "Adrenaline"
    }
}

while True:
    # Prompt the user for the character name
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ").strip().lower()

    # Check if the character name is in the dictionary
    if char_name in marvelchars:
        # Prompt the user for the character statistic
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").strip().lower()

        # Check if the character statistic is in the dictionary for the specified character
        if char_stat in marvelchars[char_name]:
            # Get the value for the specified character and statistic
            value = marvelchars[char_name][char_stat]
            # Capitalize the first letters of each word in the real name
            if char_stat == "real name":
                value = value.title()
            # Print the result
            print(f"{char_name.capitalize()}'s {char_stat} is: {value}")
        else:
            print(f"Sorry, '{char_stat}' is not a valid statistic for {char_name.capitalize()}.")
    else:
        print(f"Sorry, '{char_name}' is not a valid character.")

    # Ask the user if they want to try again
    try_again = input("Do you want to try again? (yes/no): ").strip().lower()
    if try_again != "yes":
        break
