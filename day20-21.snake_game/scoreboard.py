from turtle import Turtle

with open("data.txt", mode="r") as data:
    highest_score = int(data.read())


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = highest_score
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        text = f"Score: {self.score}, Highest Score: {self.highest_score}"
        self.write(arg=text, align="center", move=False, font=('Arial', 8, 'normal'))

    def refresh(self):
        if self.highest_score < self.score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highest_score))
        self.score = 0
        self.write_score()

    def increase(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", move=False, font=('Arial', 8, 'normal'))
