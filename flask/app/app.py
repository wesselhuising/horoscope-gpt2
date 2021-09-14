import requests
import json

from flask import Flask, render_template, request, abort
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app, content_security_policy=None)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    if request.method == "POST":
        question = request.form["question"]
        r = requests.post(f"http://api:5001/generate?context={question}&max_length=100")
        if r.status_code != 200:
            abort(400)

        content = json.loads(r.content)

        if "horoscope" not in content:
            abort(400)

        if "context" not in content:
            abort(400)

        return render_template(
            "horoscope.html",
            question=content["context"],
            horoscope=content["horoscope"],
        )
    else:
        abort(404)
