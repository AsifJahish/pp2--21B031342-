def squares(a, b):
    for i in range(a, b+1):
        yield i**2


a = int(input("enter first number     "))

b = int(input("enter second number     "))

for square in squares(a, b):
    print(square)