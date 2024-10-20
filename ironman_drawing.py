
import turtle

# Create turtle object
ironman = turtle.Turtle()

# Background settings
turtle.bgcolor("black")
ironman.speed(10)

# Head of Iron Man
ironman.color("yellow")
ironman.begin_fill()
ironman.circle(100)
ironman.end_fill()

# Face details
ironman.penup()
ironman.goto(-35, 50)
ironman.pendown()
ironman.color("red")
ironman.begin_fill()
ironman.circle(35)
ironman.end_fill()

ironman.penup()
ironman.goto(35, 50)
ironman.pendown()
ironman.begin_fill()
ironman.circle(35)
ironman.end_fill()

# Closing the turtle window
turtle.done()
