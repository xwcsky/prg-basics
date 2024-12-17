###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   z = x + y
   a = z / 2
   return a

# takes two numbers from keyboard
n1 = int(input("Wpisz pierwsza liczbe: "))
n2 = int(input("Wpisz druga liczbe: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')