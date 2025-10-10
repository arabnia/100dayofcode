import random
end_of_game = False
from word_list import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Set 'lives' to equal 6.
lives = 6

# load logo
from hangman_art import logo
print(logo[0])

#load stages
from hangman_art import stages

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    if guess in display:
        print("")
        print(f"You've already guess {guess}")
        print("".join(display))
    elif guess in chosen_word:
        print("")
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(" ".join(display))
    else:
        print(f"You guess {guess}, that's not in word, you lose a life!")
        if lives > 0:
            print(stages[lives])
            lives -= 1
        else:
            end_of_game = True
            print(stages[lives])
            print("you lose!")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
