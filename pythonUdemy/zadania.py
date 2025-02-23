# # user_name = input("Podaj imie: ")
# # user_lastname = input("Podaj nazwisko: ")
# # user_city = input("Podaj miasto: ")

# # print(f"Uzytkownik nazywa się: {user_name} {user_lastname} i mieszka w {user_city} " )



# game_map = []
# new_list = []
# new_list2 = []
# for i in range(1,5):
#     if i % 2 == 0:
#         new_list.append(0)
#     else:
#         new_list.append(1)
#     game_map.append(new_list)
#     for x in range(1,100):
#         if x % 2 == 0:
#             new_list2.append(9)
#         else:
#             new_list2.append(99)
#         game_map.append(new_list2)

# print(game_map)


# 1C 55 BD 9C
# 55 1C 9C BD
# BD 9C 1C 55
# 9C 


data = [0,1,2,3,4,5,6]
print(len(data))
del data[1]
print(data)

if 3 in data:
    print('liczba 3 w liscie')

for el in data:
    print(el)

for el in data:
    print(el * 2)


