from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["weather_data"]
collection = db["weather_records"]

# Fetch weather data from MongoDB
weather_data = list(collection.find({}))

for data in weather_data:
    print(data)
