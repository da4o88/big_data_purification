import sqlite3
import pymongo

# Connect to SQLite Database


def get_db_connection():
    """Connect to sqlite database"""
    conn = sqlite3.connect('data.db')
    # Return Memory Location of Objects, without return dictionary
    conn.row_factory = sqlite3.Row
    return conn


# Connect to MongoDB with pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["company_db"]

# Create collection
list_coll = db["companies"]
# print(db.list_collection_names())

# Check if collection exists
list_collections = db.list_collection_names()
# if "companies" in list_collections:
#     print("The collection exists.")
# else:
#     print("Collection doesn't exists.")
