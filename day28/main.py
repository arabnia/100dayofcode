from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer(seconds):
    count_down(seconds)

def timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        start_timer(long_break_sec)
        reps = 0
        count_down(short_break_sec)
    elif reps % 2 == 1:
        start_timer(short_break_sec)
        checksign_label.config(text=f"{reps * "✓"}")
    else:
        start_timer(work_sec)
        checksign_label.config(text=f"{reps * "✓"}")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = math.floor(count % 60)
    canvas.itemconfig(canvas_text, text=f"{count_minutes:02d}:{count_seconds:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=80, bg=YELLOW)
# Timer label
timer_label = Label(window, text="Timer",bg=YELLOW,fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=1, column=2)
# tomato photo
image = PhotoImage(file="pomodo.png")
canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,130, image=image)
canvas_text = canvas.create_text(100,150, text="00:00", font=(FONT_NAME, 28, "bold"), fill="white")
canvas.grid(row=2, column=2)

# start and reset button
start_button = Button(text="start", font=(FONT_NAME, 10 ,"bold"),highlightbackground=YELLOW, command=timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="reset", font=(FONT_NAME, 10 ,"bold"), highlightbackground=YELLOW)
reset_button.grid(row=3, column=3)
# check sign label
checksign_label = Label(text="",bg=YELLOW,fg=GREEN, font=(FONT_NAME, 30, "bold"))

checksign_label.grid(row=4, column=2)
window.mainloop()