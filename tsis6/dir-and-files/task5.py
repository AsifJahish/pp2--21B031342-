

filename = input("Enter file name: ")
my_list = ["I Love ", "to program", "In python", "Language"] 

# open the file in write mode
with open(filename, "w") as file:
    # loop through the list and write each item to a new line in the file
    for item in my_list:
        file.write(item + "\n")

print("List written to", filename)
