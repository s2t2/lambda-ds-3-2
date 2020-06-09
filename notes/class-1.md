
# Class 1

Preparation Announcement:

```
Hey @channel, we're going to begin this sprint with an introduction to relational databases and SQL. To prepare for class, please:

    1) Download this example sqlite database called "chinook" (https://www.sqlitetutorial.net/sqlite-sample-database/), which we'll use to practice SQL queries.

    2) Optionally download and install this FREE database management software called TablePlus (https://tableplus.com/) which will allow you to interface with the SQLite and PostgreSQL databases we'll be working with in this unit. FYI: TablePlus is my preferred / recommended tool these days, but you could always use alternative tools like DB Browser and/or PgAdmin instead, as referenced in the materials.

And as always, fork the official Lambda repo: https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases
```

Agenda:

  1. Single-table SQL
  2. Multi-table SQL
  3. Executing SQL from Python
 
Lambda Material:

  + https://learn.lambdaschool.com/ds/module/recmwiPQG5zueKFCG/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module1-introduction-to-sql
 
DBMS Tool:

  + https://tableplus.com/ (FREE)

Practice SQLite Database:

  + https://www.sqlitetutorial.net/sqlite-sample-database/
  + https://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf

## Part 0 - Preface

Database Concept Notes (FYI / BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/conceptual-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/physical-design.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/database-design/entity-relationship-diagramming.md

SQL Notes (FYI / BONUS):

  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/best-practices.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/sql-style-guide.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/single-table-sql.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/single-table-aggregate-sql.md
  + https://github.com/prof-rossetti/gwu-istm-4121-201509/blob/master/notes/data-analysis/multi-table-sql.md
 
Like an English sentence, each SQL query is comprised of one or more clauses. Here are all the clauses available for use in a SQL query, in the order they are to be used:

```
SELECT ...
FROM ...
JOIN ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
```

It is not necessary to use all clauses in a single query. The `JOIN` clause is the only one which can appear multiple times. 


## Part I - Single Table SQL

```sql
SELECT
    1 as first_col,
    2 as second_col,
    3,
    "hello" as my_message,
    2 * 10,
    6
```

```sql
-- who are our customers? (what are their names?)
SELECT
  CustomerId
  ,FirstName
  ,LastName
FROM customers
```

```sql
-- which customers are from the US?
SELECT
  CustomerId
  ,FirstName
  ,LastName
FROM customers
WHERE Country = "USA"
-- WHERE Country <> "USA"
```

```sql
-- which customers are from either the US or the UK?
SELECT
  CustomerId
  ,FirstName
  ,LastName
  ,Country
FROM customers
-- WHERE Country = "USA" or Country = "United Kingdom"
WHERE Country in ("USA", "United Kingdom")
```

```sql
-- example of ORDER BY
SELECT
  *
FROM customers
WHERE Country in ("USA", "United Kingdom")
ORDER BY Country ASC, State DESC -- ASC is the default
```

## Part I (cont'd) - Single Table SQL w/ Aggregations

```sql
-- how many customers do we have?
SELECT
  -- count(*) as customer_count -- counts number of rows
  -- count(CustomerId) as customer_count -- counts number of rows
  count(distinct CustomerId) as customer_count -- > counts actual unique values
FROM customers
```

```sql
-- how many customers are from the US?
SELECT 
  count(distinct CustomerId) 
FROM customers
WHERE Country = "USA"
```

Using a `GROUP BY` clause:

> NOTE: when using the GROUP BY clause, we specify our result set should have a "row per" all the attributes included in the GROUP BY clause.

> RULE OF THUMB: when using the GROUP BY clause, all selected attributes that are not included in the GROUP BY clause should be removed from the SELECT clause, or or aggregated in the SELECT clause

```sql
-- how many customers in each country?
SELECT
  Country
  ,count(distinct CustomerId) as customer_count -- > 59
FROM customers
GROUP BY Country
```

```sql
-- which 5 countries have the most customers?
SELECT
  Country
  ,count(distinct CustomerId) as customer_count -- > 59
FROM customers
GROUP BY Country
ORDER BY customer_count DESC
LIMIT 5
```

FYI: you can use the results of one query as a dataset to select from. This is known as a "subquery" approach:

```sql
-- on average, how many customers in each country?
SELECT avg(customer_count) --> 2.45
FROM (
    SELECT
      Country
      ,count(distinct CustomerId) as customer_count -- > 59
    FROM customers
    GROUP BY Country
) subq
```

## Part II - Multi-Table SQL


```sql
-- for each album, what is the name of the artist
-- 347 rows (row per album)
SELECT 
  albums.AlbumId
  ,albums.Title
  ,artists.Name
FROM albums
JOIN artists ON albums.ArtistId = artists.ArtistId 
```


![a venn diagram depicting the difference between inner and outer joins](https://www.ionos.com/digitalguide/fileadmin/DigitalGuide/Screenshots_2018/Outer-Join.jpg)

Taking an iterative approach to illustrate the difference between inner and outer (i.e. left) joins.

```sql
-- for each artist,
-- how many albums?
-- and how many tracks?
-- row per artist (275)
-- row per artist (204???)
SELECT
  artists.ArtistId
  ,artists.Name as ArtistName
  ,count(distinct albums.AlbumId) as AlbumCount
  ,count(distinct tracks.TrackId) as TrackCount
FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON tracks.AlbumId = albums.AlbumId
GROUP BY artists.ArtistId
```

Why are we losing some artists? Because not all artists have albums. Maintain original table by using an outer join:

```sql
-- for each artist,
-- how many albums?
-- and how many tracks?
-- row per artist (275)
SELECT
  artists.ArtistId
  ,artists.Name as ArtistName
  ,albums.AlbumId
  ,tracks.TrackId
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
LEFT JOIN tracks ON tracks.AlbumId = albums.AlbumId
```

```sql
-- for each artist,
-- how many albums?
-- and how many tracks?
-- row per artist (275)
SELECT
  artists.ArtistId
  ,artists.Name as ArtistName
  ,count(distinct albums.AlbumId) as AlbumCount
  ,count(distinct tracks.TrackId) as TrackCount
FROM artists
LEFT JOIN albums ON artists.ArtistId = albums.ArtistId
LEFT JOIN tracks ON tracks.AlbumId = albums.AlbumId
GROUP BY artists.ArtistId
```


## Part III - Executing SQL from Python

SQLite:

  + https://docs.python.org/3/library/sqlite3.html
  + https://kite.com/python/examples/3884/sqlite3-use-a-row-factory-to-access-values-by-column-name

Executing an SQL query:

```py
import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM customers;"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)
```

Iterating through all records in our results set:

```py
import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

#query = "SELECT * FROM customers;"
query = """
SELECT
  Country
  ,count(distinct CustomerId) as CustomerCount -- > 59
FROM customers
GROUP BY Country
ORDER BY CustomerCount DESC
LIMIT 5
"""

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    print(type(row))
    print(row)
    print(row[0])
    print(row[1])
    print("-----")
```

Reference also ["app/chinook_queries.py"](/app/chinook_queries.py).
