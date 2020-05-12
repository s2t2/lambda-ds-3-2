
## Class 2

> To prepare for class, please sign up for an Elephant SQL account https://www.elephantsql.com/

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/recSdx6IFkDxqgxGb/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module2-sql-for-analysis

### Part I

Topic: "RPG" database SQL assignment review and solutions.

### Part II

Topic: Insert statements in SQL.

Database Management SQL (FYI / BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-management/database-management-sql.md
  + https://stackoverflow.com/questions/28558920/postgresql-foreign-key-syntax/28560619

### Part III

Topic: Connecting to and Querying PostgreSQL databases in Python

PostgreSQL & Psycopg Docs:
  + https://www.psycopg.org/docs/
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/psycopg.md
  + https://www.postgresql.org/docs/9.5/datatype.html
  + https://www.psycopg.org/docs/usage.html
  + https://www.psycopg.org/docs/cursor.html#cursor
  + https://www.psycopg.org/docs/cursor.html#fetch
  + https://www.psycopg.org/docs/extras.html
  + https://www.psycopg.org/docs/extras.html#dictionary-like-cursor

Environment Variables:
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/environment-variables.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/os.md#environment-variables
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/dotenv.md

Installing package dependencies:

```sh
# for Pipenv users:
pipenv install python-dotenv psycopg2-binary # NOTE: the "-binary"

# for conda users:
pip install pandas python-dotenv psycopg2
```

```py
# app/elephant_queries.py

import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)
```

Head's up: you can use this configuration to refer to the rows as dictionaries (like the Row Factory approach from SQLite):

```py
# ...
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
# ...
```
See also ["app/elephant_multi.py"](/app/elephant_multi.py) for guidance about a few approaches we can take to insert data from a Python script.
