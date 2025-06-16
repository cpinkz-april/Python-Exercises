'''
Write a program to find real-number solutions of a quadratic equation
ax2 + bx + c = 0 using the quadratic formula

The program displays “No real-number solutions” when both solutions are complex
numbers.
'''

from cmath import sqrt

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
formula1 = (b**2) - (4*a*c)

x = (-b + sqrt(formula1)) / (2*a) 
y = (-b - sqrt(formula1)) / (2*a)
print(x)
print(y) 

if formula1 > 0:
    print("Two distint real solutions")
if formula1 == 0:
    print("One real (repeated) solution")
if formula1 < 0:
    print("No real-number solutions")
