from turtle import Turtle, Screen,colormode
from random import randint, choice

tao = Turtle()
tao.color("green")
screen = Screen()
colormode(255)
tao.speed(10)

def gen_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 55)
    return (r, g, b)

for i in range(36):
    tao.color(gen_random_color())
    tao.circle(100)
    tao.left(10)


screen.exitonclick()
