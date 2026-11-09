# Kirstie Wingate
# November 6, 2026
# P2LAB2
# A program that uses a dictionary to store vehicle MPG and calculates gas needed

# Pseudocode:
# 1. Create a dictionary with cars as keys and their MPG as values.
# 2. Create a variable that holds all the keys in the dictionary.
# 3. Print the variable that holds the keys.
# 4. Prompt the user to enter one of the vehicles from the dictionary.
# 5. Display the MPG for the vehicle that the user entered.
# 6. Prompt the user to enter the number of miles they will drive.
# 7. Calculate the gallons of gas needed (miles / MPG).
# 8. Display the gallons of gas needed, rounded to two decimal places.

car_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = car_dict.keys() 
print(keys)
print()

user_car = input("Enter a vehicle to see it's mpg: ")
print()

car_mpg = car_dict[user_car]
print(f"The {user_car} gets {car_mpg} mpg.")
print()

miles_to_drive = float(input(f"How many miles will you drive the {user_car}? "))
print()

gallons_needed = miles_to_drive / car_mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {user_car} {miles_to_drive} miles.")