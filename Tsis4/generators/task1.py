

def generate_squares(N):
    for i in range(N):
        yield i**2
# generate the squares of numbers up to 5
squares = generate_squares(5)

# print the squares
for square in squares:
    print(square)
