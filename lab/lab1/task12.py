


def process_pairs(n, pairs):
    array = []
    for i in range(n):
        key, value = pairs[i]
        if type(key) == str:
            array.append(value)
        elif type(key) == bool:
            if value:
                array.sort()
            else:
                array.sort(reverse=True)
        elif type(key) == int:
            if key >= 0 and key < len(array):
                array = array[key:]
        elif type(key) == set:
            array.append(value)
            array = list(set(array))
        else:
            array = [key] + array + [value]
    return array

pairs = [(str, 'value1'), (bool, False), (int, 2), (set, 'value4'), (1, 'value5')]
n = len(pairs)
result = process_pairs(n, pairs)
print(result)
