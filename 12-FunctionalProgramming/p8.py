n1 = input("Wpisz imie: ")
n2 = input("Wpisz nazwisko: ")

initials = lambda name, surname: name[0] + surname[0]

result = initials(n1,n2)

print(result)