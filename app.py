from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__) # create instance of flask

# define how to access the page
@app.route("/")
def home():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True) # to not always rerun the server