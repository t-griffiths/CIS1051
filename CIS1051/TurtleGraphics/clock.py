import turtle
import random
x = turtle.Screen
rick = turtle.Turtle()


for _ in range(12):
    colors = ["red","orange","yellow","green","blue","indigo","violet","cyan","magenta","pink"]
    rick.shape("circle")
    rick.pencolor(random.choice(colors))
    rick.color(random.choice(colors))
    rick.penup()
    rick.forward(60)
    rick.pendown()
    rick.forward(20)
    rick.penup()
    rick.forward(20)
    rick.stamp()
    rick.backward(100)
    rick.right(30)
