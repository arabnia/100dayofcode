import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Simple Tkinter Example")

# Set the window size
root.geometry("300x200")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)  # Add some padding around the label

# Create a button widget
button = tk.Button(root, text="Click Me", command=lambda: print("Button Clicked"))
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
