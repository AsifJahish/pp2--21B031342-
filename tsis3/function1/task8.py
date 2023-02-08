

def has_007(num):
    for i in range(len(num)-2):
    # we have to do len(num)-2 becuase when we say that i+2 it would go 2 more then the list length
        if num[i]==0 and num[i+1]==0 and num[i+2]==7:
            return True

    return False


has= [1,2,3,0,0,7]
don=[1,2,3,4,0,0,5]

print(has_007(don))
print(has_007(has))
