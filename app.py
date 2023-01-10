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



if __name__ == '__main__':
    app.run()
