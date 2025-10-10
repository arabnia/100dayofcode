# This app is for rock, paper & scissors 
# Rock Paper Scissors ASCII Art

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import random
op = ["paper", "rock", "scissors"]

user_ch = input ("Plz input your choice!\n \nfor Paper press 1 & for Rock press 2 & for Scissors press 3: ")

mc = random.choice(op)
print("so, your choise is:\n")

if user_ch == "1":
    print(paper)
    if mc == "paper":
        print(f"computer choise is:\n{paper}")
        print("both are equal!")
    elif mc == "rock":
        print(f"computer choise is:\n{rock}")
        print("you win!")
    elif mc == "scissors":
        print(f"computer choise is:\n{scissors}")
        print("you lose!")
elif user_ch == "2":
    print(rock)
    if mc == "rock":
        print(f"computer choise is:\n{rock}")
        print("both are equal!")
    elif mc == "scissors":
        print(f"computer choise is:\n{scissors}")
        print("you win!")
    elif mc == "paper":
        print(f"computer choise is:\n{paper}")
        print("you lose!")
elif user_ch == "3":
    print(scissors)
    if mc == "scissors":
        print(f"computer choise is:\n{scissors}")
        print("both are equal!")
    elif mc == "paper":
        print(f"computer choise is:\n{paper}")
        print("you win!")
    elif mc == "rock":
        print(f"computer choise is:\n{rock}")
        print("you lose!")
