import os
import mysql.connector
import csv
import re
import chardet

def find_tables_in_file(file_path, tables):
    try:
        with open(file_path, 'rb') as file:
            result = chardet.detect(file.read())
            encoding = result['encoding']

        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()
            used_tables = [table for table in tables if re.search(fr'\b{table}\b', content, re.IGNORECASE)]
            return used_tables
    except UnicodeDecodeError:
        print(f"Unable to decode file: {file_path}")
        return []

def search_php_files_for_tables(root_folder, tables):
    table_usage_data = []

    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.php'):
                file_path = os.path.join(foldername, filename)
                used_tables = find_tables_in_file(file_path, tables)
                if used_tables:
                    table_usage_data.append({
                        "File": file_path,
                        "Used Tables": used_tables
                    })

    return table_usage_data

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="osme1"
)

myCursor = mydb.cursor()

myCursor.execute("SHOW TABLES")
tables = [table[0] for table in myCursor]

# Specify the root folder where you want to search for table usage
root_folder_path = "/home/harish/Downloads/sothys-21-11-2023"

table_usage_data = search_php_files_for_tables(root_folder_path, tables)

# Specify the path where you want to save the CSV file
csv_file_path = "/home/harish/Downloads/csv_names/table_usage_data.csv"

with open(csv_file_path, mode='w', newline='') as csvfile:
    fieldnames = ["File", "Used Tables"]
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    csv_writer.writeheader()

    # Write the table usage data
    csv_writer.writerows(table_usage_data)

print(f"Table usage data has been written to {csv_file_path}")
