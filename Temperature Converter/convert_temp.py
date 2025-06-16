''' Write a program that accepts a temperature in kelvin (k) from a user. 
The program then converts the temperature to degree celsius and displays the
result with 2 digits after the decimal point.

c = k - 273.15 

Input temperature in kelvin: 0
Temperature in degree celsius: -273.15
'''

kelvin = input("Enter the temperature in kelvin (K): ")
convert_to_celsius = int(kelvin) - 273.15

print(f"Temperature in degree Celsius: {convert_to_celsius:.2f}")
