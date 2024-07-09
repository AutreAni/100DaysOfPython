from turtle import Turtle, Screen
from food import Food
from snake import Snake, ORIENTATION
from scoreboard import ScoreBoard
import time
screen = Screen()
border = 290
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

for direction in ORIENTATION:
    screen.onkey(key=direction.capitalize(), fun=getattr(snake, direction))

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    # detect collision with wall
    if snake.head.xcor() > border or snake.head.xcor() < -border or snake.head.ycor() > border or snake.head.ycor() < -border:
        snake.refresh()
        scoreboard.refresh()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if segment.distance(snake.head) < 5:
            snake.refresh()
            scoreboard.refresh()




screen.exitonclick()