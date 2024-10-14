# A program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.

phone = input('Enter phone number: ')

# Format the phone number with dashes between every 3 digits
formatted_phone = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]

# Print the formatted phone number
print(f'Phone number: {formatted_phone}')
