from app import app
from flask import render_template
from flask_paginate import Pagination, get_page_args
from .handlers import get_companies, get_total_companies


@app.route('/')
def home():  # put application's code here

    return render_template("home.html")


@app.route('/raw-data')
def show_raw_data():
    companies = get_companies()
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(companies)
    pagination_companies = get_total_companies(companies=companies, offset=offset, per_page=per_page)
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
