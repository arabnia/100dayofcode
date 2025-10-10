import turtle
import random
from tkinter import messagebox

# Function to set global turtle configuration
def configure_turtle(obj):
    obj.penup()
    # t.speed("fast")  # Set speed if needed
    obj.shape("turtle")
    obj.color(colors[turtle_index])

# Initialize screen
screen = turtle.Screen()
screen.setup(500, 400)

# Colors for turtles (unused in your snippet but can be used for customization)
colors = ["red", "blue", "orange", "purple", "green", "yellow"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter the color")

# Create and configure turtles
cordination = [-100, -60, -20, 20, 60, 100]
turtles = {}

for turtle_index in range(0, 6):
    turtles_name = f"turtle_{turtle_index}"
    turtles[turtles_name] = turtle.Turtle()
    configure_turtle(turtles[turtles_name])
    turtles[turtles_name].goto(x=-230, y=(cordination[turtle_index]))

if user_bet:
    continue_game = True
else:
    print("you should select one turtle!")
while continue_game:
    for player in turtles:
        turtles[player].fd(random.randint(0,10))
        if turtles[player].xcor() > 230:
            if user_bet == turtles[player].fillcolor():
                messagebox.showinfo("end Game", "Congrat!, You Win!")
                break
            else:
                messagebox.showinfo("end Game", "Sorry!, You Lose!")
                break

# # Start the main loop
screen.mainloop()
