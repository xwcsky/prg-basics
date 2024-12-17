n1 = int(input("Wpisz liczbe w m/s: "))

ms_to_kmh = lambda ms: ms*3.6

result = ms_to_kmh(n1)

print(f'Mordeczko twoj wynik to {result}km/h')