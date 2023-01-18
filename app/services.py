import sqlite3
import pymongo
from app import app
from flask_mongoengine import MongoEngine

# Connect to SQLite Database


def get_db_connection():
    conn = sqlite3.connect('data.db')
    # Return Memory Location of Objects, without return dictionary
    conn.row_factory = sqlite3.Row
    return conn


# Connect to MongoDB

# app.config['MONGODB_SETTINGS'] = {
#     'db': 'company_db',
#     'host': 'localhost',
#     'port': 27017
# }
#
# db = MongoEngine()
# db.init_app(app)

# Connect to MongoDB with pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["company_db"]

list_coll = db["companies"]
print(db.list_collection_names())

list_collections = db.list_collection_names()
if "companies" in list_collections:
    print("The collection exists.")
else:
    print("Collection doesn't exists.")

