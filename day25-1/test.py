# import pandas as pd
# data = pd.read_csv("data/50_states.csv")
#
# print(int(data[data.state.str.lower() == "texas"].x.iloc[0]))
# print(int(data[data.state.str.lower() == "texas"].y.iloc[0]))
# print(data[data.state.str.lower() == "new york"].state.iloc[0])
import turtle
import turtle as t

def turtle_message(title, message):
    screen = t.Screen()

    # پن برای کشیدن جعبه
    box = t.Turtle()
    box.hideturtle()
    box.penup()

    # کشیدن پنجره پیام
    box.goto(-150, 50)
    box.pendown()
    box.fillcolor("white")
    box.begin_fill()
    for _ in range(2):
        box.forward(300)
        box.right(90)
        box.forward(120)
        box.right(90)
    box.end_fill()
    box.penup()

    # نوشتن عنوان
    box.goto(0, 20)
    box.write(title, align="center", font=("Arial", 14, "bold"))

    # نوشتن متن پیام
    box.goto(0, -10)
    box.write(message, align="center", font=("Arial", 12))

    # دکمه OK
    box.goto(0, -60)
    box.write("[  OK  ]", align="center", font=("Arial", 12, "bold"))

    # بستن با کلیک
    def close_msg(x, y):
        if -40 < x < 40 and -75 < y < -45:
            box.clear()
            screen.onclick(None)  # غیرفعال کردن کلیک

    screen.exitonclick(close_msg)

turtle.listen("kir", "tonamus")