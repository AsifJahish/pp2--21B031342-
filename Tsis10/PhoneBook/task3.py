# Implement updating data in the table (change user first name or phone)


import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="postgres"
)

# Open a cursor to perform database operations
cursor = conn.cursor()


# Define the update statement
update_statement = "UPDATE Phonebook SET first_name = %s WHERE address = %s"

# Define the values to be updated
update_values = ("teacherpp2", "23")

# Execute the update statement with the values
cur.execute(update_statement, update_values)

# Commit the changes
conn.commit()


# Close the cursor and database connection
cursor.close()
conn.close()
