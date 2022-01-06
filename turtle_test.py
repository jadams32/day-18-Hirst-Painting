# This is a test file that was used to get familiar with the Turtle library. This final code draws a spirograph, give
# it a run and play with the different graphs possible

from turtle import Turtle, Screen
from random import randint
import random

john = Turtle()
john.shape("turtle")
john.color("Blue")


num = randint(1, 50)
colors = ["black", "brown", "red", "yellow", "green", "orange", "beige", "turquoise", "pink"]
deg_choices = range(0, 361, 4)
john.speed('fastest')

john.circle(100)

for i in deg_choices:
    john.circle(100)
    john.setheading(i)
    john.color(random.choice(colors))



screen = Screen()
screen.exitonclick()
