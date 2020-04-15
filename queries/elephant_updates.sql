
DROP TABLE IF EXISTS my_table;

CREATE TABLE my_table as (
    SELECT * FROM test_table -- don't have permissions to change
);

-- goal: update the name value of the record w/ id=12
-- h/t: https://www.tutorialspoint.com/postgresql/postgresql_update_query.htm
UPDATE my_table
SET name = 'newer name'
WHERE id = 1;

SELECT *
FROM my_table;
