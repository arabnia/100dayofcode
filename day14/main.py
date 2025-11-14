from art import logo, vs
from game_data import data
import random
import os
def rand_celeb ():
    return random.choice(data)

def ans():
    while True:
        ans = input("Who has more followers? Type 'A' or 'B': ").lower()
        if ans in ("a","b"):
            return ans
        else:
            print("You must answer in A or B only!")


def play_game():
    first_A = rand_celeb()
    second_B = rand_celeb()
    score = 0
    while True:
        os.system("clear")
        print(logo)
        # score()
        if score != 0:
            print(f"That's correct!, your score is {score}")
        print(f'Compare A: {first_A["name"]}, a {first_A["description"]}, from {first_A["country"]}')
        print(vs)
        print(f'against B: {second_B["name"]}, a {second_B["description"]}, from {second_B["country"]}')
        # print(type(first_A["follower_count"]))
        get_ans = ans()
        if first_A["follower_count"] > second_B["follower_count"] and get_ans == "a":
            first_A = second_B
            second_B = rand_celeb()
            score += 1
        elif first_A["follower_count"] < second_B["follower_count"] and get_ans == "b":
            first_A = second_B
            second_B = rand_celeb()
            score += 1
        else:
            print("its wrong!")
            break
    os.system("clear")
    print(logo)
    print(f"Sorry, that's wrong!, your final score is {score}")

play_game()