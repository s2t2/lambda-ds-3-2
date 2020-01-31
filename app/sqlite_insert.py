import os
import pandas as pd
import sqlite3

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.db")

connection = sqlite3.connect(DB_FILEPATH)
table_name = "reviews2"

df = pd.read_csv(CSV_FILEPATH)
df.index.rename("id", inplace=True) # assigns a column label "id" for the index column
df.index += 1 # starts ids at 1 instead of 0
print(df.head())
df.to_sql(table_name, con=connection)

cursor = connection.cursor()
cursor.execute(f"SELECT count(distinct id) as review_count FROM {table_name};")
results = cursor.fetchone()
print(results, "RECORDS")
