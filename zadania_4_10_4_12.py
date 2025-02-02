jedzenie = ['banan', 'pomidor', 'ananas', 'truskawka', 'ser', 'jogurt', 'chleb']

print(f"First 3 elements: {jedzenie[:3]}")
print(f"3 elements in the middle: {jedzenie[2:5]}")
print(f"Last 3 elements: {jedzenie[-3:]}")



moja_pizza = ['ser', 'peperoni', 'szpinak']
twoja_pizza = moja_pizza[:]

moja_pizza.append('chilli')
twoja_pizza.append('olives')

print(f"My pizza has ingredients: {moja_pizza} and your pizza has: {twoja_pizza}")