# -*- coding:utf-8 -*-

from flask import Flask, render_template
import requests

app = Flask(__name__)
r = requests.get('http://data.citedia.com/r1/parks?crs=EPSG:4326').json()

res = []
for i in r["parks"]:
    for j in r["features"]["features"]:
        if i["id"] == j["id"]:
            tmpCoordY = j["geometry"]["coordinates"][0]
            tmpCoordX = j["geometry"]["coordinates"][1]
    percent = i["parkInformation"]["free"] / i["parkInformation"]["max"] * 100
    revertPercent = 100 - percent
    if percent <= 10 or i["parkInformation"]["free"] <= 20:
        color = "orange"
    else:
        color = "green"

    if i["parkInformation"]["status"] == "FULL" or i["parkInformation"]["status"] == "CLOSED":
        color = "red"

    tmp = {
        "nom": i["parkInformation"]["name"],
        "status": i["parkInformation"]["status"],
        "nbPlaces": i["parkInformation"]["max"],
        "placesDispo": i["parkInformation"]["free"],
        "coordX": tmpCoordX,
        "coordY": tmpCoordY,
        "percent": int(i["parkInformation"]["free"] / i["parkInformation"]["max"] * 100),
        "revertPercent": int(revertPercent),
        "color": color
    }
    res.append(tmp)
    tmpCoordX = ""
    tmpCoordY = ""

print(res)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parking')
def parking():
    return render_template('parking.html', data=res)

@app.route("/hello")
def hello():
    names = ["a","b"]
    return render_template('hello.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)


