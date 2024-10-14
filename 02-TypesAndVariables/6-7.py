# A program that prints a numerical representation of each letter of your name.

name = 'John'  # replace John with your name

# Iterate through each letter in the name and print its numerical representation
for letter in name:
    print(f'The letter {letter} has a code {ord(letter)}')
