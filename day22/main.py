from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong!")
screen.listen()
screen.tracer(0)
 
paddle_1 = Paddle((350,0))
paddle_2 = Paddle((-350,0))

screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")
ball = Ball()
for _ in range(1000):
    screen.update()
    ball.move()
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.y_bounce()
    if ball.distance(paddle_1) < 40 and ball.xcor() > 340 or ball.distance(paddle_2) < 40 and ball.xcor() < -340:
        ball.x_bounce()
    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.x_bounce()
        ball.y_bounce()
    if ball.xcor() < -380:
        ball.goto(0,0)
        ball.x_bounce()
        ball.y_bounce()

screen.exitonclick()