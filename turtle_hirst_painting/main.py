import turtle

import colorgram
import turtle as t
from random import choice, randint

# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

# print(rgb_colors)
turtle.colormode(255)
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
 (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
 (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166),
 (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188),
 (34, 151, 210), (65, 66, 56), (230, 161, 166)]



jaz = t.Turtle()

jaz.speed("fastest")

jaz.pu()
jaz.hideturtle()

jaz.setheading(225)
jaz.forward(300)
jaz.setheading(0)

for _ in range(10):
    for _ in range(10):
        jaz.dot(20, choice(color_list))
        jaz.forward(50)
    jaz.setheading(90)
    jaz.forward(50)
    jaz.setheading(180)
    jaz.forward(500)
    jaz.setheading(0)





screen = t.Screen()
screen.exitonclick()


