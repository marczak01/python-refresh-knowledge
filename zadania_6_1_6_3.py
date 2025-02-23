alien_0 = {'color': 'zielony', 'points': 5}

print(alien_0['color'])

new_points = alien_0['points']
print(f"Zdobyłeś {new_points} punktów")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['speed'] = 'średnio'

if alien_0['speed'] == 'wolno':
    x_increment = 1
elif alien_0['speed'] == 'średnio':
    x_increment = 2
else:
    x_increment = 3

print(f"początkowa wartosc x-position {alien_0['x_position']}")

alien_0['x_position'] += x_increment

print(f"nowa wartosc x-position {alien_0['x_position']}\n")


osoba = {
    'first_name': 'Andrzej',
    'last_name': 'Kowalski',
    'age': 25,
    'city': 'Warsaw',
}

print(osoba)
for key in osoba:
    print(osoba[key])


ulubione_liczby = {
    'marek': 25,
    'tomek': 99,
    'adam': 69,
}

for val in ulubione_liczby:
    print(f"{val.title()} : {ulubione_liczby[val]}")


glosariusz = {
    'slownik': 'To para klucz-wartość, bardzo przydatny objekt',
    'lista': 'Lista / Tablica [ ] moze zawierać rózne elementy, a kazdy z nich ma swoj indeks. Tablice zaczynaja się '
             +'od indeksu "0", ostatniego elementu mozna latwo uzyskac dostęp dzieki indeksowi "-1"',
    'krotka': 'To taka "lista/tablica", ale bez mozliwosci zmiany zapisanych w niej wartosci. Przydatne jezeli wiemy,' 
             +' ze informacje w niej zapisane nie moga ulec zmianie w trakcie dzialania programu',
}

print(glosariusz)
