import requests

# Define the URL of the API
url = "https://pokeapi.co/api/v2/pokemon/1/"

try:
    # Make an HTTP GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Display some interesting data from the response
        print("Name: ", data["name"])
        print("Height: ", data["height"])
        print("Weight: ", data["weight"])
        print("Abilities: ", [ability["ability"]["name"] for ability in data["abilities"]])
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error making the request:", e)
