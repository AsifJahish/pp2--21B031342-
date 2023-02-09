

def classify_elements(arr2):
    only_ints = []
    list_of_strings = []
    float_nums = []
    array_of_bools = []
    for element in arr2:
        if type(element) == int:
            only_ints.append(element)
        elif type(element) == str:
            list_of_strings.append(element)
        elif type(element) == float:
            float_nums.append(element)
        elif type(element) == bool:
            array_of_bools.append(element)
    return only_ints, list_of_strings, float_nums, array_of_bools

arr2 = [100, "Astana", -10, 1, 10.4, True, 3, 4, 70, 24, -9, "Almaty", "Aktau"]
only_ints, list_of_strings, float_nums, array_of_bools = classify_elements(arr2)
print("Integers:", only_ints)
print("Strings:", list_of_strings)
print("Floats:", float_nums)
print("Booleans:", array_of_bools)
    