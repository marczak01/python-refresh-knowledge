def increase_salary(money, bonus):
    money += money * 0.2
    return money + bonus

salary = 5000

wynik = increase_salary(salary, 1000)
print(wynik)

print(salary)