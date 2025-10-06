import requests
from flask import Flask, render_template

app = Flask(__name__)

access_key = "3f6c024514d2f3d0a8c8da3a2a6ed0cf"

def data_practice():
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url)
    data = response.json()
    print(data["text"])

data_practice()


# @app.route('/')
# def index():
#
#     return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)