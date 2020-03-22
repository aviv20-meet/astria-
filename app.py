from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/lawyers")
def lawyers():
	return render_template("index.html")

@app.route("/rights")
def rights():
	return render_template("index.html")
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)