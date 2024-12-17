n1 = int(input("Podaj liczbe: "))

is_even = lambda number : True if number % 2 == 0 else False
 
result = is_even(n1)

print(result)