from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write_score()

    def increment(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 14, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over!", align="center", font=("Courier", 20, "bold"))
