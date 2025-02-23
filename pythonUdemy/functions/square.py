def calculate_square():
    user = input('Podaj liczbe calkowita ')
    user = int(user)
    return user * user

print(f"pole kwadratu wynosi: {calculate_square()}")

def calculate_float_square():
    user = input('Podaj liczbe calkowita ')
    user = float(user)
    return round(user * user, 2)

print(f"pole kwadratu wynosi: {calculate_float_square()}")
