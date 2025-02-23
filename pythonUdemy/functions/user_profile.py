userProfile = {}

def create_user_profile(first_name = None, age = 0, last_name = None, city= None):
    first_name = input("Wprowadź swoje imie: ")
    if first_name:
        userProfile['first_name'] = first_name
    last_name = input("Wprowadź swoje nazwisko (opcjonalne): ")
    if last_name:
        userProfile['last_name'] = last_name
    age = input("Wprowadź swój wiek: ")
    if age:
        userProfile['age'] = age
    city = input("Wprowadź swoje miejsce zamieszkania: ")
    if city:

        userProfile['city'] = city

    return userProfile


wynik = create_user_profile()
print(wynik)