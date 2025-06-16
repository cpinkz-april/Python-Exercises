''' The stone, pound, and ounce are English units of mass, where 1
stone is equal to 14 pounds, and 1 pound is equal to 16 ounces. One kilogram 
is equal to 2.2 pounds.

Write a program that accepts a mass in stones, pounds, and ounces from a 
user. It then calculates and displays the equivalent mass in kilograms.

Input a mass in stones, pounds, ounces: 1 3 4
The equivalent mass in kg = 7.84
'''

stones, pounds, ounces = input("Input a mass in stone, pounds, ounces: ").split()
convert_stones_to_pounds = float(stones) * 14
convert_ounces_to_pounds = float(ounces) / 16
mass = float(convert_stones_to_pounds) + float(pounds) + float(convert_ounces_to_pounds)
convert_mass_to_kg = float(mass) / 2.2

print(f"The equivalent mass in kg = {convert_mass_to_kg:.2f}")
