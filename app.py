from flask import Flask
from flask import render_template, redirect, request
import sqlite3
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)

ROWS_PER_PAGE = 10


@app.route('/')
def home():  # put application's code here

    return render_template("home.html")


@app.route('/raw-data')
def show_raw_data():
    # new_companies = []
    # companies = get_raw_data()
    #
    # for c in companies:
    #     company = {
    #         "id": c['id'],
    #         "name": c['name'],
    #         "country_iso": c['country_iso'],
    #         "city": c['city'],
    #         "nace": c['nace'],
    #         "website": c['website']
    #     }
    #     new_companies.append(company)

    return render_template("raw_data.html", companies=companies)


@app.route('/show-data')
def show_data():
    return render_template("show_data.html")


def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_raw_data():
    conn = get_db_connection()
    companies_from_db = conn.execute('SELECT * FROM companies').fetchall()
    conn.close()

    return companies_from_db


def get_companies():
    new_companies = []
    companies_from_db = get_raw_data()

    for c in companies_from_db:
        company = {
            "id": c['id'],
            "name": c['name'],
            "country_iso": c['country_iso'],
            "city": c['city'],
            "nace": c['nace'],
            "website": c['website']
        }
        new_companies.append(company)
    return new_companies


companies = get_companies()

if __name__ == '__main__':
    app.run(debug=True)
