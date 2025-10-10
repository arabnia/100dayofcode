import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected")

if __name__ == "__main__":
    open_file_dialog()
