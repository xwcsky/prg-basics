distance = int(input("Podaj dystans: "))
hours = int(input("Podaj godziny: "))
minutes = int(input("Podaj minuty: "))

avg_speed = lambda distance, hours, minutes: distance/(hours + minutes/60)

result = avg_speed(distance, hours, minutes)
print(f'Twoja srednia predkosc to: {result}')