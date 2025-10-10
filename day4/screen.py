# import turtle
from turtle import Turtle, Screen

# Create an instance of the Screen class
screen = Screen()

# Create a turtle object
my_turtle = Turtle()

# Use the listen method on the screen instance
screen.listen()
# screen.bgcolor("red")

# Example of how to bind a key press event to a function
def move_forward():
    my_turtle.forward(100)

screen.onkey(move_forward, "Up")

# Keep the window open until it is closed by the user
screen.mainloop()
