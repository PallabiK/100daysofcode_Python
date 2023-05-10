#####Turtle Intro######

import turtle as t

jaz = t.Turtle()
jaz.shape("turtle")
jaz.color("indigo")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############
#for _ in range(4):
#  tim.forward(100)
#  tim.left(90)

########### Challenge 2 - Draw a Dashed Line ########
# for _ in range(15):
#   jaz.forward(10)
#   jaz.up()
#   jaz.forward(10)
#   jaz.down()

########### Challenge 3 - Draw Shapes ########

from random import choice, randint

# colors = ["red", "green", "blue", "yellow", "indigo", "chocolate", "dark olive green", "magenta",
# "blanched almond", "dark green", "aquamarine", "deep sky blue"]
#
#
# for sides in range(3, 11):
#   angle = 360 / sides
#   jaz.color(choice(colors))
#   for _ in range(sides):
#     jaz.forward(100)
#     jaz.right(angle)


########## Challenge 4 - Random Walk ########
t.colormode(255)
def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)

# jaz.pensize(10)
jaz.speed("fastest")
#
# directions = [0, 90, 180, 270]
#
# for _ in range(300):
#   jaz.color(random_color())
#   jaz.forward(30)
#   jaz.setheading(choice(directions))
#


########### Challenge 5 - Spirograph ########
def draw_spirograph(size_of_gap):
  for _ in range(int(360/size_of_gap)):
    jaz.color(random_color())
    jaz.circle(100)
    #jaz.left(5)
    jaz.setheading(jaz.heading()+ size_of_gap)

draw_spirograph(3)



screen = t.Screen()
screen.exitonclick()

