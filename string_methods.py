# name = "jan kowalski"
# # print(name.upper()) #capslock
# # print(name.title()) #kazdy wyraz z duzej
# name = 'Jan KOWALSKI'
# print(name.lower())


# first_name = 'jan'
# last_name = 'kowalski'

# full_name = f"{first_name} {last_name}"
# print(full_name)

# print(f"Witaj, {full_name.title()}!")



# print('Python')
# print('\tPython')
# print('Python\nTo\nSuper\nJęzyk')

# print('Języki:\n\tPython\n\tC++\n\tJavaScript')

favourite_language = 'python '
favourite_language.rstrip() #removes whitespaces on right side

favourite_language = ' python'
favourite_language.lstrip() #removes whitespaces os left side

favourite_language = ' python '
favourite_language.strip() # removes whitespaces on both sides

# jezeli nie przypiszemy zmiennej favourite_language 
# nowej wartosci to usuniecie bedzie tylko tymczasowe

favourite_language = ' python '
favourite_language = favourite_language.strip()
