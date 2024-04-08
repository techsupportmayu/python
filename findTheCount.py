import os

def count_files_in_folder(folder_path):
    try:
        # Get the list of files in the specified folder
        files = os.listdir(folder_path)

        # Count the number of files
        file_count = len(files)

        print(f'The number of files in the folder "{folder_path}" is: {file_count}')

    except FileNotFoundError:
        print(f'Error: The specified folder "{folder_path}" was not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

# Replace 'your_folder_path' with the actual path of the folder you want to count files in
folder_path = '/home/harish/Downloads/images-20231226T062724Z-001/images'
count_files_in_folder(folder_path)
