from urllib import request

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

access_key = "3f6c024514d2f3d0a8c8da3a2a6ed0cf"

def get_from_api(city: str):
    return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={access_key}&units=metric").json()


@app.route('/', methods=['GET', 'POST'])
def data_practice():
    if request.method == 'POST':
        city = request.form.get('city')
    else:
        city=('Exeter')

    data = get_from_api(city)

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    return render_template("index.html", weather = weather, temp = temperature, city = city)


if __name__ == "__main__":
    app.run(debug=True)