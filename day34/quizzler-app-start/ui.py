THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *

class AppInterface():
    def __init__(self, quiz_obj: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_obj
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.true_icon = PhotoImage(file="images/true.png")
        self.false_icon = PhotoImage(file="images/false.png")
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,width=290, text="", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=3)
        self.true_button = Button(image=self.true_icon, highlightthickness=0, width=100,height=100,
                      highlightbackground=THEME_COLOR, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=1, padx=20, pady=20)
        self.false_button = Button(image=self.false_icon, highlightthickness=0, width=100,height=100,
                                   highlightbackground=THEME_COLOR, bg=THEME_COLOR)
        self.false_button.grid(row=2, column=2, padx=20, pady=20)
        self.score = Label(text="score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "italic"))
        self.score.grid(row=0, column=2, padx=20, pady=20)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)