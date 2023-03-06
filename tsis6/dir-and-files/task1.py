
import os

path = input("Enter path: ") # specify the path

# list only directories
print("\nDirectories:")
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        print(item)

# list only files
print("\nFiles:")
for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(item)

# list all directories and files
print("\nAll Directories and Files:")
for item in os.listdir(path):
    print(item)