from app import app
from flask import render_template, redirect, request, url_for, Response
from flask_paginate import Pagination, get_page_args, get_page_parameter
from .handlers import get_companies, get_total_companies, get_raw_data


@app.route('/')
def home():  # put application's code here

    return render_template("home.html")


@app.route('/raw-data', methods=["POST", "GET"])
def show_raw_data():

    if request.method == "POST" and request.form.get("btn-migrate"):
        return redirect('/show-data')

    # Data from Database
    companies = get_raw_data()

    # companies = get_companies()  # list
    total = len(companies)  # length of list

    # Set Pagination
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    offset = (page - 1) * per_page

    # Setting up the pagination variable, where using len(total) to set the total items available
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
