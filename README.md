# PostgreSQL-Database-Connection-and-Operations-with-Python
This repository contains a Python script demonstrating how to connect to a PostgreSQL database using the Psycopg2 module. The script performs various database transactions, including creating a table, inserting data, updating records, and fetching data from the table.

Prerequisites

    Install the psycopg2 module using:
    pip install psycopg2

Usage

    Update the database connection parameters (hostname, database, username, password, port) in the script according to your PostgreSQL setup.

    Run the script using:
    python postgres_operations.py

PostgreSQL Database Connection and Operations with Python

This repository contains a Python script demonstrating how to connect to a PostgreSQL database using the Psycopg2 module. The script performs various database transactions, including creating a table, inserting data, updating records, and fetching data from the table.
Prerequisites

    Install the psycopg2 module using:

    bash
    Copy code
    pip install psycopg2

Usage

    Update the database connection parameters (hostname, database, username, password, port) in the script according to your PostgreSQL setup.

    Run the script using:

    bash
    Copy code
    python postgres_operations.py

    

Script Overview

    The script connects to the PostgreSQL database and creates a table named "employee" with columns (id, name, salary, dept_id).

    Inserts sample data into the "employee" table.

    Updates the salary of all employees with a 50% increase.

    Fetches and prints all records from the "employee" table.

    The script also demonstrates the use of a context manager (WITH clause) to handle database connection and cursor operations, emphasizing its advantages.

Note

    Commented sections in the script, such as deleting records, are provided for reference and can be uncommented as needed.

Feel free to customize and integrate this script into your projects. If you encounter any issues or have suggestions, please let me know!
