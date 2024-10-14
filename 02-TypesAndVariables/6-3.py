# A program that prints a university abbreviation

university = "Krakow University of Economics"

# Split the university name into words and take the first letter of each word
words = university.split()
abbreviation = ''.join([word[0] for word in words])

# Print the abbreviation
print(abbreviation)
