population = (38, 88, 75, 110, 33)

population += (130,)
population += (29,)
print(population)

for pop in population:
    if pop >= 100:
        print(f"{pop} mln na miejscu {population.index(pop)+1}")

print(population[round(len(population)/2)])