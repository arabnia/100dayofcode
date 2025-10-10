from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.cars = []
        self.SPEED = STARTING_MOVE_DISTANCE
    def creat(self):
        if random.randrange(1,6) == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.goto(300,random.randrange(-250,240))
            self.cars.append(new_car)

    def accelerate(self):
        self.SPEED += MOVE_INCREMENT

    def move(self):
        for every in self.cars:
            every.fd(-self.SPEED)

