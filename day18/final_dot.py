import turtle
import random
t = turtle.Turtle()
# colors = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71)]

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

turtle.colormode(255)
t.up()
t.speed("fastest")
t.hideturtle()

def dot():
    t.color((rand_color()))
    t.dot(20)
t.setheading(225)
t.fd(300)
t.setheading(0)
t.screen.setup(width=600, height=600)

for i in range(10):
    dot()
    for i in range(9):
        t.fd(50)
        dot()
    t.left(90)
    t.fd(50)
    t.left(-90)
    t.backward(450)
    

t.screen.mainloop()