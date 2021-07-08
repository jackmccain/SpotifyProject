from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests
import random
import spotify_auth
from datetime import date

load_dotenv()

SPOTIFY_AUTHORIZATION = spotify_auth.get_bearer_token()

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Welcome. </p>"


@app.route("/album")
def getalbum():
    response = requests.get(
        "https://api.spotify.com/v1/albums",
        params={
            "ids": "3XLn9BkDkwq4icsUye2Krp,1oNWum7uuaISS4cSgDQhWT,2If8WvHmIANFsGWDf36e2M,2vmjRfAgNyYIiFsHuUU8u9"
        },
        headers={"Authorization": SPOTIFY_AUTHORIZATION},
    ).json()

    
    i = random.randint(0, 3)
    j=random.randint(0,3)
    while j == i:
        j = random.randint(0, 3)

    album1 = response["albums"][i]
    album2 = response["albums"][j]
    albumdate1 = album1["release_date"]
    albumdate2 = album2["release_date"]
    year1 = int(albumdate1[0:4])
    month1 = int(albumdate1[5:7])
    day1 = int(albumdate1[8:10])

    year2 = int(albumdate2[0:4])
    month2 = int(albumdate2[5:7])
    day2 = int(albumdate2[8:10])

    d0 = date(year1, month1, day1)
    d01 = date(year2, month2, day2)
    d1 = date.today()
    delta1 = d1 - d0
    delta2 = d1 - d01
    daysbetween1 = delta1.days
    daysbetween2 = delta2.days
    days1 = str(daysbetween1)
    days2 = str(daysbetween2)
    name1 = album1["name"]
    name2 = album2["name"]
    image1 = album1["images"][1]["url"]
    image2 = album2["images"][1]["url"]
    
    return render_template("album.html", days1=days1, days2=days2, image1=image1, image2=image2, name1=name1, name2=name2)


app.run(debug=True)
