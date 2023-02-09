




def multiply_values(tuples):
    result = []
    for t in tuples:
        result.append(t[0] * t[1])
    return result

tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(multiply_values(tuples))


