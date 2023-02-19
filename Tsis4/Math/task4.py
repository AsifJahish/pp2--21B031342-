


# Write a Python program to calculate the area of a parallelogram.


def area_P(a ,h):
    return a*h

a=int(input("Length of base: "))
h= int(input("Height of parallelogram: "))

print(f"Expected Output: {float(area_P(a,h))}")