import requests

def fetch_apod(date, api_key):
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "date": date,
        "api_key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch APOD. Status code:", response.status_code)
        return None

def main():
    api_key = input("Enter your NASA API key: ")

    date = input("Enter the date (YYYY-MM-DD) for the APOD image: ")

    apod_data = fetch_apod(date, api_key)

    if apod_data:
        title = apod_data.get("title")
        explanation = apod_data.get("explanation")
        url = apod_data.get("url")

        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"Explanation: {explanation}")
        print(f"Image URL: {url}")

if __name__ == "__main__":
    main()
