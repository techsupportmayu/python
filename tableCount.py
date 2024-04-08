import mysql.connector
import csv

# Define your MySQL database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'osme1'
}

# Connect to the MySQL server
connection = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Get the list of tables in the database
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Create a CSV file to store the results
csv_filename = '/home/harish/Documents/tablesCount/table_data_status.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Table', 'Row Count'])

    # Iterate through each table and check the row count
    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]

        # Write the table name and row count to the CSV file
        csv_writer.writerow([table_name, row_count])

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Table data status (including row count) has been saved to '{csv_filename}'.")
