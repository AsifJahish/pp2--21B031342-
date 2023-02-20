

import math

n = int(input("Enter the number of sides  "))
length = float(input("Enter the length of side "))

# Calculate the apothem
apothem = 0.5 * length / math.tan(math.pi / n)

# Calculate the area
area = 0.5 * n * length * apothem

print(f"The area of the polygon is {area} ")
