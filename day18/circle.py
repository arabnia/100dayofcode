import turtle
import random
t = turtle.Turtle()

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
angel = 8
turtle.colormode(255)
# t.color(rand_color())
t.speed("fastest")
def rasm():
    t.color("blue")
    t.circle(100)
    t.right(angel)

for _ in range(int(360 / angel)):
    rasm()

t.screen.mainloop()