

def divisible_by_3():
    result = []
    for i in range(1, 101):
        if i % 3 == 0:
            result.append(i)
    return result

print(divisible_by_3())
