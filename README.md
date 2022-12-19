### README


#### Task 1
I'm having problem trying to load test dataset into the database. However, from the table definition here: https://ohdsi.github.io/CommonDataModel/cdm54.html#Clinical_Data_Tables
I could create the tables and put in some sample rows of my own for testing and code development for task 2.

Here are the files: 
tables_creation_script.sql : For creating the tables
add_foreign_key.sql : For adding the defined constraints
add_primary_key.sql : For adding primary keys to the tables
create_users.sql : Task 1.1
query.sql : Task 1.2


#### Task 2
The main codes is in: Task2_PY_Package/EHRReader/ehrreader/reader.py 

Tests(pytest) is in: Task2_PY_Package/EHRReader/ehrreader/tests/

To test, use terminal to navigate to: Task2_PY_Package/EHRReader/ehrreader
and run: "pytest"

#### Task 3
Couldn't complete in 6 hours timeframe.


Assumptions:
Task 1 database using Postgres as DBMS.