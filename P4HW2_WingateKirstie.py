# Kirstie Wingate
# November 20, 2026
# P4HW2
# This program calculates regular pay, overtime pay, and gross pay for multiple employees until the user enters "Done", then displays the final totals.

# Pseudocode:
# 1. Set starting variables to 0 keep track of total employees, total overtime pay, total regular pay, and total gross pay.
# 2. Ask the user to enter the first employee's name or type "Done" to quit.
# 3. Start a while loop that keeps running as long as the name is not "Done".
# 4. Inside the loop, ask for the employee's hours worked and hourly pay rate.
# 5. Use if/else to check if the employee worked more than 40 hours and calculate overtime pay, regular pay, and gross pay.
# 6. Show the employee's pay breakdown in formatted columns.
# 7. Add 1 to the employee count and add this employee's overtime pay, regular, and gross pay to the running totals.
# 8. Ask for the next employee's name or "Done" to stop.
# 9. After the loop ends, show the total number of employees and all three pay totals.

total_employees = 0
total_overtime_pay = 0 
total_regular_pay = 0
total_gross_pay = 0

name = input('Enter employees\'s name or "Done" to terminate: ')

while name != "Done":
    hours = float(input(f"How many hours did {name} work? "))
    rate = float(input(f"What is {name}'s pay rate? "))

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
    else:
        overtime_hours = 0
        overtime_pay = 0 
        regular_pay = hours * rate

    gross_pay = regular_pay + overtime_pay

    print()
    print(f"Employee name:   {name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay':<12}")
    print("----------------------------------------------------------------------------------------")
    print(f"{hours:<15.1f}{rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<18.2f}${regular_pay:<17.2f}${gross_pay:<11.2f}")
    print()

    total_employees = total_employees + 1
    total_overtime_pay = total_overtime_pay + overtime_pay
    total_regular_pay = total_regular_pay + regular_pay
    total_gross_pay = total_gross_pay + gross_pay

    name = input('Enter employee\'s name or "Done" to terminate: ')

print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")