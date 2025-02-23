shoppingList = []

while True:
    userGrocery = input("Co musisz kupic: ")

    if userGrocery == "koniec":
        break;

    shoppingList.append(userGrocery)


def displayShoppingList(shoppingList):
    for item in shoppingList:
        print(f"- {item}")


displayShoppingList(shoppingList)