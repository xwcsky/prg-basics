###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age >=65:
    print('You can get a discount')
else:
    print("You can't get a discount")