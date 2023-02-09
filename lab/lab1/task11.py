def fizzbuzz(number):
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz, ", end='')
        elif i % 3 == 0:
            print("Fizz, ", end='')
        elif i % 5 == 0:
            print("Buzz, ", end='')
        else:
            print(f"{i:2}, ", end='')
        if i % 10 == 0:
            print("")
    print(".")

number = 100
fizzbuzz(number)
