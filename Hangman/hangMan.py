import random
import string
from Word import words


def get_a_valid_word(words):
    word = random.choice(words)
    while "-" and " " in words:
        word = random.choice(words)

    return word


def hangMan():
    word = get_a_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_Letter = set()

    # getting user input
    user_Letter = input("Guess a letter").upper()
    if user_Letter in alphabet - used_Letter:
        used_Letter.__add__(user_Letter)
        if user_Letter in word_letters:
            word_letters.remove(user_Letter)

    elif user_Letter in used_Letter:
        print("You have already used that character, Please try again")

    else:
        print("Invalid")
