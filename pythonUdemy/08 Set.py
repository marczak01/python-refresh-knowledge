# names = {'Kasia', 'Basia', 'Ola', 'Ania', 'Lisa'}

# names.add('Olek')
# names.add('Tomek')
# names.add('Basia')
# names.add('Kacper')
# names.add('Alex')

# print(names)
# print(len(names))

# for el in names: print(el)


def kosztPrzesylki(waga, wys, szer, dlu):
    if wys >= 50 and szer >= 50 and dlu >= 50:
        if waga >= 5: return 50
        else: return 25
    elif wys >= 20 and szer >= 20 and dlu >= 20:
        if waga >= 5: return 20
        else: return 15
    else: return 10

wynik = kosztPrzesylki(5, 40, 30, 55)
print(wynik)