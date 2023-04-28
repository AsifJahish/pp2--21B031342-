import psycopg2
import csv

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="postgres"
)




cur = conn.cursor()

with open('/home/asifjahish/vscode/pp2--21B031342-/Tsis10/PhoneBook/phoneBook - Sheet1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute(
            "INSERT INTO Phonebook(first_name, last_name, address,phone_number) VALUES (%s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3])
        )

conn.commit()

cur.close()
conn.close()