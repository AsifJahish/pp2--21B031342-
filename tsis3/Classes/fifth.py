

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(lambda x: (i for i in range()), numbers))

print("Prime numbers in the list:", prime_numbers)
