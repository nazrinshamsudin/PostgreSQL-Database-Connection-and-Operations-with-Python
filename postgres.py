import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': '127.0.0.1',
    'port': '5432'
}

# Establish a connection to the database
try:
    connection = psycopg2.connect(**db_params)
    print("Connected to the database!")

    # Create a cursor object for executing SQL statements
    cursor = connection.cursor()

    # Execute a simple query
    cursor.execute("SELECT version();")

    # Fetch the result
    result = cursor.fetchone()
    print("PostgreSQL version:", result)

except Exception as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")
