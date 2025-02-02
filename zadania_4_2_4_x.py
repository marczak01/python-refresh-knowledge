# numbers = list(range(1,11))
# print(numbers)

# numbers2 = []
# for number in range(1,11):
#     numbers2.append(number*2)

# print(numbers2)

# numbers3 = []
# for number in range(2,20,2):
#     numbers3.append(number)

# print(numbers3)

# many_numbers = list(range(1,941421, 2))
# print(sum(many_numbers))

# squares = [value**2 for value in range(1,11)]
# print(squares)



# zadania

# for number in range(1,21):
#     print(number)

# for number in range(1,1000001):
#     print(number)


million = [value for value in range(1,1000001)]

print(min(million))
print(max(million))
print(sum(million))

evens = [value for value in range(1,21,2)]
print(evens)

third_power = [value**3 for value in range(3,31)]
for num in third_power:
    print(num)