from functools import reduce


users = [
    {'name': 'Adam', 'age': 17},
    {'name': 'Kamil', 'age': 18},
    {'name': 'Ania', 'age': 22},
    {'name': 'Tomek', 'age': 40},
]

result = filter(lambda x: x['age'] > 18, users)
result = list(result)
print(result)
double_age = map(lambda x: x['age'] * 2, result)
double_age = list(double_age)
print(double_age)
sum_ages = reduce(lambda x, y: x + y, double_age)
print(sum_ages)