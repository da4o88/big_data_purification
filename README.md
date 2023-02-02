# Big Data Purification
Big Data Purification is a Flask application which uses the ETL process, to extract data from SQLite database, which contains names of companies and additional information about them, make transformation on the names of companies and then load them in Mongo database.
Flask app is consist of web application elements(HTML, CSS) and two API functions endpoints.

# Additional Information

- First API function is to read data from sqlite database and use GET method.
- Second API function use POST method and make changes to the names (remove brackets and text inside them, capitalize the names of each company and etc.) and insert the modified data into mongo database, where key is the name of the company and attributes are the additional information about company.


# Techologies


Techologies used in this app are:
- Python 3.11
- Flask ver. 2.2.2
- SQLAlchemy ver.1.4.46
- Bootstrap5
- SQLite
- MongoDB
