import requests
from flask_paginate import get_page_parameter, Pagination
# from .models import Company
from .handlers import *
from app import app
from flask import Flask, request, render_template, redirect, url_for


# Create routes for app
@app.route('/api/get-data', methods=["GET"])
def get_data():
    data = get_db_data()
    return data

@app.route('/api/insert-data')
def insert_data():
    insert_data_to_db()
    return "Done"


@app.route('/raw-data', methods=["POST", "GET"])
def show_raw_data():
    # Clicked on button Migrate Data
    if request.method == "POST" and request.form.get("btn-migrate"):
        url = "http://127.0.0.1:5000//api/insert-data"
        request_api = requests.get(url)

        if request_api.status_code == 200:
            return redirect('show-data')

    # Data from Database
    companies = get_raw_data()

    total = len(companies)  # length of list
    btn_migrate_flag = False

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
                           btn_migrate_flag=btn_migrate_flag,
                           )


@app.route('/show-data', methods=["GET", "POST"])
def show_data():
    companies = get_all_mongo_data()
    records = count_all_records()

    # Check if DB is empty
    if request.method == "GET" and records == 0:
        records_flag = True
        return render_template('show_data.html', records_flag=records_flag)

    if request.method == "POST" and request.form.get("btn-delete-all-records"):
        # delete_all_data()
        records_flag = True
        return render_template('show_data.html', records_flag=records_flag)

    # Set Pagination
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    offset = (page - 1) * per_page

    # Setting up the pagination variable, where using len(total) to set the total items available
    pagination_companies = get_total_companies(companies=companies, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=records, css_framework='bootstrap5')

    return render_template("show_data.html",
                           records=records,
                           companies=pagination_companies,
                           pagination=pagination,
                           page=page,
                           per_page=per_page,
                           )


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.form.get("btn-home-migrate"):
        url = "http://127.0.0.1:5000/api/get-data"
        request_api = requests.get(url)

        if request_api.status_code == 200:
            return redirect('raw-data')

    return render_template("home.html")
