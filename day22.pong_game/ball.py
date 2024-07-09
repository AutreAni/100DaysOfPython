from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        prev_x = self.xcor()
        prev_y = self.ycor()
        self.setpos(prev_x + self.x_move, prev_y + self.y_move, )

    def bounce(self, axis):
        if axis == "x":
            self.x_move *= -1
        elif axis == "y":
            self.y_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = .1
