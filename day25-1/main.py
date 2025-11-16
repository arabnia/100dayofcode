import pandas as pd
import turtle as t
from tkinter import messagebox

data = pd.read_csv("data/50_states.csv")
screen = t.Screen()
answers = []
screen.setup(730,495)
screen.bgpic("photos/blank_states_img.gif")

def duplicate_name(answer):
    for state in answers:
        if state.name == answer.lower():
            return True

def check_answer(answer):
    if data[data.state.str.lower() == answer].empty:
        # messagebox.showinfo("Wrong name!", f"there isn't state called {answer}")
        screen.textinput("Wrong!", "There is no state with that name.")
        return False
    elif duplicate_name(answer):
        print(duplicate_name(answer))
        messagebox.showinfo("Duplicate name!", f"{answer} is Duplicate")
        return False
    else:
        return True

def fill_map(answer):
    state_name = t.Turtle()
    state_name.color("black")
    state_name.penup()
    state_name.name = answer.lower()
    state_name.hideturtle()
    x_cor = int(data[data.state == answer].x.iloc[0])
    y_cor = int(data[data.state == answer].y.iloc[0])
    state_name.goto(x_cor, y_cor)
    style = ('Courier', 10, 'italic')
    state_name.write(answer, font=style, align='center')
    answers.append(state_name)


while len(answers) != 50:
    if len(answers) == 0:
        answer = screen.textinput(f"{len(answers)}/50 States Correct", "Gives the firs state name!").lower()
        if check_answer(answer):
            fill_map(data[data.state.str.lower() == answer].state.iloc[0])
    else:
        answer = screen.textinput(f"{len(answers)}/50 States Correct", "Whats another state name?").lower()
        if check_answer(answer):
            fill_map(answer)
# screen.textinput("input","input")
screen.exitonclick()