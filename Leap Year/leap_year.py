'''
A leap year is a year with 366 days. The rules to determine if a year is a
leap year are as follow:

• Any year that is divisible by 400 is a leap year.
• Of the remaining years, any year that is divisible by 100 is not a leap year.
• Of the remaining years, any year that is divisible by 4 is a leap year.
• All the remaining years are not leap years.

Write a program that accepts a year from the user and displays if the input year is a
leap year.
'''

year = int(input("Enter the year: "))

if year % 400 == 0:
    print("It's a leap year.")
elif year % 4 == 0:
    print("It's a leap year.")
elif year % 100 == 0:
    print("It's not a leap year.")
else:
    print("It's not a leap year.")
