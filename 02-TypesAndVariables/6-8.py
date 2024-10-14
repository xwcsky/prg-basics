# A program that calculates
# how many letters are between two given letters

# Get input from the user
first = input('Enter first letter: ')
last = input('Enter last letter: ')

# Get the numerical representations of the letters
first_letter_code = ord(first)
last_letter_code = ord(last)

# Calculate the number of letters between the two letters
number_of_letters = abs(last_letter_code - first_letter_code) - 1

# Print the result
print(f'Between {first} and {last} is {number_of_letters} letters')
