from flask import Flask
from flask import render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sqlite3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data"
db = SQLAlchemy(app)


@app.route('/')
def home():  # put application's code here
    companies = db.Query
    return render_template("home.html")


@app.route('/raw-data')
def get_raw_data():
    return render_template("raw_data.html")


@app.route('/show-data')
def show_data():
    return render_template("show_data.html")


if __name__ == '__main__':
    app.run()