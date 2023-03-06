filename = input("Enter file name: ") # specify the file name

# open the file in read mode
with open(filename, "r") as file:
    # initialize a counter for the number of lines
    num_lines = 0
    # loop through the file and count the number of lines
    for line in file:
        num_lines += 1

print("Number of lines:", num_lines)
