sides = int(input("Enter the amount of sides you would like"))

import turtle
x = turtle.Screen
james = turtle.Turtle()
james.pencolor("purple")

angle = 360 / sides
for count in range(sides):
            james.forward(50)
            james.right(angle)
