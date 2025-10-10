import turtle
import random
color_list = ["cornflower blue","deep sky blue", "deep sky blue","medium purple","orchid","orange","goldenrod","aquamarine","light pink"]
t = turtle.Turtle()
t.pensize(15)
t.speed("fastest")

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def rand_walk():
    t.color(rand_color())
    t.setheading(random.choice([0,90,180,270]))
    t.fd(25)
    
turtle.colormode(255)
for _ in range(200):
    rand_walk()
turtle.colormode(255)
# t.color(rand_color())
# t.screen.mainloop()