names = ['ola', 'ania', 'kasia']

result = list(map(lambda x: f"{x.title()} Kowalska", names))

print(list(filter(lambda x: len(x) >= 14, result)))

