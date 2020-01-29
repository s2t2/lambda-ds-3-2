
import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")

conn = sqlite3.connect(DB_FILEPATH)

curs = conn.cursor()

query = "SELECT COUNT(customerId) FROM customers;"
print("SQL", query)
#curs.execute(query)

results = curs.execute(query).fetchall()
print("RESULTS", results)
