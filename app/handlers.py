from .data_handlers import clean_company_name
from .services import get_db_connection, list_coll


# Get data from SQLite Database


def get_raw_data():
    conn = get_db_connection()

    cursor = conn.cursor()
    companies_from_db = cursor.execute('SELECT * FROM companies').fetchall()
    # Get number of rows in table
    # count = conn.execute('SELECT COUNT(*) FROM companies').fetchone()[0]
    conn.close()

    return companies_from_db


def get_total_companies(companies, offset=0, per_page=10):
    return companies[offset: offset + per_page]


def get_companies(companies):
    new_companies = []

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


def get_db_data():
    # Get data from DB
    companies = get_raw_data()

    # Return list of dictionaries
    result = get_companies(companies)

    return result


# <-- Work With MongoDB -->
# pymongo

def insert_data_to_db():
    companies = get_db_data()

    for i in range(len(companies)):
        company = {
            "name": clean_company_name(companies[i]["name"]),
            "country_iso": companies[i]["country_iso"],
            "city": companies[i]["city"],
            "nace": companies[i]["nace"],
            "website": companies[i]["website"],
        }
        list_coll.insert_one(company)

# Get All Data from MongoDB


def get_all_mongo_data():
    data = list(list_coll.find({}))
    return data


def count_all_records():
    records = list_coll.count_documents({})
    return records


def delete_all_data():
    list_coll.delete_many({})
