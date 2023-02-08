


def unique_list(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

list= [1,2,3,4,5,6,7,7,5,5,5,1]
print(unique_list(list))