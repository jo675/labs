import math
from typing import Text

def cube_volume():
    """
    Calculate the volume of a cube
    """
    a = eval(input("Enter side of cube in cm "))
    volume = a**3
    return round(volume, 2)

def tetrahedron_volume():
    """
    Calculate the volume of a tedrahedron
    """
    b = eval(input("Enter side of tetrahedron in cm "))
    volume = (b ** 3 / (6 * math.sqrt(2)))
    return round(volume, 2)

while True:
    print('Press 1 if you want to calculate volume of cube\nPress 2 if you want to calculate volume of tetrahedron\nPress Q if you want to quit\n')
    x = input('select: ')
    if x == '1':
        y = cube_volume()
        print(f'The volume of your cube is {y} cm^3\n')
    elif x == '2':
        z = tetrahedron_volume()
        print(f'The volume of your tedrahedron is {z} cm^3\n')
    elif x == 'Q':
        print('Good bye')
        break
    else:
        print('wrong option')
