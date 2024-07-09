from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.segments = []
        self.x_cor = x_cor
        self.create()


    def create(self):
        self.speed(10)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(self.x_cor, 0)

    def move_up(self):
        if self.ycor() < 250:
            self.setpos(self.x_cor, self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -230:
            self.setpos(self.x_cor, self.ycor() - 20)
