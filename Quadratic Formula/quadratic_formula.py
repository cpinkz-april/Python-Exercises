'''
Write a program to solve a quadratic equation ax^2 + bx + c = 0 using the quadratic formula
'''

from cmath import sqrt

value = 1

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
formula1 = (b**2) - (4*a*c)

if value:
    x = (-b + sqrt(formula1)) / (2*a) 
    y = (-b - sqrt(formula1)) / (2*a)
    print(x)
    print(y) 
