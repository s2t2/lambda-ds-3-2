
import os
from dotenv import load_dotenv
import psycopg2
import json

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

print("-------------------")
query = "SELECT usename, usecreatedb, usesuper, passwd FROM pg_user;"
print("SQL:", query)
cursor.execute(query)
for row in cursor.fetchall()[0:10]:
    print(row)



#
# CREATE THE TABLE
#

table_name = "test_table2"

print("-------------------")
query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
  id SERIAL PRIMARY KEY,
  name varchar(40) NOT NULL,
  data JSONB
);
"""
print("SQL:", query)
cursor.execute(query)

#
# INSERT SOME DATA
#

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

#print("-------------------")
#query = f"""
#INSERT INTO {table_name} (name, data) VALUES
#(
#  'A row name',
#  null
#),
#(
#  'Another row, with JSON',
#  '{json.dumps(my_dict)}'::JSONB
#);
#"""
#print("SQL:", query)
#curs.execute(query)

#print("-------------------")
#query = f"""
#INSERT INTO {table_name} (name, data) VALUES
#(
#  'A row name',
#  null
#),
#(
#  'Another row, with JSON',
#  '{json.dumps(my_dict)}'::JSONB
#);
#"""
#print("SQL:", query)
#curs.execute(query)

insertion_query = f"INSERT INTO {table_name} (name, data) VALUES (%s, %s)"
cursor.execute(insertion_query,
  ('A rowwwww', 'null')
)
cursor.execute(insertion_query,
  ('Another row, with JSONNNNN', json.dumps(my_dict))
)



#
# QUERY THE TABLE
#

print("-------------------")
query = f"SELECT * FROM {table_name};"
print("SQL:", query)
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()

cursor.close()
connection.close()
