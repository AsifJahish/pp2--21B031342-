

import math

n = int(input("Enter the number of sides of the regular polygon: "))
length = float(input("Enter the length of each side of the regular polygon: "))

# Calculate the apothem
apothem = 0.5 * length / math.tan(math.pi / n)

# Calculate the area
area = 0.5 * n * length * apothem

print(f"The area of the regular polygon is {area:.2f} square units.")
