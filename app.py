from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home():
	return url_for("home.html")

@app.route("/lawyers")
def lawyers():
	return url_for("lawyers.html")

@app.route("/rights")
def rights():
	return url_for("rights.html")


if __name__ == '__main__':
    app.run(debug=True)