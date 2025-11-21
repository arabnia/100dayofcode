import tkinter as tk
window = tk.Tk()
window.title("GUI example")
window.minsize(600, 300)
my_label = tk.Label(font=("B Nazanin", 24, "bold"), text="زندگی هنوز زیباست.")
my_label.pack(side="right")


window.mainloop()