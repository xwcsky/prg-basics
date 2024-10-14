# A program to calculate the volume and surface area of ​​a cube.

cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)

# Calculate the volume and surface area of the cube
cube_volume = cube_side ** 3
cube_surface_area = 6 * (cube_side ** 2)

# Print the results
print(f'The volume of a cube with side {cube_side} is {cube_volume}.')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}.')
