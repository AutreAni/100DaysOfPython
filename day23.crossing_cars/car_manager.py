from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        super().__init__()
        self.moving_speed = STARTING_MOVE_DISTANCE
        self.car_list = []

    def create_car(self, level=0):
        if randint(1, 6 - level) == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.setheading(180)
            car.goto(300, randint(-250, 270))
            self.car_list.append(car)

    def speed_up(self):
        self.moving_speed += MOVE_INCREMENT

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.moving_speed)


