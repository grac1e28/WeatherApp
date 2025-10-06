import requests
from flask import Flask, render_template

app = Flask(__name__)

access_key = "3f6c024514d2f3d0a8c8da3a2a6ed0cf"

def get_from_api(city: str):
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={access_key}&units=metric").json()


@app.route('/')
def data_practice():
    weather = get_from_api("Exeter")["weather"][0]["main"]
    return render_template("index.html", weather = weather)


# @app.route('/')
# def index():
#
#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)