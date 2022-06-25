import time
import random
from random_word import RandomWords
import os

randomWord = RandomWords()

stage_1 = """
    +---+
    |   |
        |
        |
        |
        |
    =========
"""
stage_2 = """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
"""
stage_3 = """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
"""
stage_4 = """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
"""
stage_5 = """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
"""
stage_6 = """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |  
    =========
"""
stage_7 = """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
"""

hanging_stages = [stage_1, stage_2, stage_3,
                  stage_4, stage_5, stage_6, stage_7]

print("Welcome to Hangman, by Bookworm-bit!")


def hangman_frame_switcher(word):
    correct_letters = []
    incorrect_letters = []
    hangman_frame = 0
    guessed_letters = []
    partial_word = "_ "  * len(word)

    while True:
        print(hanging_stages[hangman_frame])
        
        guess = input("Guess a letter: ")
        guess = guess.lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        if guess.isalpha() == False:
            print("Please only guess letters.")
        else:
            os.system('cls')
            if guess in word:
                print("Correct!")
                print("-" * 50)

                correct_letters.append(guess)
                guessed_letters.append(guess)

                guess_word_indices = []
                for i in range(len(word)):
                    if guess == word[i]:
                        guess_word_indices.append(i)

                for i in guess_word_indices:
                    partial_word = partial_word[:i] + guess + partial_word[i+1:]

                print(f"Incorrect Letters: {incorrect_letters}")
                print(f"Correct Letters: {correct_letters}")
                print(f"Word: {partial_word}")
            else:
                print("Incorrect!")
                print("-" * 50)
                hangman_frame += 1

                if hangman_frame == 6:
                    print("You lose!")
                    print(f"The word was: {word}")
                    break
                    
                incorrect_letters.append(guess)
                guessed_letters.append(guess)

                print(f"Incorrect Letters: {incorrect_letters}")
                print(f"Correct Letters: {correct_letters}")
                print(f"Word: {partial_word}")

while True:
    hangman_frame_switcher(randomWord.get_random_word())