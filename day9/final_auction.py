import os

from art import auction_logo
print(auction_logo)
print("Welcome to the secret action Program!")

user_bid = {}
def add_user():
    username = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    user_bid[username] = bid
    # print(user_bid)

def compare(users_dict):
    print(max(users_dict.values()))

def resum_app():
    while True:
        ans = input(f"Are there any other bidders? yes or no:\n").lower()
        if ans in ( "yes" , "no", "n", "y"):
            return ans
        else:
            print("You must answer yes or no ")

continue_auction = 1 
while continue_auction:
    add_user()
    ans = resum_app()
    if ans == "no":
        compare(user_bid)
        continue_auction = 0
    else:
        os.system('clear')