from turtle import Turtle
my_turtle = Turtle()
# my_turtle.screen.title('dashed line')
# my_turtle.screen.bgcolor("blue")
yal = 4
degri = 360 / yal
my_turtle.color("red", "green")
while True:
    my_turtle.fd(100)
    my_turtle.right(degri)
    if abs(my_turtle.pos()) < 1:
        if yal < 8:
            yal += 1
            degri = 360 / yal
            my_turtle.color("blue")
        else:
            break

my_turtle.screen.mainloop()