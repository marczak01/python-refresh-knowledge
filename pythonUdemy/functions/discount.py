def calculate_discount(initial_price, discount):
    return initial_price - (initial_price * discount)/100

price = float(input("Podaj cene produktu:"))
discount = float(input("Jaki jest rabat w %:"))

wynik = calculate_discount(price, discount)
print(f"Cena po rabacie wynosi: {wynik}")