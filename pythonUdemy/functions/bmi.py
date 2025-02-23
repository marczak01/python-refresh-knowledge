def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

waga = float(input("Podaj wage:"))
wzrost = float(input("Podaj wzrost:"))
bmi = calculate_bmi(waga, wzrost)

def clasify_bmi(bmi):
    if bmi < 18.5: print("Masz niedowage")
    elif bmi < 25: print("Twoja waga jest w normie")
    elif bmi < 30: print("Masz nadwage")
    else: print("Masz spora nadwage")

clasify_bmi(bmi)