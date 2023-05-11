from turtle import Turtle, Screen

jaz = Turtle()
screen = Screen()

def move_forwards():
    jaz.forward(10)

def move_backwards():
    jaz.backward(10)

def clockwise():
    jaz.left(10)

def counter_clockwise():
    jaz.right(10)

def clear():
    jaz.penup()
    jaz.clear()
    jaz.home()
    jaz.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(clockwise, "d")
screen.onkey(counter_clockwise, "a")
screen.onkey(clear, "c")
screen.exitonclick()
