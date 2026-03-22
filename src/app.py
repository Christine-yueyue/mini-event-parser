from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Mini Event Parser!"

@app.route("/parse", methods=["POST"])
def parse_event():
    data = request.get_json()
    text = data.get("text", "")

    result = {
        "event_name": "Unknown Event",
        "date": "Unknown",
        "time": "Unknown",
        "location": "Unknown"
    }

    # simple eventName parsing, e.g. "Workshop"
    if "workshop" in text.lower():
        result["event_name"] = "Workshop"

    # simple location parsing, e.g. "Ottawa"
    if "ottawa" in text.lower():
        result["location"] = "Ottawa"

    # simple date parsing, e.g. "this Monday", "next Friday"
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for day in days:
        if day in text.lower():
            if "this " + day in text.lower():
                result["date"] = "this " + day.capitalize()
            elif "next " + day in text.lower():
                result["date"] = "next " + day.capitalize()
            else:
                result["date"] = day.capitalize()
            break

    # simple time parsing, e.g. 2 PM, 10 AM, 2:30 PM
    time_match = re.search(r'\b\d{1,2}(:\d{2})?\s?(AM|PM)\b', text, re.IGNORECASE)
    if time_match:
        result["time"] = time_match.group()
    

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)