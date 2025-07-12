weather_data = {
    "london": {"temperature": 18, "humidity": 55, "pressure": 1015},
    "paris": {"temperature": 22, "humidity": 48, "pressure": 1011}
}

def get_weather(city):
    data = weather_data[city.lower()]
    if data is not None:
        return {
            "temperature": data["temperature"],
            "humidity": data["humidity"],
            "pressure": data["pressure"],
            "city": city
        }
    return {"error": f"Could not retrieve weather for {city}"}
