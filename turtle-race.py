from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet",
                            prompt = "Which turtle will win the race?\nEnter a color of the rainbow: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions =[-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. :/ The {winning_color} turtle is the winner.")

        rand_distance = randint(0, 30)
        turtle.forward(rand_distance)

screen.exitonclick()
