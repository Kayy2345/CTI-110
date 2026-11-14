# Kirstie Wingate
# November 11, 2026
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average

# Pseudocode:
# 1. Prompt the user to enter gradesfor Module 1 through Module 6 as floats.
# 2. store all six grades in a list.
# 3. Calculate the lowest grades using min().
# 4. Calculate the highest grade using max().
# 5. Calculate the sum of grades using sum().
# 6. Calculate the average by dviding the sum by 1en().
# 7. Display the results formatted in aligned columns with average to 2 decimals.
# 8. Determine and display the letter grade (A, B, C, D, OR F)

# Enter grades for six modules

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()

# add grades entered to a list

module_grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# determine lowest, highest , sum and average for grades

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

# determine letter grade for average


if average_grade >= 90:
    print('Your grade is: A')
elif average_grade >= 80:
    print('Your grade is B')
elif average_grade >= 70:
    print('Your grade is: C')
elif average_grade >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')