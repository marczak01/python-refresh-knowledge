# aliens = []

# for alien_number in range(1,31):
#     new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
#     aliens.append(new_alien)

# for alien in aliens:
#     print(alien)

# print(f"całkowita liczba obcych: {len(aliens)}")

# for alien_number in aliens[:5]:
#     alien_number['color'] = 'czerwony'
#     alien_number['points'] = 10

# for alien in aliens:
#     print(alien)



osoba1 = {
    'first_name': 'Andrzej',
    'last_name': 'Kowalski',
    'age': 25,
    'city': 'Warsaw',
}

osoba2 = {
    'first_name': 'Jan',
    'last_name': 'Nowak',
    'age': 40,
    'city': 'Kolberg',
}

osoba3 = {
    'first_name': 'Adam',
    'last_name': 'Nić',
    'age': 35,
    'city': 'Koszalin',
}

osoby = [osoba1, osoba2, osoba3]

for osoba in osoby:
    full_name = f"{osoba['first_name']} {osoba['last_name']}"
    age_city = f"Ma {osoba['age']}lat i mieszka w {osoba['city']}"
    print(f"Uzytkownik ma na imie {full_name}\n{age_city}\n")



pies = {
    'gatunek': 'pies',
    'imie': 'fifek',
    'wiek': 5,
    'rasa': 'dalmatynczyk',
}

kot = {
    'gatunek': 'kot',
    'imie': 'filemon',
    'wiek': 2,
    'rasa': 'europejskiej',
}

kon = {
    'gatunek': 'kon',
    'imie': 'plotka',
    'wiek': 8,
    'rasa': 'arabskiej',
}

pets = [pies, kot, kon]

for pet in pets:
    print(f"{pet['gatunek'].title()} o imieniu {pet['imie'].title()}\n\tma {pet['wiek']} i jest rasy {pet['rasa']}")



