from tkinter import *
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
## UI setup ##


## functions ##
# Load word file
data = pd.read_csv("data/translated_most_freq_word.csv")
def random_word():
    return random.choice(data["word"])

def key_action():
    word = random_word()
    canvas.itemconfig(canvas_word, text=word)

window = Tk()
window.configure(background=BACKGROUND_COLOR, padx=10, pady=10)

# load image
fc_back = Canvas(window, bg="white")
fc_front_image = PhotoImage(file="./photos/card_front.png")
fc_back_image = PhotoImage(file="./photos/card_back.png")
right_button_image = PhotoImage(file="./photos/right.png")
wrong_button_image = PhotoImage(file="./photos/wrong.png")

# Canvas photo
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=fc_back_image)
canvas_title = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text=random_word(), font=("Arial", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button section
right_button = Button(image=right_button_image, highlightthickness=0, width=100,height=100,
                      highlightbackground=BACKGROUND_COLOR,
                      command=key_action)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, width=100,height=100,
                      highlightbackground=BACKGROUND_COLOR,
                      command=key_action)
wrong_button.grid(row=1, column=1)



window.mainloop()

