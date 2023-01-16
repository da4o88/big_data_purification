from .services import get_db_connection
from .models import Company
from .data_handlers import clean_company_name


# Get data from SQLite Database


def get_raw_data():
    conn = get_db_connection()
    companies_from_db = conn.execute('SELECT * FROM "companies"').fetchall()
    # Get number of rows in table
    # count = conn.execute('SELECT COUNT(*) FROM companies').fetchone()[0]
    conn.close()
    return companies_from_db


def get_total_companies(companies, offset=0, per_page=10):
    return companies[offset: offset + per_page]


def get_companies(companies):
    new_companies = []
    # companies = get_raw_data()

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


# <-- Work With MongoDB -->
# Add data to MongoDB

def add_data(all_companies):
    companies = get_companies(all_companies)

    # Insert data in Mongo DB

    for c in companies:
        company = Company()
        # company.id = c['id']
        company.name = clean_company_name(c['name'])
        company.country_iso = c['country_iso']
        company.city = c['city']
        company.nace = c['nace']
        company.website = c['website']
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
