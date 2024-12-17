n1 = int(input("Wpisz liczbe w m/s: "))


def ms_to_kmh(ms):
    kmh = ms*3.6
    return kmh

result = ms_to_kmh(n1)

print(f'Mordeczko twoj wynik to {result}km/h')