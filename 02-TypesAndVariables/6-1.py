# A program that calculates the number of characters
# of your name, surname, and full name

name = 'Anna'   # replace Anna with your name
surname = 'May' # replace May with your surname

# Calculate the number of characters in name and surname
characters_in_name = len(name)
characters_in_surname = len(surname)

# Calculate the number of characters in the full name (with space between name and surname)
full_name = name + ' ' + surname
characters_in_full_name = len(full_name)

# Print the results
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters')  # with a space between name and surname
