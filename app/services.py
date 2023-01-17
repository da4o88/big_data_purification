import sqlite3
from app import app
from flask_mongoengine import MongoEngine

# Connect to SQLite Database


def get_db_connection():
    conn = sqlite3.connect('data.db')
    # Return Memory Location of Objects, without return dictionary
    conn.row_factory = sqlite3.Row
    return conn


# Connect to MongoDB

app.config['MONGODB_SETTINGS'] = {
    'db': 'company_db',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)
