import os

# Specify the file path to delete
file_path = "b.txt"

# Check if file exists
if os.path.exists(file_path):

    # Check if the file is accessible
    if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):

        # Delete the file
        os.remove(file_path)
        print("File deleted successfully.")

    else:
        print("You don't have the required permissions to delete the file.")

else:
    print("File not found.")
