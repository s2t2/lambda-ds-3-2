
# shared by Aaron from DS 14
# https://lambda-students.slack.com/archives/GT7MZ0TKK/p1589389551424400

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PW,
    host=DB_HOST)
cur = conn.cursor()

# Review shape of titanic.csv in terminal
# to determine schema
# 8 columns:
"""
Survived INT
Pclass INT
Name VARCHAR(40) NOT NULL
Sex ENUM
Age INT
Siblings/Spouses Aboard INT
Parents/Children Aboard INT
Fare NUMERIC
"""

# Create titanic table
# cur.execute(
#     """
#     --CREATE TYPE sex AS ENUM ('male', 'female');
#     CREATE TABLE titanic (
#         Survived INTEGER NOT NULL,
#         Pclass INTEGER NOT NULL,
#         Name TEXT NOT NULL,
#         Sex sex,
#         Age NUMERIC NOT NULL,
#         "Siblings/Spouses Aboard" INTEGER NOT NULL,
#         "Parents/Children Aboard" INTEGER NOT NULL,
#         Fare NUMERIC NOT NULL
#     );
#     """
# )
# conn.commit()

### Insert titanic data
### https://www.dataquest.io/blog/loading-data-into-postgres/

with open('module2-sql-for-analysis/titanic.csv', 'r') as f:
    next(f)  # Skip header row
    cur.copy_from(f, 'titanic', sep=',')
 
conn.commit()

