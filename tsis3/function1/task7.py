


#  Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(num):
    for i in range(len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True
    return False




print(has_33([1,3,3]))

print(has_33([1,2,3,4,5,6,7,8]))