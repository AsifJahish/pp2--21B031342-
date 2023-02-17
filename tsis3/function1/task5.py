from itertools import permutations


#Write a function that accepts string from user and print all permutations of that string.



def all_permutations(string):
    return [''.join(p) for p in permutations(string)]

string = "abc"
print(all_permutations(string))
