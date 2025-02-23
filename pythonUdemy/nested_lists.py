nested_lists = [
    [1,2,3],
    ['a','b','c'],
    [True, False, True]
]

for nested_list in nested_lists:
    print(f"list: {nested_list}")
    for el in nested_list:
        print(el)
    else:
        print('\n')