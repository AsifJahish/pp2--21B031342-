

#You are given list of numbers separated by spaces. Write a
#function filter_prime which will
# take list of numbers as an agrument and returns only prime numbers from the list.


def filter_prime(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    return [number for number in numbers if is_prime(number)]

numbers= [1,2,3,4,5,6,7,8,9,10,11,12]
print(filter_prime(numbers))