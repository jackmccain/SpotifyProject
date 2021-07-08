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

SPOTIFY_DATA = requests.get(
    "https://api.spotify.com/v1/albums",
    params={
        "ids": "45ba6QAtNrdv6Ke4MFOKk9,3lajefIuUk4SfzqVBSJy8p,7z4GhRfLqfSkqrj5F3Yt2B,1lXY618HWkwYKJWBRYR4MK,6PBZN8cbwkqm1ERj2BGXJ1,42WVQWuf1teDysXiOupIZt,4GNIhgEGXzWGAefgN5qjdU,41GuZcammIkupMPKH2OJ6I,6pwuKxMUkNg673KETsXPUV,20r762YmB5HeofjMCiPMLv,4Uv86qWpGTxf7fU7lG5X6F,5fPglEDz9YEwRgbLRvhCZy,7gsWAHLeT0w7es6FofOXk1,7ycBtnsMtyVbbwTfJwRjSP,4eLPsYPBmXABThSJ821sqY,2VBcztE58pBKjIDS5oEgFh"
    },
    headers={"Authorization": SPOTIFY_AUTHORIZATION},
).json()


@app.route("/")
def home():
    return "<p>Welcome. </p>"


@app.route("/album")
def getalbum():

    for idx, album in enumerate(SPOTIFY_DATA["albums"]):
        if album is None:
            print(f"{idx} is none")
        else:
            print(f"{idx} is NOT none")

    response = SPOTIFY_DATA
    num_albums = len(response["albums"])
    i = random.randint(0, num_albums - 1)
    j = random.randint(0, num_albums - 1)
    while i == j:
        i = random.randint(0, 17)

    album1 = response["albums"][i]
    album2 = response["albums"][j]
    albumdate1 = album1["release_date"]
    albumdate2 = album2["release_date"]

    name1 = album1["name"]
    name2 = album2["name"]
    image1 = album1["images"][1]["url"]
    image2 = album2["images"][1]["url"]
    artist1 = album1["artists"][0]["name"]
    artist2 = album2["artists"][0]["name"]

    return render_template(
        "pages/game.html",
        album1=album1,
        album2=album2,
        image1=image1,
        image2=image2,
        name1=name1,
        name2=name2,
        artist1=artist1,
        artist2=artist2,
    )


app.run(debug=True)
