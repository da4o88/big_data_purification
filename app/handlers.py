from .services import get_db_connection
import json
from bson.objectid import ObjectId
from .models import Company

# Get data from SQLite Database


def get_raw_data():
    conn = get_db_connection()
    companies_from_db = conn.execute('SELECT * FROM "companies"').fetchall()
    conn.close()
    return companies_from_db


def get_companies():
    new_companies = []
    companies = get_raw_data()

    for c in companies:
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


def get_total_companies(companies, offset=0, per_page=10):
    return companies[offset: offset + per_page]


# <-- Work With MongoDB -->
# Add data to MongoDB

def get_and_import_data():
    conn = get_db_connection()

    # Get number of rows in table
    count = conn.execute('SELECT COUNT(*) FROM companies').fetchone()[0]
    print(count)



def add_data():
    company = Company()
    company.name = "Lost in Translation"
    company.city = "New Somewhere"
    company.country_iso = 'MKD'

    company.save()


def show_company_data():
    output = []
    companies = Company.objects

    for comp in companies:
        output.append(comp)

    return output

# Delete Data in DB


def delete_all_data():
    companies = Company.objects

    for company in companies:
        company.delete()