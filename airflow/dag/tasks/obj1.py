# Importing necessary libraries
import psycopg2
import pandas as pd
import os
import sys

# Getting the date from the command line argument
date = input("Enter the date in YYYY-MM-DD format: ")

# Setting up PostgreSQL connection details
host = "localhost"
database = "northwind"
user = "northwind_user"
password = "thewindisblowing"

# Establishing connection to the database
try:
    db_conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    print("Successfully connected to the database!")
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
    sys.exit(1)

# Getting table names from the database
def get_table_names(db_conn):
    table_names = []
    try:
        with db_conn.cursor() as db_cursor:
            db_cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
            for name in db_cursor.fetchall():
                table_names.append(name[0])
    except psycopg2.Error as e:
        print("Error getting table names:", e)
    return table_names

# Exporting table data to CSV files
def csv_export(db_conn, table_name, date):
    try:
        with db_conn.cursor() as db_cursor:
            select = "SELECT * FROM {}".format(table_name)
            SQL_for_file_output = "COPY ({}) TO STDOUT WITH CSV HEADER".format(select)
            path_file = "/data/postgres/{}/data_{}.csv".format(table_name, date)
            os.makedirs(os.path.dirname(path_file), exist_ok=True)
            with open(path_file, 'w') as f_output:
                db_cursor.copy_expert(SQL_for_file_output, f_output)
            print("Data from table '{}' successfully exported to '{}'!".format(table_name, path_file))
    except psycopg2.Error as e:
        print("Error exporting data from table '{}':".format(table_name), e)

# Getting and exporting data from all tables
table_names = get_table_names(db_conn)
for table_name in table_names:
    csv_export(db_conn, table_name, date)

# Closing the database connection
db_conn.close()
