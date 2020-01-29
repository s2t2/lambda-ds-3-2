
import os
import sqlite3
from pprint import pprint

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "chinook.db")

conn = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", type(conn)) #> <class 'sqlite3.Connection'>

# h/t: https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name
conn.row_factory = sqlite3.Row

curs = conn.cursor()
print("CURSOR:", type(curs)) #> <class 'sqlite3.Cursor'>

queries = [
    #"SELECT COUNT(customerId) FROM customers;",
    "SELECT * FROM customers LIMIT 3;"
]

for query in queries:
    print("--------------")
    print(f"QUERY: '{query}'")

    #obj = curs.execute(query)
    #print("OBJ", type(obj))
    #print(obj) #> <class 'sqlite3.Cursor'>

    results = curs.execute(query).fetchall()
    print("RESULTS:", type(results))
    print(results)

    print(type(results[0])) #> type(results[0])
    breakpoint()
