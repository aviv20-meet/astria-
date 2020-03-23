from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home():
	return render_template("home.html")

@app.route("/lawyers")
def lawyers():
	lawyers = get_all_lawyers()
	return render_template("lawyers.html", lawyers = lawyers)

@app.route("/rights")
def rights():
	rights = get_all_rights()
	laws = get_all_laws()
	return render_template("rights.html",rights = rights,laws = laws)

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("index.html")

@app.route("/contact")
def contact():
	return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)