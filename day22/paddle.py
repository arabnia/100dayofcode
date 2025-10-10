from turtle import Turtle
SPEED = 20
class Paddle(Turtle):
    def __init__(self,position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(1,5)
        self.penup()
        self.goto(position)
        
    def move_up(self):
        self.fd(SPEED)
        
    def move_down(self):
        self.bk(SPEED)
    

