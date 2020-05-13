
## Class 3

> To prepare for class, please sign up for a MongoDB Atlas account https://account.mongodb.com/

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/rec3JRFsRH2yeALwS/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/tree/master/module3-nosql-and-document-oriented-databases

## Part I

Recap of previous assignment (inserting "titanic.csv" file data into a PostgreSQL database).

## Part II and III

MongoDB Docs:

  + https://api.mongodb.com/python/current/tutorial.html
  + https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
  + https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
  + https://api.mongodb.com/python/current/tutorial.html#range-queries
  + https://docs.mongodb.com/manual/reference/operator/query/

Vocabulary comparison:

![](https://www.includehelp.com/mongodb/Images/mongodb-structure.jpg)

Configuring Mongo Atlas:

  + IP Address to allow connections from anywhere: `0.0.0.0/0`

Installing packages:

```sh
# for pipenv users:
pipenv install pymongo dnspython

# for conda users:
pip install pymongo dnspython
```

```py

# app/mongo_queries.py

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})
print("DOCS:", collection.count_documents({}))
print(collection.count_documents({"name": "Pikachu"}))
```

> FYI: if you see "pymongo.errors.ServerSelectionTimeoutError [SSL: CERTIFICATE_VERIFY_FAILED]", and you have already allowed  access from all IP addresses, and you have already installed the `dnspython` package, try adding `&ssl=true&ssl_cert_reqs=CERT_NONE` to the end of the connection string (thanks to Aaron from DS 14)!


Reference also ["app/mongo_prep.py"](/app/mongo_prep.py).
