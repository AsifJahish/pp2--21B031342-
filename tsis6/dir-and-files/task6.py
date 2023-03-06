

import string

# Generate file names A.txt, B.txt, and so on up to Z.txt
file_names = [letter + '.txt' for letter in string.ascii_uppercase]

# Create the text files
for file_name in file_names:
    with open(file_name, 'w') as f:
        f.write('This is the {} file.'.format(file_name))
