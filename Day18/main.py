#from turtle import Turtle, Screen

#timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)

#for _ in range(4):
#    timmy_the_turtle.forward(100)
#    timmy_the_turtle.left(90)

#screen = Screen()
#screen.exitonclick()

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


#for _ in range(15):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

#def draw_shape(num_sides):
#    angle = 360 / num_sides
#    for _ in range(num_sides):
#        tim.forward(100)
#        tim.right(angle)

#for shape_side_n in range(3, 11):
#    tim.color(random.choice(colours))
#    draw_shape(shape_side_n)