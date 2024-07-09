from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_score()

    def l_increment(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_increment(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.goto(-100, 100)
        self.write(f"{self.l_score}", align="center", font=('Arial', 20, 'bold'))
        self.goto(100, 100)
        self.write(f"{self.r_score}", align="center", font=('Arial', 20, 'bold'))

    def write_game_over(self, winner):
        self.goto(0, 0)
        self.write(f"Game over!!! {winner} wins", align="center", font=('Arial', 14, 'bold'))
