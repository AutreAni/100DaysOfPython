from turtle import Turtle, Screen, listen
from random import randint


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
screen = Screen()
user_answer = screen.textinput("Guess winner color", "Guess the color of the turtle that will win the race")
screen_size = 600
screen.setup(screen_size, screen_size)
turtles_list = []
for index, color in enumerate(colors):
    turtle = Turtle()
    turtle.color(color)
    turtle.speed(10)
    turtles_list.append(turtle)
    turtle.penup()
    turtle.shape("turtle")
    turtle_y = screen_size * .25 - ((len(colors) - index) * 30)
    turtle.goto(-(screen_size / 2) + 50, turtle_y)

race_is_on = True
winner = None
while race_is_on:
    for turtle in turtles_list:
        turtle.forward(randint(0, 10))
        if screen_size/2 - 20 <= turtle.xcor():
            race_is_on = False
            winner = turtle.pencolor()

if winner == user_answer.lower():
    print(f"You and {winner} turtle win!")
else:
    print(f"Wrong guess! {winner.capitalize()} turtle wins!")
listen()
screen.exitonclick()
