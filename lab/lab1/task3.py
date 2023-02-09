


N = int(input("Enter a number: "))

squares = []
i = 1
while i * i <= N:
    squares.append(i * i)
    i += 1

print(squares)
