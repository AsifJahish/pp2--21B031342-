set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


"""


You can use the union() method that returns
a new set containing all items from both sets, 

or the update() method that inserts all the items from one set into another:
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

z= x.intersection(y)
print(z)
