from flask import Flask
from flask import render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import sqlite3

app = Flask(__name__)
# Get DB connections
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data"
# db = SQLAlchemy(app)



@app.route('/')
def home():  # put application's code here

    return render_template("home.html")


@app.route('/raw-data')
def get_raw_data():
    conn = get_db_connection()
    companies = conn.execute('SELECT * FROM companies').fetchall()
    conn.close()
    return render_template("raw_data.html", companies=companies)


@app.route('/show-data')
def show_data():
    return render_template("show_data.html")


def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    app.run(debug=True)
