# DS Unit 3 Sprint 2

```sh
cd ds-3-2-inclass
```

```sh
pipenv install
```



<hr>

## Class 1

    Hey everyone, excited to dive into SQL with you tonight! To prepare for class, I recommend you download this database management software called TablePlus, which will allow you to interface with the Sqlite and PostgreSQL databases we'll be working with in this unit. https://tableplus.com/ (this would take the place of DB Browser and PGAdmin, which you'll see references to in the material)

    Also download this example sqlite database called "chinook" https://www.sqlitetutorial.net/sqlite-sample-database/ which we will use to practice SQL queries

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/recmwiPQG5zueKFCG/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module1-introduction-to-sql

DBMS Tool:

  + https://tableplus.com/

SQLite:

  + https://docs.python.org/3/library/sqlite3.html
  + https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name

Practice Database:

  + https://www.sqlitetutorial.net/sqlite-sample-database/
  + https://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf

Database Concept Notes (BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/conceptual-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/physical-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/entity-relationship-diagramming.md


SQL Notes (BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/best-practices.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/sql-style-guide.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/single-table-sql.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/single-table-aggregate-sql.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/multi-table-sql.md

## Class 2

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/recSdx6IFkDxqgxGb/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module2-sql-for-analysis

PostgreSQL & Psycopg Docs:

  + https://www.psycopg.org/docs/
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/psycopg.md
  + https://www.postgresql.org/docs/9.5/datatype.html

Environment Variables:
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/environment-variables.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/os.md#environment-variables
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/dotenv.md

(BONUS) Database Management SQL:

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-management/database-management-sql.md


```sh
#pipenv install psycopg2 #> leads to issues? (need to use -binary)
pipenv install psycopg2-binary #> leads to issues?
```

or start over with conda env:

```sh
conda create -n db-env python=3.7
conda activate db-env
#pip install psycopg2 python-dotenv
pip install -r requirements.txt
```

## Class 3

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/rec3JRFsRH2yeALwS/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module3-nosql-and-document-oriented-databases

MongoDB Docs:

  + https://api.mongodb.com/python/current/tutorial.html
  + https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
  + https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
  + https://api.mongodb.com/python/current/tutorial.html#range-queries
  + https://docs.mongodb.com/manual/reference/operator/query/


```sh
pip install pymongo dnspython python-dotenv
```

```sh
python app/mongo_prep.py
```


## Class 4

Lambda Material:

  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module4-acid-and-database-scalability-tradeoffs
  + https://learn.lambdaschool.com/ds/module/rec9c9nW20Sn6TBAO/
  + [Sprint Challenge](https://github.com/LambdaSchool/DS-Material/blob/master/unit3-data-engineering/sprint2-sql-and-databases/sprint-challenge/challenge.md)

Normalization:

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/logical-design.md
  + [Database Relations Exercise](https://docs.google.com/spreadsheets/d/1xZ98yXEieMtaWuVQh3lQjCuP5aIqhinQcnzbnux52tY/edit?usp=sharing)

SQL Review:

  + https://www.w3schools.com/sql/sql_exercises.asp
