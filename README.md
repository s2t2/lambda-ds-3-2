# DS Unit 3 Sprint 2

```sh
cd ds-3-2-inclass
```

```sh
pipenv install
```



<hr>

## Class 1

Reference Links:

  + https://learn.lambdaschool.com/ds/module/recmwiPQG5zueKFCG/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module1-introduction-to-sql
  + https://docs.python.org/3/library/sqlite3.html
  + https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name
  + https://tableplus.com/
  + https://www.sqlitetutorial.net/sqlite-sample-database/
  + https://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf

Database Concept Notes (BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/conceptual-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/logical-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/physical-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/entity-relationship-diagramming.md


SQL Notes (BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/best-practices.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/sql-style-guide.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/single-table-sql.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/single-table-aggregate-sql.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/multi-table-sql.md

## Class 2

  + https://learn.lambdaschool.com/ds/module/recSdx6IFkDxqgxGb/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module2-sql-for-analysis
  + https://www.psycopg.org/docs/
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/psycopg.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-management/database-management-sql.md


  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/environment-variables.md
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/os.md#environment-variables
  + https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/dotenv.md


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

Reference Links:

  + https://learn.lambdaschool.com/ds/module/rec3JRFsRH2yeALwS/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module3-nosql-and-document-oriented-databases
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
