


import re
my_string = input('enter a string ')
p = re.compile('[A-Z]+[a-z]+')
m = p.search(my_string)
if m:
    print('it\'s a match')
    print(m.group())
else:
    print('no match ')