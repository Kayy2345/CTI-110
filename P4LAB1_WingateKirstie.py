# Kirstie Wingate
# November 18, 2026
# P4LAB1
# This program uses turtle graphics and loops to draw a house.

# Pseudocode:
# 1. Import turtle and set separate colors for the background and turtle.
# 2. Draw a square base using a for loop.
# 3. Lift the pen and move to the top-left corner of the square.
# 4. Draw a triangle roof using a while loop.
# 5. Keep the window open until clicked.

import turtle

win = turtle.Screen()
win.bgcolor("pink")

t = turtle.Turtle()
t.color("blue")
t.shape("turtle")

for side in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
count = 0 
while count < 3:
    t.forward(100)
    t.left(120)
    count = count + 1
win.exitonclick()