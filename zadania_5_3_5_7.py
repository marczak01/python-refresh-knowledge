alien_color = 'dasdd'
if alien_color == 'zielony':
    print('otrzymujesz 5pkt')
elif alien_color == 'zolty':
    print('otrzymujesz 10pkt')
elif alien_color == 'czerwony':
    print('otrzymujesz 15pkt')
else:
    print('nie otrzymujesz zadnych punktow')


age = 64
if age < 2:
    print('masz mniej niz 2 lata')
elif age >= 2 and age < 4:
    print('jestes dzieckiem')
elif age >= 4 and age < 13:
    print('jestes dzieckiem mlodym')
elif age >= 13 and age < 20:
    print('jestes nastolatkiem')
elif age >= 20 and age < 65:
    print('jestes dorosly')
else:
    print('jestes seniorem')


favourite_fruits = ['ananas', 'banan', 'jablko']

if 'banan' in favourite_fruits:
    print('lubisz banany')