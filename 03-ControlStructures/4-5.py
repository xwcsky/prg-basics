###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    chartercode = ord(char)
    chartercode += 1
    encrypted_text = encrypted_text + chr(chartercode)   
print(plain_text)
print(encrypted_text)