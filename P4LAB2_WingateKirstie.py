# Kirstie Wingate
# November 19, 2026
# P4LAB2 
# This program displays a multiplication table for non-negative integers and repeats if requested.

# Pseudocode:
# 1. Set run_again variable to "yes" to start the while lopp.
# 2. Ask the user to enter an integer.
# 3. Use an if/else decision to check if the integer is 0 or greater,
# 4. If 0 or greater, use a for loop from 1-12 to print the multiplication table.
# 5. If les than 0, print a message saying negative numbers are not handled.
# 6. Ask the user if they want to run the program again ("yes" or "no").
# 7. When the user enters "no", exit the while loop and print an exit message.

run_again = "yes"
while run_again == "yes":
    num = int(input("Enter an integer: "))
    print()
    if num >=0:
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")
    else:
        print("This program does not handle negative numbers.")
    print()
    run_again = input("Would you like to run the program again? ")
    print()
print("Exiting program...")