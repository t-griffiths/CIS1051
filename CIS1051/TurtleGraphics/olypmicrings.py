import turtle
x = turtle.Screen()
circ = 75
tim = turtle.Turtle()
tim.penup()
tim.goto(-175,0)
tim.pendown()
tim.pensize(15)

tim.pencolor("blue")
tim.circle(circ)
tim.penup()
tim.forward(200)

tim.pencolor("black")
tim.pendown()
tim.circle(circ)
tim.penup()
tim.forward(200)

tim.pencolor("red")
tim.pendown()
tim.circle(circ)
tim.penup()

tim.right(90)
tim.forward(75)
tim.right(90)
tim.forward(100)
tim.right(180)
tim.pendown()

tim.pencolor("green")
tim.circle(circ)
tim.penup()
tim.right(180)
tim.forward(200)
tim.right(180)

tim.pencolor("yellow")
tim.pendown()
tim.circle(circ)



