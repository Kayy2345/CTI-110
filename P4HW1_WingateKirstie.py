# Kirstie Wingate
# November 20, 2026
# P4HW1
# This program collects valid test scores using loops, drops the lowest score, calculates the average, and displays a letter grade.

# Pseucode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to hold the valid scores.
# 3. Use a for loop to ask for each score from 1 up to the total number entered.
# 4. Inside the loop, use a while loop to check if the score is between 0 and 100.
# 5. If invalid, show an error message and ask for the score again until valid.
# 6. Add each valid score to the list.
# 7. Find the lowest score using min() and remove it from the list.
# 8. Find the average of the remaining scores using sum() and len().
# 9. Use if/elif/else to figure out the letter grade (A, B, C, D, or F).
# 10. Display the lowest score, the updated list, the average, and the letter grade.

num_scores = int(input("How many scores do you want to enter? "))
print()

scores_list = []

for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float (input(f"Enter score #{i} again: "))

    scores_list.append(score)

lowest_score = min(scores_list)
scores_list.remove(lowest_score)
average = sum(scores_list) / len(scores_list)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print()
print("--------------Results-----------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {scores_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("----------------------------------")