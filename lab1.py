import math

#Get input data
a = int(input("Enter side of cube in cm "))
b = int(input("Enter side of tetdahedron in cm "))


#Calculate volume of cube in cm
def cube_volume(a):
    volume = a**3
    return round(volume, 2)

get_volume = cube_volume(a)
print(f'The volume of your cube is {get_volume} cm')

def tetrahedron_volume(b):
    # volume = a**3*(math.sqrt(2))
    volume = (b ** 3 / (6 * math.sqrt(2)))
    return round(volume, 2)

get_tetrahedron = tetrahedron_volume(b)
print(f'The volume of your tedrahedron is {get_tetrahedron} cm')