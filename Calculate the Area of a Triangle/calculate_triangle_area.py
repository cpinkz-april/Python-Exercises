'''
Given lengths of two sides of a triangle (a, b) and an angle between
those sides (c), we can calculate the area of the triangle (A) by:

A = (a*b) * sin(c) / 2

Write a Python program that accepts lengths of two sides of a triangle (a, b),
and an angle between the sides (c) in degrees. Then, calculate and display the
area of the triangle.
'''

import math

a, b = input("Enter lengths of two sides: ").split()
c = int(input("Enter an angle between them: "))
convert_radians_to_degrees = math.radians(c)

area_triangle = ((int(a)*int(b)) * math.sin(convert_radians_to_degrees)) / 2
print(f"The area of the triangle is {area_triangle:.2f}")
