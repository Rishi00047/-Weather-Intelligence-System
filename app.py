from flask import Flask, render_template, request, jsonify
from routing import shortest_path
from map_service import create_map
from weather_service import get_weather, analyze_risk

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/route", methods=["POST"])
def route():
    start = request.form["start"]
    end = request.form["end"]

    distance, path = shortest_path(start, end)

    create_map(path)

    weather = get_weather(end)
    risk = analyze_risk(weather)

    return jsonify({
        "route": path,
        "distance": distance,
        "weather": weather,
        "risk": risk,
        "map": "route_map.html"
    })


if __name__ == "__main__":
    app.run(debug=True)