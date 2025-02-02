goscie = ['Lincoln', 'Spider-Man', 'IronMan']

print(f"Cześć {goscie[0].title()} zapraszam Cię jutro na obiad!")
print(f"Cześć {goscie[1].title()} zapraszam Cię jutro na obiad!")
print(f"Cześć {goscie[2].title()} zapraszam Cię jutro na obiad!\n")

print(f"Ehh niestety, ale IronMan nie moze przyjsc\n")

# goscie.remove(goscie[-1])
goscie.remove('IronMan')
goscie.append('Wolverine')

print(f"Cześć {goscie[0].title()} zapraszam Cię jutro na obiad!")
print(f"Cześć {goscie[1].title()} zapraszam Cię jutro na obiad!")
print(f"Cześć {goscie[2].title()} zapraszam Cię jutro na obiad!\n")

print('Mamy wiekszy stół więc zapraszam wiecej osob\n')

goscie.insert(0, 'AntMan')
goscie.insert(3, 'Black Widow')
goscie.append('Hulk')

print(goscie)

popped_quest = goscie.pop()
print(f"Wybacz {popped_quest} ale nie mamy jednak miejsca")


popped_quest = goscie.pop()
print(f"Wybacz {popped_quest} ale nie mamy jednak miejsca")

popped_quest = goscie.pop()
print(f"Wybacz {popped_quest} ale nie mamy jednak miejsca")

popped_quest = goscie.pop()
print(f"Wybacz {popped_quest} ale nie mamy jednak miejsca")


print(f"Cześć {goscie[0].title()} zapraszam Cię jutro na obiad!")
print(f"Cześć {goscie[1].title()} zapraszam Cię jutro na obiad!")
print(goscie)

del goscie[0]
del goscie[0]

print(goscie)