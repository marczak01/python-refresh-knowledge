import time
t_start = time.perf_counter()
address_book = {
    'Jan Kowalski': {'city': 'Kraków', 'age': 44, 'country': 'Poland' },
}
# print(address_book)

address_book['Zygmunt Stary'] = {'city': 'Gniezno'}
print(address_book)

address_book['Zygmunt Stary']['age'] = 69
print(address_book)

del address_book['Jan Kowalski']
print(address_book)

address_book.clear()
print(address_book)

t_end = time.perf_counter()
print(t_end - t_start)