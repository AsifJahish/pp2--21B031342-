

person = {
    'first_name': 'Asabeneh',
    'relative':['uncle', 'father', 'mother', 'brother', 'sister'],
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'relative':
        for relat in person['relative']:
            print(relat, end= " ")
print("\n")