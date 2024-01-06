import os
import shutil
import sys

def move_files(base_path):
    # Define the subdirectory and filename to look for
    sub_dir = 'pts_bbox'
    file_name = 'results_nusc.json'

    # Iterate through each directory in the base path
    for dir_name in os.listdir(base_path):
        dir_path = os.path.join(base_path, dir_name)

        # Check if it is a directory
        if os.path.isdir(dir_path):
            file_path = os.path.join(dir_path, sub_dir, file_name)

            # Check if the file exists
            if os.path.exists(file_path):
                # Move the file
                shutil.move(file_path, dir_path)
                print(f"Moved {file_path} to {dir_path}")

                # Optionally, remove the now empty subdirectory
                os.rmdir(os.path.join(dir_path, sub_dir))
                print(f"Removed empty directory {os.path.join(dir_path, sub_dir)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_base_folder>")
    else:
        move_files(sys.argv[1])