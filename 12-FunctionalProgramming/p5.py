distance = int(input("Podaj dystans: "))
hours = int(input("Podaj godziny: "))
minutes = int(input("Podaj minuty: "))

def avg_speed(distance, hours, minutes):
    hours = hours + minutes/60
    speed = distance/hours
    return speed

result = avg_speed(distance, hours, minutes)
print(f'Twoja srednia predkosc to: {result}')