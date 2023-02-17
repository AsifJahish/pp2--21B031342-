


#Write a function that computes the volume of a sphere given its radius.
import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

radius= int(input("enter the radius of the shpere   "))

print(sphere_volume(radius))