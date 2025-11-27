from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from sqlalchemy.orm import joinedload


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    nr_letters = random.randint(5, 7)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for n in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for n in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for n in range(nr_numbers)]
    random.shuffle(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(password_list))
    pyperclip.copy(password_var.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data_dict = {
        website_var.get(): {
            "email": email_username_entry.get(),
            "password": password_entry.get(),
        }
    }
    if len(website_var.get()) == 0 or len(email_username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        if messagebox.askokcancel("Quit", f"password {password_entry.get()} for website {website_entry.get()} will be saved\n you want to save or quit?"):
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(data_dict)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(data_dict, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    # file.write(f"{website_var.get()} | {email_username_entry.get()} | {password_entry.get()}\n")
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ------------------------ Search Function -----------------------------#
def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(data[website_entry.get()], f"Email: {data[website_entry.get()]["email"]}\n Password: {data[website_entry.get()]["password"]}")
    except KeyError:
        messagebox.showerror("Error", "No data found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
lock_logo = PhotoImage(file="lock_icon.png")
# canvas photo import
canvas = Canvas(height=200, width=200)
canvas.create_image(100,100,image=lock_logo)
canvas.grid(row=0, column=1)
# Label section
website = Label(text="Website:")
website.grid(row=1, column=0)
Email_Username = Label(text="Email/Username:")
Email_Username.grid(row=2, column=0)
Password = Label(text="Password:")
Password.grid(row=3, column=0)

# generate password button
genpass_button = Button(text="Generate Password", command=password_generator)
genpass_button.grid(row=3, column=2)

# generate password config
# configpass_button = Button(text="⚙")
# configpass_button.grid(row=3, column=4)

# Entry section
website_var = StringVar()
website_entry = Entry(width=21, textvariable=website_var)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_var = StringVar()
email_username_entry = Entry(width=38, textvariable=email_var)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "hoseinarabnia@gmail.com")

password_var = StringVar()
password_entry = Entry(width=21, textvariable=password_var)
password_entry.grid(row=3, column=1)
# add button
add_button = Button(text="Add", width=36, command=save) # command=add_button)
add_button.grid(row=4, column=1, columnspan=2)
# search button
search_button = Button(text="Search", command=search, width=13)
search_button.grid(row=1, column=2)

window.mainloop()