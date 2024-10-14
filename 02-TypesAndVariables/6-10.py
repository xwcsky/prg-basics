# String manipulation

movie = "The Lord of the Rings: The Return of the King"

# Print the number of characters
print('Number of characters: ', len(movie))

# Print title in capital letters
print('Title in capital letters: ', movie.upper())

# Print title in small letters
print('Title in small letters: ', movie.lower())

# Print how many times the vowel "e" appears in the title
vowel = 'e'
count_vowel = movie.lower().count(vowel)  # Convert to lowercase to count all instances
print(f'Number of times the vowel "{vowel}" appears: ', count_vowel)

# Print where in the text is the word "Lord"
index_lord = movie.find("Lord")
if index_lord != -1:
    print(f'The word "Lord" is found at index: {index_lord}')
else:
    print('The word "Lord" is not found.')

# Print where in the text is the word "dragon"
index_dragon = movie.find("dragon")
if index_dragon != -1:
    print(f'The word "dragon" is found at index: {index_dragon}')
else:
    print('The word "dragon" is not found.')
