from flask import Flask, request, render_template
import json
from flask_cors import cross_origin
from loguru import logger


app = Flask(__name__)
app.secret_key="akdfhaksdfhaf"


@app.route('/index')
def index():
    return render_template("login.html")


@app.route("/login", methods=['post'])
# @cross_origin()
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    logger.info(username)
    logger.info(password)
    return None


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=1908, debug=True)


