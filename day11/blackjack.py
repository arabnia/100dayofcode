############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 15, 15]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import os
from art import logo

def deal():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate(player_deal):
    if sum(player_deal) == 21 and len(player_deal) == 2 :
        return 0
    elif sum(player_deal) > 21 and 11 in player_deal:
        player_deal.remove(11)
        player_deal.append(1)
    return sum(player_deal)
        
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

    
def game():
    print(logo)

    user_deal = []
    computer_deal = []
    for i in range(2):
        user_deal.append(deal())
        computer_deal.append(deal())
    game_end = False
    while not game_end:
        user_score = calculate(user_deal)
        computer_score = calculate(computer_deal)
        print(f"   Your cards: {user_deal}, current score: {user_score}")
        print(f"   Computer's first card: {computer_deal[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_deal.append(deal())
            else:
                game_end = True
    while computer_score != 0 and computer_score < 17:
        computer_deal.append(deal())
        computer_score = calculate(computer_deal)        
    print(f"   Your final hand: {user_deal}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_deal}, final score: {computer_score}")
    print(compare(user_score, computer_score))
  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("clear")
    game()

