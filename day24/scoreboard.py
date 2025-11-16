from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("highscore.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("highscore.txt", "w") as file:
                file.write("0")
                self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))
        self.score = 0 # forgot to reset score on scoreboard
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()