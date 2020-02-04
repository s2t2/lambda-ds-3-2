






import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import json
import pandas as pd

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

#
# QUERY THE TABLE
#

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
CSV_ABSPATH = os.path.abspath(CSV_FILEPATH)
print("CSV FILEPATH", CSV_ABSPATH)

query = f"COPY passengers2 FROM '{CSV_ABSPATH}';"
print("-------------------")
print("SQL:", query)
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

#> psycopg2.errors.InsufficientPrivilege: must be superuser or a member of the pg_read_server_files role to COPY from a file
#> HINT:  Anyone can COPY to stdout or from stdin. psql's \copy command also works for anyone.

# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()

cursor.close()
connection.close()
