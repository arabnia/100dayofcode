from tkinter import *
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
## UI setup ##


## functions ##
# Load word file
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/translated_most_freq_word.csv")

row = ""
timer = None
def front_card():
    global row, data
    row = data.sample(n=1)
    canvas.itemconfig(image_on_canvas, image=fc_front_image)
    canvas.itemconfig(canvas_title, text="English", fill="black",font=("Arial", 40, "italic"))
    canvas.itemconfig(canvas_word, text=row["word"].iloc[0], fill="black", font=("Arial", 60, "bold"))

def back_card():
    global row
    canvas.itemconfig(image_on_canvas, image=fc_back_image)
    canvas.itemconfig(canvas_title, text="فارسی", fill="white", font=("vazir", 40, "bold"))
    canvas.itemconfig(canvas_word, text=row["translation"].iloc[0], fill="white", font=("vazir", 60, "bold"))

def flip_card():
    global timer
    timer = window.after(3000, back_card)

def key_button():
    global timer
    window.after_cancel(timer)
    front_card()
    flip_card()

def known_word():
    global row, data
    data = data.drop(index=row.index)
    data.to_csv("data/words_to_learn.csv")
    key_button()

window = Tk()
window.configure(background=BACKGROUND_COLOR, padx=10, pady=10)

# load image
fc_back = Canvas(window, bg="white")
fc_back_image = PhotoImage(file="./photos/card_front.png")
fc_front_image = PhotoImage(file="./photos/card_back.png")
right_button_image = PhotoImage(file="./photos/right.png")
wrong_button_image = PhotoImage(file="./photos/wrong.png")

# Canvas photo
canvas = Canvas(width=800, height=526)
image_on_canvas = canvas.create_image(400, 263)
canvas_title = canvas.create_text(400, 150, text="")
canvas_word = canvas.create_text(400, 263, text="")
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button section
right_button = Button(image=right_button_image, highlightthickness=0, width=100,height=100,
                      highlightbackground=BACKGROUND_COLOR,
                      command=known_word)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, width=100,height=100,
                      highlightbackground=BACKGROUND_COLOR,
                      command=key_button)
wrong_button.grid(row=1, column=1)

front_card()
flip_card()

window.mainloop()

