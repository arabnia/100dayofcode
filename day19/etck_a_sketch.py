from turtle import Turtle, Screen
screen = Screen()
tur = Turtle()

screen.listen()
screen.title("Etch a Sketch")
def forward():
    tur.fd(10)

def backward():
    tur.backward(10)

def turn_right():
    tur.right(5)

def turn_left():
    tur.left(5)

def clear():
    tur.clear()


screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear, key="c")



screen.mainloop()
