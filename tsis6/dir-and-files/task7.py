

filename = input("Enter first file name: ")
with open(filename, 'r') as input_file:

    # Read the contents of the input file
    file_contents = input_file.read()

# Open the output file in write mode
filename1 = input("Enter first file name: ")
with open(filename1, 'w') as output_file:

    # Write the contents of the input file to the output file
    output_file.write(file_contents)
