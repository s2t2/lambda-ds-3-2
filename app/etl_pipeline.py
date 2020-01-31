import json
import os
from dotenv import load_dotenv
import pandas as pd
import sqlite3
import psycopg2
from psycopg2.extras import execute_values

load_dotenv() # looks inside the .env file for some env vars

# passes env var values to python var
DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")

sqlite_connection = sqlite3.connect(DB_FILEPATH)
#sqlite_connection.row_factory = sqlite3.Row
sqlite_cursor = sqlite_connection.cursor()

pg_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
pg_cursor = pg_connection.cursor()

def create_characters_table(pg_connection, pg_cursor):
    create_query = """
    CREATE TABLE IF NOT EXISTS characters (
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        level INT,
        exp INT,
        hp INT,
        strength INT,
        intelligence INT,
        dexterity INT,
        wisdom INT
    )
    """
    print(create_query)
    pg_cursor.execute(create_query)
    pg_connection.commit()

def insert_characters(pg_connection, pg_cursor, characters):
    insertion_query = "INSERT INTO characters (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES %s"
    #records = df.to_dict("records") #> [{0: 'A rowwwww', 1: 'null'}, {0: 'Another row, with JSONNNNN', 1: '{"a": 1, "b": ["dog", "cat", 42], "c": "true"}'}, {0: 'Third row', 1: '3'}, {0: 'Pandas Row', 1: 'YOOO!'}]
    #list_of_tuples = [(r[0], r[1]) for r in records]
    list_of_tuples = characters
    execute_values(pg_cursor, insertion_query, list_of_tuples)
    pg_connection.commit()

if __name__ == "__main__":

    #
    # EXTRACT
    #

    characters = sqlite_connection.execute("SELECT * FROM charactercreator_character;").fetchall()
    print(type(characters))
    print(characters)

    #
    # LOAD
    #

    create_characters_table(pg_connection, pg_cursor)

    insert_characters(pg_connection, pg_cursor, characters)
