"""
Task 5) OS File Manager
   - Ask user for a directory path.
   - Automatically:
        - Create a folder "backup" inside it if not exists.
        - Copy all .txt files into "backup".
        - Print summary: how many files copied.
   - If directory invalid, retry until correct.

"""

import os

def manager():

    while True:
        dir_path = input("Enter a directory path: ")
        if not os.path.isdir(dir_path):
            print("Invalid directory, try again.")
            continue

        backup_path = os.path.join(dir_path, "backup")
        os.makedirs(backup_path, exist_ok=True)

        txt_files = [file for file in os.listdir(dir_path) if file.endswith('.txt')]
        for file_name in txt_files:
            src_file = os.path.join(dir_path, file_name)
            dest_file = os.path.join(backup_path, file_name)
            try:
                with open(src_file, 'rb') as src:
                    with open(dest_file, 'wb') as dest:
                        dest.write(src.read())
            except Exception as e:
                print(f"Failed to copy {file_name}: {e}")
        print(f"Copied {len(txt_files)} .txt files to 'backup' folder.")
        break
