


# Define a dictionary using curly braces
person = {"name": "John Doe", "age": 32, "city": "New York"}
print(person)

# Define a dictionary using the dict function
person = dict(name="Jane Doe", age=29, city="London")
print(person)


"""
    Ordered 
    Changeable
    Duplicates Not Allowed
    """
    
print(len(person)) 
print(type(person))

# how to access element

x = person.get("New York")

print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

  #we change the value in the dict

thisdict ["year"]= 1233

print(thisdict)

thisdict.update({"color": "red"})
print(thisdict)

thisdict.pop("model")
print(thisdict)

mydict = thisdict.copy()

print(mydict)
