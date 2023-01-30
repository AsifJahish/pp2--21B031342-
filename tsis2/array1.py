"""
what is the different between array and list    
    
    
    
    
    Array can only store elements of the same data type, 
    while a list can store elements of different data types.
Arrays are more efficient in terms of memory usage and performance,
as they are fixed-size, while lists are dynamic in size.
The array module is not a built-in module and must be imported, 
while lists are a built-in data type.
Array uses square brackets "[]" for indexing and slicing, while lists use the same syntax.
    
    """
    
import array

# Creating an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Printing the array
print("The array is: ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")

# Adding a new element to the array
arr.append(6)

# Printing the updated array
print("\nThe updated array is: ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")
    
print("\n")

arr.pop();

print(arr)