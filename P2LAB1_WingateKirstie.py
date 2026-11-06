# Kirstie Wingate
# November 5, 2026
# P2LAB1
# The program will calculate the diameter, circumference, and area of a circle

# Pseudocode:
# 1. Get the radius input from the use as a float.
# 2. Calculate the diameter using 2 * radius.
# 3. Calculate the circumference using 2 * 3.14159 * radius.
# 4. Calculate the area using 3.14159 * radius * radius.
# 5. Print the formatted diameter with 1 decimal place.
# 6. Print the formatted circumference with 2 decimal places.
# 7. Print the formatted area with 3 decimal places.

radius = float(input("What is the radius of the circle? "))
print()

diameter = 2 * radius
print(f"The diameter of the circle is {diameter:.1f}")
print()

circumference = 2 * 3.14159 * radius
print(f"The circumference of the circle is {circumference:.2f}")
print()

area = 3.14159 * radius * radius
print(f"The area of the circle is {area:.3f}")