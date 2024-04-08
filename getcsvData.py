import mysql.connector
import csv
import os

# Define your MySQL database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'osme1'
}

# Establish a connection to the MySQL server
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor(dictionary=True)

# Get a list of tables in the database
cursor.execute("SHOW TABLES")
tables = [table['Tables_in_osme1'] for table in cursor.fetchall()]

# Create a CSV file to store the relationships and counts
csv_file_path = '/home/harish/Documents/connection/relationship_analysis_with_counts.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Parent Database', 'Parent Table', 'Child Database', 'Child Table', 'Relationship Type', 'Parent Count', 'Child Count'])

    # Iterate through each table
    for table in tables:
        # Get foreign key information for the table
        cursor.execute(f"SHOW CREATE TABLE {table}")
        create_table_query = cursor.fetchone()['Create Table']

        # Extract foreign key constraints from the CREATE TABLE query
        foreign_keys = [line.strip() for line in create_table_query.split('\n') if 'FOREIGN KEY' in line]

        # Iterate through each foreign key constraint
        for foreign_key in foreign_keys:
            # Extract parent and child table information
            parent_table = foreign_key.split('REFERENCES')[0].split('`')[1]
            child_table = foreign_key.split('REFERENCES')[1].split('`')[1]

            # Get counts of records in the parent and child tables
            cursor.execute(f"SELECT COUNT(*) AS count FROM {table}")
            parent_count = cursor.fetchone()['count']

            cursor.execute(f"SELECT COUNT(*) AS count FROM {child_table}")
            child_count = cursor.fetchone()['count']

            # Determine relationship type
            relationship_type = 'One-to-One' if parent_count == child_count == 1 else 'One-to-Many'

            # Write the relationship and counts to the CSV file
            csv_writer.writerow([db_config['database'], table, db_config['database'], parent_table, relationship_type, parent_count, child_count])
            csv_writer.writerow([db_config['database'], parent_table, db_config['database'], child_table, relationship_type, parent_count, child_count])

# Close the database connection
cursor.close()
connection.close()

print(f"Relationship analysis with counts saved to {csv_file_path}")
