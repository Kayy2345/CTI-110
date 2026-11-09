# Kirstie Winagte
# November 8, 2026
# P2HW2
# A program that stores module test grades in a list and displays statistics

# Pseudocode:
# 1. Prompt the user to enter grades for Module 1 through Module 6 as floats.
# 2. Store all six entered grades into a descriptively name list.
# 3. Calculate the lowest grade using min().
# 4. Calculate the highest grade using max()
# 5. Calculate the sum of grades using sum().
# 6. Calculate the average by dividing the sum by len().
# 7. Display the results formatted in aligned columns with average to 2 decimals.

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter garde for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for module 6: "))
print()

module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_grades = sum(module_grades)
average_grade = sum_grades / len(module_grades)

print("------------Results------------")
print(f"{'Lowest Grade: ':<20}{lowest_grade}")
print(f"{'Highest Grade: ':<20}{highest_grade}")
print(f"{'Sum of Grades: ':<20}{sum_grades}")
print(f"{'Average: ':<20}{average_grade:.2f}")
print("----------------------------------------")