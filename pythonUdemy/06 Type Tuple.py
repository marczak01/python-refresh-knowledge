numbers = (50, 100, 150, 200, 250)

print(type(numbers))
print(numbers[len(numbers) - 1])
print(len(numbers))
print(numbers[1:4])


wydatki = (100, 200, 300, 500, 800, 350)
suma_wydatkow = 0
for wydatek in wydatki: suma_wydatkow += wydatek

print(suma_wydatkow)