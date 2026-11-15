# Kirstie Wingate
# November 15, 2026
# P3HW2
# This programm calculates an employee's regular pay, overtime pay, and gross pay

# Pseudocode: 
# 1. Prompt the user to enter the employee's name, hours worked, and pay rate.
# 2. Check is hours worked is greater than 40 using an if/else statement.
# 3. If hours worked is greater than 40, calculate overtime hours (hours - 40), overtime pay (overtime hours * pay rate * 1.5), and regular pay (40 * pay rate).
# 4. Otherwise, set overtime hours and overtime pay to 0, and calculate regular pay  (hours worked * pay rate).
# 5. Calculate gross pay by adding regular pay and overtime pay.
# 6. Display the employee name and formatted columns for hours worked, pay rate, overtime hours, overtime pay, regular pay, and gross pay.

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

gross_pay = regular_pay + overtime_pay

print("-------------------------------------")
print(f"Employee name:   {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("--------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<15.1f}{overtime_hours:<15.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}")