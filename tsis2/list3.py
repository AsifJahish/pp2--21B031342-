
"""
how to sort list in python and how to reverse it     
    
    
    """


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] 
thislist.sort()  # in ascending, by default
print(thislist)

mylist = [100, 50, 65, 82, 23]
mylist.sort() # in ascending, by default
print(mylist)


thislist.sort(reverse=True)  # To sort descending, use the keyword argument reverse = True

print(thislist)

mylist.sort(reverse=True) # To sort descending, use the keyword argument reverse = True

print(mylist)



"""
Customize Sort Function
You can also customize your own function by using the keyword argument key = function.    
    
    """
    
    
def my_function(n):
    return abs(n-80)

mylist.sort(key=my_function)

print(mylist)


thislist.reverse()

print(thislist)

# how to copy list

new_list= thislist.copy()

print(new_list)


new= thislist+ new_list

print(new);

thislist.extend(mylist);
print(thislist)

for x in mylist:
    thislist.append(x)
print(thislist)