# shared by Zach from DS 14!
# https://lambda-students.slack.com/archives/GT7MZ0TKK/p1589395061441200

import os
from sqlalchemy import create_engine
import sqlite3
from dotenv import load_dotenv
import pandas as pd

# Set up .env variables to connect to postgres later

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

# Instantiate titanic data

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
df = pd.read_csv(CSV_FILEPATH)

# Change the columns to be more sql friendly

df.columns = ['survived', 'pclass', 'name', 'sex', 'age', 'siblings_spouses_aboard', 'parents_children_aboard', 'fare']
print(df.columns)

# Set connection to PostgreSQL

sql_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
engine = create_engine(sql_url)

# Copy df to new table in PostgreSQL
df.to_sql('titanic_data', engine, if_exists='replace')
