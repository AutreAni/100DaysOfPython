from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(.5)
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))





