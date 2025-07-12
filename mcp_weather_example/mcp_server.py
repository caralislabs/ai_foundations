from flask import Flask, request, jsonify
from weather_api import get_weather

app = Flask(__name__)

@app.route("/resolve_context", methods=["POST"])
def resolve_context():
    req_data = request.json
    intent = req_data.get("intent")
    if intent == "weather_lookup":
        city = req_data.get("city")
        result = get_weather(city)

        return jsonify({"result": result})
    return jsonify({"error": "Unknown intent"}), 400

if __name__ == "__main__":
    app.run(port=5005)
