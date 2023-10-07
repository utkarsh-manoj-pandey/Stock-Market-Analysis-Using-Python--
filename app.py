from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["weather_data"]
collection = db["weather_records"]

@app.route("/")
def index():
    # Fetch weather data from MongoDB
    weather_data = list(collection.find({}))
    return render_template("index.html", weather_data=weather_data)

@app.route("/api/weather_data")
def api_weather_data():
    # Fetch weather data from MongoDB as JSON
    weather_data = list(collection.find({}))
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug=False)





