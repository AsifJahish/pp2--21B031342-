# Define a set using curly braces
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Define a set using the set function
vegetables = set(["carrot", "potato", "celery"])
print(vegetables)

"""
Unchangeable
Unordered


Duplicates Not Allowed

"""

for i in fruits:
    print(i, end=" ")

print("/n")

print("apple" in fruits)

fruits.add("mango")
print(fruits)


print(type(fruits))


fruits.update(vegetables)
print(fruits)

