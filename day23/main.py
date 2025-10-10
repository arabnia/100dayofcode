import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)


game_is_on = True
user = Player()
screen.onkey(user.move_up, "Up")
cars = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.creat()
    cars.move()
        # if car.distance(user) < 30:
        #     game_is_on = False
    

screen.exitonclick()
