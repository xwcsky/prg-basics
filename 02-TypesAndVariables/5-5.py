# A program to calculate the discounted product price and the discount reduction.

# Read the product price and discount percentage from the keyboard.
price_string = input('Enter price: ')
discount_string = input('Enter discount %: ')

# Convert the inputs to the appropriate types
price = float(price_string)
discount = float(discount_string)

# Calculate the discount amount
discount_amount = price * (discount / 100)

# Calculate the discounted price
discounted_price = price - discount_amount

# Print the product price, discounted price, and the discount amount with two decimal places
print(f'Price with discount: {discounted_price:.2f}')
print(f'Reduction: {discount_amount:.2f}')
