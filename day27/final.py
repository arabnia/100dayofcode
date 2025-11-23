from tkinter import *

window = Tk()
window.title("mile to km converter")
window.minsize(250, 90)

input_var = StringVar()
input_box = Entry(width=10, textvariable=input_var)
input_box.insert(END, "1")
input_box.grid(row=0, column=2)


label_mile = Label(window, text="Mile")
label_mile.grid(row=0, column=3)
label_equal = Label(window, text="is equal to ")
label_equal.grid(row=2, column=1)
label_quantity = Label(text="1.60934")
label_quantity.grid(row=2, column=2)
label_km = Label(window, text="Km")
label_km.grid(row=2, column=3)
def calculate(*args):
    try:
        new_value = float(input_var.get()) * 1.60934
        label_quantity.config(text=str(new_value))
    except ValueError:
        label_quantity.config(text=str(""))

input_var.trace_add("write", calculate)

# button = Button(window, text="calculate", command=calculate)
# button.grid(row=3, column=2)


window.mainloop()