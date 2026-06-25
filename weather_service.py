import requests
from config import API_KEY

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url, timeout=5)
        data = res.json()

        if res.status_code != 200:
            return None

        return {
            "temp": data["main"]["temp"],
            "wind": data["wind"]["speed"],
            "condition": data["weather"][0]["main"]
        }

    except:
        return None


def analyze_risk(weather):
    if not weather:
        return "UNKNOWN"

    risk_score = 0

    if weather["wind"] > 12:
        risk_score += 2
    if weather["temp"] > 35:
        risk_score += 1

    bad_weather = ["storm", "rain", "thunderstorm", "haze"]
    if weather["condition"].lower() in bad_weather:
        risk_score += 3

    if risk_score <= 1:
        return "LOW"
    elif risk_score <= 3:
        return "MODERATE"
    else:
        return "HIGH"