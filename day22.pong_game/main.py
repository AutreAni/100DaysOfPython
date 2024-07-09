from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle(x_cor=350)
l_paddle = Paddle(x_cor=-350)
scoreboard = Scoreboard()
ball = Ball()
screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="x", fun=l_paddle.move_down)
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    # detect collision with top and bottom walls
    if ball.distance(x=ball.xcor(), y=300) < 20 or ball.distance(x=ball.xcor(), y=-300) < 20:
        ball.bounce("y")
    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 330:
        ball.bounce("x")
        scoreboard.r_increment()
    print(ball.xcor())
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce("x")
        scoreboard.l_increment()
    # detect collision with right and left walls
    if ball.xcor() > r_paddle.xcor():
        scoreboard.l_increment()
        ball.reset()
    if ball.xcor() < l_paddle.xcor():
        scoreboard.r_increment()
        ball.restart()

screen.exitonclick()
