from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        self.hideturtle()
        self.write(f"Score: {self.score}",align="center",font=('Arial', 20, 'normal'))

    def increase(self):
        self.score += 1 
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=('Arial', 20, 'normal'))

    def gameover(self):
        self.goto(x=0,y=0)
        self.write("Game Over !",align="center",font=('Arial', 18, 'normal'))

