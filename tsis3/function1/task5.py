
# to print all the permutation of a string




import itertools

def permutations(string):
    return list("".join(p) for p in itertools.permutations(string))

s= str(input("enter the string you want     "))
print(permutations(s))
