# The code below was used to grab a color palette from the image.jpg. It is no longer need and slows the program, so
# I have commented it out.
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Importing needed modules.
from turtle import Turtle, Screen
import random


# Initializing turtle and window, and setting colors to take in RGB values
john = Turtle()
screen = Screen()
screen.colormode(255)

# List of colors gathered from the color palette of image.jpg using colorgram
new_colors = [(219, 156, 91), (127, 166, 192), (55, 102, 146), (182, 65, 29), (238, 209, 96), (128, 178, 146),
              (229, 66, 99), (62, 118, 83), (240, 65, 36), (213, 126, 151), (10, 43, 66), (182, 19, 9), (143, 71, 98),
              (173, 147, 53), (80, 158, 111), (65, 40, 20), (165, 22, 35), (239, 157, 173), (158, 212, 199),
              (28, 87, 55), (17, 60, 129), (244, 166, 152), (20, 53, 37), (107, 120, 168), (173, 188, 217),
              (70, 42, 50)]


def dot_draw():
    """Draws 10 dots in random colors."""
    for i in range(10):
        john.dot(20, random.choice(new_colors))
        john.penup()
        john.forward(50)

def set_position(y_pos):
    """"Sets the position of the turtle for each line."""
    john.penup()
    john.setposition(-200, y_pos)


def draw_painting():
    """Draws the Hirst painting."""
    # This sets the starting y position in a place that centers the image.
    y_pos = -200

    # This loop prints the dots in the grid pattern.
    for n in range(10):
        set_position(y_pos)
        dot_draw()
        y_pos += 50


# Calling the function to draw the Hirst painting.
draw_painting()

# This allows us to exit the drawing screen when clicking
screen.exitonclick()
