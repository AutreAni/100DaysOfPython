from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = ScoreBoard()
game_is_on = True
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.move)
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car(scoreboard.score)
    for car in car_manager.car_list:
        if car.xcor() < -360:
            car_manager.car_list.remove(car)
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() == 280:
        scoreboard.increment()
        car_manager.speed_up()
        player.go_to_start()
    car_manager.move_cars()
    screen.update()


screen.exitonclick()