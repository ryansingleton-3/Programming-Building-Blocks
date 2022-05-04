import math
square = float(input('What is the length of a side of the square? '))
print(f'The area of the square is: {square ** 2}.')

rectangle_length = float(input('What is the length of the rectangle? '))
rectangle_width = float(input('What is the width of the rectangle? '))
rectangle_area = rectangle_length * rectangle_width
print(f'The area of the rectangle is: {rectangle_area}.')


circle_radius = float(input('What is the radius of the circle? '))
circle_area = math.pi * (circle_radius ** 2)
print(f'The area of the circle is {circle_area}.')




length_value = float(input('What is the length value? '))
new_square_area = length_value ** 2
new_circle_area = math.pi * (length_value ** 2)
cube_volume = length_value ** 3
print(f'The area of the square is: {new_square_area}')
print(f'The area of the circle is: {new_circle_area}')
print(f'The volume of the cube is: {cube_volume}')
sphere_volume = (4/3) * math.pi * (length_value ** 3)
print(f'The volume of the sphere is {sphere_volume}.')

