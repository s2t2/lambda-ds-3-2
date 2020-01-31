
# DOESN'T WORK WITH PG

#import os
#import pandas as pd
#from dotenv import load_dotenv
#import psycopg2
#
#load_dotenv()
#
#DB_HOST = os.getenv("DB_HOST", default="OOPS")
#DB_NAME = os.getenv("DB_NAME", default="OOPS")
#DB_USER = os.getenv("DB_USER", default="OOPS")
#DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
#
#connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
#print("CONNECTION", type(connection))
#
#CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")
#df = pd.read_csv(CSV_FILEPATH)
#df.index.rename("id", inplace=True) # assigns a column label "id" for the index column
#df.index += 1 # starts ids at 1 instead of 0
#print(df.head())
#
#table_name = "reviews"
#df.to_sql(table_name, con=connection)
#
#cursor = connection.cursor()
#cursor.execute(f"SELECT count(distinct id) as review_count FROM {table_name};")
#results = cursor.fetchone()
#print(results, "RECORDS")
#
