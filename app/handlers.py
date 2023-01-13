from .services import get_db_connection

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
