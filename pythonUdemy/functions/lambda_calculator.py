from functools import reduce


numbers = [1, 5, 6, 4, 3, 3, 8]

sum = reduce(lambda x, y: x + y, numbers)

print(sum / len(numbers))