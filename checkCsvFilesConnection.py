import os
import pandas as pd
from itertools import combinations

def identify_foreign_keys(file_list):
    foreign_keys = {}

    # Iterate through all pairs of files
    for file1, file2 in combinations(file_list, 2):
        df1, df2 = pd.read_csv(file1), pd.read_csv(file2)

        # Iterate through columns to find potential foreign keys
        for col in df1.columns:
            if col in df2.columns:
                if df1[col].nunique() == len(df1) and df2[col].nunique() == len(df2):
                    common_values = set(df1[col]) & set(df2[col])

                    if common_values:
                        foreign_keys[(file1, file2, col)] = list(common_values)

    return foreign_keys

def create_connection_file(foreign_keys, output_file):
    connection_df = pd.DataFrame(list(foreign_keys.keys()), columns=['File1', 'File2', 'ForeignKey'])
    connection_df['CommonValues'] = [', '.join(map(str, values)) for values in foreign_keys.values()]

    connection_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path to the folder containing your CSV files
    folder_path = '/home/harish/Documents/osme'
    
    # Get a list of all CSV files in the folder
    file_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]

    if not file_list:
        print("No CSV files found in the specified folder.")
    else:
        # Identify foreign keys
        foreign_keys = identify_foreign_keys(file_list)

        if foreign_keys:
            # Create a connection file
            create_connection_file(foreign_keys, '/home/harish/Documents/connection/connection_file.csv')
            print("Connection file created successfully.")
        else:
            print("No relationships found.")
