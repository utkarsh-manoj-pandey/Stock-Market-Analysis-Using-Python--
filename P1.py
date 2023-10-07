import requests
from pymongo import MongoClient
from datetime import datetime

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(api_key, location):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'  # Use metric units for Celsius
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# List of Indian states and union territories
indian_states_and_ut = [
    "Andaman and Nicobar Islands",
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chandigarh",
    "Chhattisgarh",
    "Dadra and Nagar Haveli",
    "Daman and Diu",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Puducherry",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["weather_data"]
collection = db["weather_records"]

# Example usage:
api_key = '3e918d2b5db8254dca0f76d50b828bc2'  # Replace with your OpenWeatherMap API key

for location in indian_states_and_ut:
    weather_data = fetch_weather_data(api_key, location)

    if weather_data:
        # Extract relevant weather information
        temperature = weather_data['main']['temp']
        conditions = weather_data['weather'][0]['description']

        # Create a document to store in MongoDB
        data_to_store = {
            "location": location,
            "temperature_Celsius": temperature,
            "conditions": conditions,
            "timestamp": datetime.now()
        }

        # Insert the data into MongoDB
        collection.insert_one(data_to_store)
        print(f"Weather data for {location} added to MongoDB.")
    else:
        print(f"Failed to retrieve weather data for {location}.")





