from turtle import Turtle
class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_speed = 2
        self.y_speed = 2
    def move(self):
            xcor = self.xcor() + self.x_speed
            ycor = self.ycor() + self.y_speed
            self.goto(xcor,ycor)

    def y_bounce(self):
        self.y_speed *= -1

    def x_bounce(self):
         self.x_speed *= -1
                