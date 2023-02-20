

import math

def degree_radian(n):

    a = (n* math.pi)/180

    return a

degree = float(input("enter the degree you want   "))

print(degree_radian(degree))