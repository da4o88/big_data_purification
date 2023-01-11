from flask import Flask
from flask import render_template, redirect, request
import sqlite3
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here

    return render_template("home.html")


@app.route('/raw-data')
def show_raw_data():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(total_companies)
    pagination_companies = get_total_companies(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap5')

    return render_template("raw_data.html",
                           pagination_companies=pagination_companies,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


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


def get_total_companies(offset=0, per_page=10):
    return total_companies[offset: offset + per_page]


companies = get_companies()
total_companies = companies

if __name__ == '__main__':
    app.run(debug=True)
