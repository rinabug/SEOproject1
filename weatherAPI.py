import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')

def fetch_weather(name):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={name}&apikey={API_KEY}"
    headers = {
        "accept": "application/json",
        "location": name,
        }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch weather data: {response.status_code}")

#if __name__ == "__main__":
 #   fetch_weather('newyork')