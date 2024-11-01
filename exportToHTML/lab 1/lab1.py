import math

radius = 5
area = math.pi * (radius ** 2)
print("Area of the circle:", area)

radius = 3
volume = (4/3) * math.pi * (radius ** 3)
print("Volume of the sphere:", volume)

a = 3
b = 4
hypotenuse = math.sqrt(a**2 + b**2)
print("Hypotenuse of the triangle:", hypotenuse)

full_name = "Cami R Willis"
print("Length of name:", len(full_name))

first_name = "Cami"
middle_name = "R"
last_name = "Willis"
print("Full name:", first_name + " " + middle_name + " " + last_name)

print("Name in uppercase:", full_name.upper())
print("Name in lowercase:", full_name.lower())

age = 41
height_feet = 5
height_inches = 7
weight = 135

print("Age:", age, "(", "years", ")")
print("Height:", height_feet, "feet", height_inches, "inches (", "feet/inches", ")")
print("Weight:", weight, "(", "pounds", ")")

bmi = weight / ((height_feet * 12 + height_inches) ** 2) * 703
print("BMI:", bmi)
