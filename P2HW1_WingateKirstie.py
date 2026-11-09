# Kirstie Wingate
# November 8, 2026
# P2HW1
# A program that calculates and displays formatted travel expenses

# Pseudocode
# 1. Display program purpose.
# 2. Ask user to eneter their budget as a float.
# 3. Ask user to enter their travel destination.
# 4. Ask user to enter amount they will spend on gas as a float.
# 5. Ask user to enter amount they will spend on accommodation as a float.
# 6. Ask user to enter amount they will spend on food as a float.
# 7. Add expenses and subtract from budget to get remaining balance.
# 8. Display formatted results in aligned columns with $ and two decimal places.

print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
print()

destination = input("Enter your travel destination: ")
print()

gas = float(input("How much do you think you will spend on gas? "))
print()

hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food = float(input("Last, how much do you need for food? "))
print()

total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print("------------Travel Expenses------------")
print(f"{'Location: ':<20}{destination}")
print(f"{'Initial Budget: ':<20}${budget:.2f}")
print(f"{'Fuel: ':<20}${gas:.2f}")
print(f"{'Accomodation: ':<20}${hotel:.2f}")
print(f"{'food: ':<20}${food:.2f}")
print("----------------------------------------")
print()
print(f"{'Remaining Balance: ':<20}${remaining_balance:.2f}")