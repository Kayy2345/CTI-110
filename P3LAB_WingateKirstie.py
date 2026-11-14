# Kirstie Wingate
# November 11, 2026
# P3LAB
# A program that allows the user to enter a money (float) value with two places after the decimal

# Pseudocode:
# 1. Prompt the user to enter an amount of money as a float.
# 2. Convert the dollar amount into total cents as an integer.
# 3. If total cents is 0, display "No change".
# 4. Calculate dollars, quarters, dimes, nickels, and pennies using floor division (//) and subtraction (-).
# 5. Display each coin only if its count is greater than 0, using singular or plural labels.

# Get value from user
change = float(input("Enter the amount of money as a float: $"))

# Converting the value to an integer
cents = int(round(change * 100))

if cents == 0:
    print("No change")
else:
    # Calculate dollars (100 cents each)
    num_dollars = cents // 100
    cents = cents - (num_dollars * 100)

    # Calculate quarters (25 cents each)
    num_quarters = cents // 25
    cents = cents - (num_quarters * 25)

    # Calculate dimes (10 cents each) 
    num_dimes = cents // 10
    cents = cents - (num_dimes * 10)

    # Calculate nickels (5 cents each)
    num_nickels = cents // 5
    cents = cents - (num_nickels * 5)

    # Remaining cents are pennies (1 cent each)
    num_pennies = cents

    # Display dollars if greater than 0
    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    # Display quarters if greater than 0
    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    # Display dimes if greater than 0 
    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    # Display nickles if greater than 0
    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    # Display pennies if greater than 0
    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else: 
            print(f"{num_pennies} Pennies")