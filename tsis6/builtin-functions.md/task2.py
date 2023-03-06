

def upperCount(st):
    upper=0
    lower=0
    for i in range(len(st)):
     if st[i].isupper():
        upper += 1
     elif st[i].islower():
        lower +=1
    return upper, lower

st= str(input("enter a string  "))
print(upperCount(st))