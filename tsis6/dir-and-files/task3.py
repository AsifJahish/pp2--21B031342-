

import os

path = input("Enter path: ") # specify the path


if os.path.exists(path):
    print("Path exists.")

  
    dirname, filename = os.path.split(path)
    print("Directory:", dirname)
    if filename:
        print("Filename:", filename)
    else:
        print("There is no filename for this path.")

else:
    print("Path does not exist.")

