# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.

# Read the dimensions of the cuboid from the keyboard.
a = input('a=')
b = input('b=')
c = input('c=')

# Convert the inputs from strings to integers
a = int(a)
b = int(b)
c = int(c)

# Calculate the volume of the cuboid
cuboid_volume = a * b * c

# Calculate the surface area of the cuboid
cuboid_surface_area = 2 * (a * b + b * c + a * c)

# Print the results
print(f'The volume of the cuboid with sides {a}, {b}, and {c} is {cuboid_volume}.')
print(f'The surface area of the cuboid with sides {a}, {b}, and {c} is {cuboid_surface_area}.')
