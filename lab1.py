import math

# Get input data
a = float(input("Enter side of cube in cm "))
b = float(input("Enter side of tetrahedron in cm "))

# Calculate volume of cube in cm
def cube_volume(a):
    volume = a**3
    return round(volume, 2)

# Calculate volume of tetrahedron in cm
def tetrahedron_volume(b):
    volume = (b ** 3 / (6 * math.sqrt(2)))
    return round(volume, 2)

# Perform calculations
get_volume = cube_volume(a)
get_tetrahedron = tetrahedron_volume(b)

print(f'The volume of your cube is {get_volume} cm')
print(f'The volume of your tedrahedron is {get_tetrahedron} cm')
