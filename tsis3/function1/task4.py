

#You are given list of numbers separated by spaces. Write a
#function filter_prime which will
# take list of numbers as an agrument and returns only prime numbers from the list.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(filter_prime(numbers))