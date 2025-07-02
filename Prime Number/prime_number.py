'''
Write a program that accepts a positive integer p. It then check if p is a
prime number. Note that a prime number is a positive integer greater than 1 whose
only factors are 1 and the number itself.
'''

import math

n = int(input("Enter a number to check if it's prime: "))

if n >= 1:
    if n == 2 or n == 3:
        print("It's a prime number.")
    if n!= 2 or n != 3:
        if n % 2 == 0 or n % 3 == 0:
            print("It's not a prime number.")
        elif n % math.isqrt(n) == 0:
            print("It's not a prime number.")
        else:
            print("It's a prime number.") 
