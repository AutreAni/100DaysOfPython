from turtle import Turtle, Screen, colormode
from random import random, randint, choice
from colors import colors

colormode(255)
tao = Turtle()

# turtle setups
tao.hideturtle()
tao.speed(10)
tao.penup()

# dot setups
dot_quantity = 10
dot_size = 15
distance = 30

# bring cursor to bottom left
tao_x = -(dot_size + distance) * (dot_quantity / 2)
tao_y = -(dot_size + distance) * (dot_quantity / 2)
tao.setposition(tao_x, tao_y)
for j in range(1, 1 + dot_quantity):
    for i in range(1, 1 + dot_quantity):
        color = choice(colors)
        tao.dot(dot_size, color)
        tao.forward(dot_size + distance)
    # reposition y for every new line
    tao_y = tao_y + (dot_size + distance)
    tao.setposition(tao_x, tao_y)

screen = Screen()
screen.exitonclick()
