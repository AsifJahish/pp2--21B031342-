

#  Write a Python function that
#  takes a list and returns a new list with unique 
# elements of the first list. Note: don't use collection set.


def unique_list(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

list= [1,2,3,4,5,6,7,7,5,5,5,1]
print(unique_list(list))