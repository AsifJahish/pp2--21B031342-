import psycopg2


    # Establish a connection to the database
conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres")



cur = conn.cursor()

    # Execute an INSERT statement to add a new employee to the employees table


cur.execute("SELECT d.doctor_name, h.name, d.joining_date, d.salary FROM Doctor d JOIN hospital h ON d.hospital_Id = h.Id;")

rows = cur.fetchall()

    # Process the retrieved data
for row in rows:
        # Process each row
        print(row)


    # Commit the transaction
conn.commit()

    # Close the cursor and database connection
cur.close()
conn.close()
