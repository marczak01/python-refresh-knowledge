# uzytkownicy = ['marczak01', 'admin', 'tomek133', 'basiabasia', 'koxok']
uzytkownicy = []

if uzytkownicy:
    for uzytkownik in uzytkownicy:
        if uzytkownik == 'admin':
            print(f"Witaj {uzytkownik} jestes adminem. ")
        else:
            print(f"Witaj {uzytkownik}")
else:
    print(f"Na liście mamy {len(uzytkownicy)} uzytkownikow. Musimy znaleźć nowych uzytkownikow.")


current_users = ['marczak01', 'admin', 'tomek133', 'basiabasia', 'koxok']
new_users = ['toMek133', 'adixon', 'pikaczu', 'starbaks']

if new_users:
    for user in new_users:
        if user.lower() in current_users:
            print(f"{user} podobna nazwa znajduje sie juz na liscie uzytkownikow")
        else:
            print(f"{user} witaj na naszej stronie!")
else:
    print('brak uzytkownikow do sprawdzenia')


# zarejestrowani_uzytkownicy = ['marczak01', 'tomek1333', 'antonikowal9', 'koksik0']
# nowi_uzytkownicy = ['alexx', 'andrzej55', 'arek2', 'ToMeK1333', 'kubek1']

# let zarejestrujUzytkownika = function(uzytkownicy){
#     for(let i = 0; i < uzytkownicy.length; i++){
#         if(zarejestrowani_uzytkownicy.includes(uzytkownicy[i])){
#             console.log('mamy juz uzytkownika o podanej nazwie ${uzytkownicy[i]}');
#         } else {
#             zarejestrowani_uzytkownicy.push(uzytkownicy[i]);
#         }
#     }
# }

# zarejestrujUzytkownika(nowi_uzytkownicy);
# console.log(zarejestrowani_uzytkownicy)


liczby = [value for value in range(1,10)]

for val in liczby:
    if val == 1:
        print(f"{val}st")
    elif val == 2:
        print(f"{val}nd")
    elif val == 3:
        print(f"{val}rd")
    else:
        print(f"{val}th")