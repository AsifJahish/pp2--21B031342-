

"""
A tuple in Python is an immutable, ordered collection of elements of any type.

It is defined using parentheses () and elements are separated by commas ,.    
    
    
    Allow Duplicates
    
    Unchangeable
    
    Ordered
    
    """
# define a tuple
person = ("John", 32, "Engineer")

# access tuple elements
name = person[0]
age = person[1]
occupation = person[2]

print("Name:", name)
print("Age:", age)
print("Occupation:", occupation)

print(person)
# -1 refers to the last item, -2 refers to the second last item etc.
print(person[-1])

#When specifying a range, the return value will be a new tuple with the specified items.

print(person[0:2])


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


my = ("apple", "banana", "cherry")
you = list(thistuple)
you.remove("apple")
thistuple = tuple(you)