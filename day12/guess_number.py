# this is Guess Number Game
from ascii_art import game_logo, win
import random
# difficulty answer
def diff_ans():
    while True:
        difficulty = input("Choose difficulty, type e for 'easy' or h for 'hard' :  ").lower()
        if difficulty in ("h"):
            return 5
        elif difficulty in ("e"):
            return 10
        else:
            print("You must answer e for 'easy' or h for 'hard' !")

def game():
    """ This is main game function """
    print(game_logo)
    print("Welcom to the number Guessing Game!")
    print("I'm thinking a number between 1 and 100.")
    system_random = random.randrange(1, 100)
    # print(type(system_random))
    print(f"Pssst, the correct answer is {system_random}")
    # choose difficulty
    rmn_gs = diff_ans()
    # print(type(rmn_gs))
    
    while rmn_gs > 0:
        print(f"You have {rmn_gs} attemps remaing to guess number!")
        usr_gs = str
        while not type(usr_gs) == int:
            try:
                usr_gs = int(input("Make a Guess: "))
            except ValueError:
                print("you can input number only")
        if usr_gs > system_random:
            print("Too Big!")
            rmn_gs -= 1
        elif usr_gs < system_random:
            print(f"Too small!")
            rmn_gs -= 1
        elif usr_gs == system_random:
            print(win)
            break
    if rmn_gs == 0:
        print("You lose!, maybe try again!")

game()
