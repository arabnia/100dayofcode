from tkinter import *
window = Tk()
window.title("GUI example")
window.minsize(600, 300)
header = Label(window, text="First text")
header.pack()
def submit_button():
    in_func_var = box_test.get()
    box_test.delete(0, END)
    header.config(text=in_func_var)

button = Button(window, text="button", command=submit_button)
button.pack()
box_test = Entry()
box_test.pack()



window.mainloop()