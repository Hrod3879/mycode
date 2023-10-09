import requests

def get_iss_location():
    api_url = "http://api.open-notify.org/iss-now.json"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            
            # latitude and longitude
            lon = data['iss_position']['longitude']
            lat = data['iss_position']['latitude']
            
            # Print format
            print("CURRENT LOCATION OF THE ISS:")
            print(f"Longitude: {lon}")
            print(f"Latitude: {lat}")
        else:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    get_iss_location()
