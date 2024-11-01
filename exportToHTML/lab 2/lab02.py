name = "Cami Willis"
age = 41
height = 5.7
favorite_color = ("green")

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Favorite Color:", favorite_color)

print(name, age, height, favorite_color)

print(f"Hello, my name is {name}, I am {age} years old, {height} feet tall, and my favorite color is {favorite_color}.")

print(f"{name:^20s} is a {age:d} year old, {height:.2f} feet tall, {favorite_color:s} enthusiast!")

print(f"""
Name: {name}
Age: {age}
Height: {height:.2f}
Favorite Color: {favorite_color}
""")

print(f"""
    Name: {name}
    Age: {age}
    Height: {height:.2f}
    Favorite Color: {favorite_color}
""")

print(f"""
    Name: {name}
    Age: {age}
    Height: {height:.2f}
    Favorite Color: {favorite_color}
""".strip())

import math

radius = 365
circle_area = math.pi * (radius ** 2)
print(f"Circle Area: {circle_area:.1f}")

sqrt_age = math.sqrt(age)
print(f"Square Root of Age: {sqrt_age:.2f}")

sin_height = math.sin(height)
cos_height = math.cos(height)
print(f"Sine of Height: {sin_height:.2f}")
print(f"Cosine of Height: {cos_height:.2f}")

print(f"Sum of Age and 5: {age + 5}")
print(f"Difference between Height and 4: {height - 4}")
print(f"Product of Age and Height: {age * height}")
print(f"Quotient of Height and 2: {height / 2}")
print(f"Remainder of Age divided by 3: {age % 3}")
print(f"Age raised to the power of 2: {age ** 2}")

fahrenheit = float(input("please type temp in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")



