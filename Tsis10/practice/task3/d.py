import psycopg2
import csv


    # Establish a connection to the database
conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres")


cur = conn.cursor()

# Create a procedure to insert joined table data into a CSV file
def export_data_to_csv(file_path):
    # Join the tables and retrieve data
    cur.execute("SELECT d.doctor_name, h.name, d.joining_date, d.speciality, d.salary, d.experience FROM Doctor d JOIN Hospital h ON d.hospital_id = h.Id")
    rows = cur.fetchall()

    # Export data to CSV file
    with open('/home/asifjahish/vscode/pp2--21B031342-/Tsis10/practice/task3/sheet2.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['doctor-name', 'name', 'joining_date', 'speciality', 'salary', 'experience'])
        writer.writerows(rows)

    print("Data exported to CSV file successfully.")

# Call the procedure and specify the file path
export_data_to_csv("output.csv")

# Close the cursor and database connection
cur.close()
conn.close()