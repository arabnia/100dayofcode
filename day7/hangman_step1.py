import random
# This is leven 1 of hangman Game!
word_list = ["ardvark", "baboon", "camel"]
# TODO-1 - Random select word and assign it to chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign it to variable called guess . make it lower case! 
guess = input("plz guess a word!: ").lower()

# TODO-3 - Check if the letter the use guessed is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")