
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(conn))

curs = conn.cursor()
print("CURSOR", type(curs))

print("-------------------")
query = "SELECT usename, usecreatedb, usesuper, passwd FROM pg_user;"
print("SQL:", query)
curs.execute(query)
for row in curs.fetchall()[0:10]:
    print(row)






print("-------------------")
query = """
CREATE TABLE IF NOT EXISTS test_table2 (
  id SERIAL PRIMARY KEY,
  name varchar(40) NOT NULL,
  data JSONB
);
"""
print("SQL:", query)
curs.execute(query)

print("-------------------")
query = """
INSERT INTO test_table2 (name, data) VALUES
(
  'A row name',
  null
),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
);
"""
print("SQL:", query)
curs.execute(query)

print("-------------------")
query = f"SELECT * FROM test_table2;"
print("SQL:", query)
curs.execute(query)
for row in curs.fetchall():
    print(row)

# ACTUALLY SAVE THE TRANSACTIONS
conn.commit()

curs.close()
conn.close()
