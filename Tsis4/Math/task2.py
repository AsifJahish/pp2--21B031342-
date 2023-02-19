

import math
def area(h,b,c):

    a= ((b+c)/2)*h
    return a

height= int(input("Height:   "))

base1= int(input("first value:  "))
base2= int(input("Second value: "))
result= area(height,base1, base2)
print(f"expected Area is :{result}")