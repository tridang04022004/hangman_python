import string
from words import words
from random import *

def getWord():
    word = choice(words).strip().upper()
    return word

def hangman():
    word = getWord()
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)

    lives = 5

    while len(word_letters) > 0 and lives > 0:

        print("You have ", lives, "lives left | You have already guessed these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Enter a letter: ").upper()
        if len(user_letter) == 1 and user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("You guessed the wrong letter!")

        elif len(user_letter) == 1 and user_letter in used_letters:
            print("You have already guessed that letter.")

        else:
            print("Invalid letter.")

    if lives == 0:
        print("You lost! The word was: ", word)
    else:
        print("You win! The word was: ", word)

hangman()












