from flask import Flask

app = Flask(__name__)
i = 0

@app.route("/")
def hello_world():
    global i
    i = i + 1
    return "<p>You are the " + str(i) + " users to visit the site.</p>"

app.run(debug=True)