"""Import your functions from wordle_functions.py into main.py.
• Use a list to store previous guesses.
• Use meaningful variable and function names.
• Include comments explaining important sections.
• Do not use classes or advanced Python features we have not discussed."""

"""
1. Welcome the player.

3. Give the player up to six guesses.
4. Require each guess to contain exactly five letters.
5. Reject guesses that have already been used.
6. Display feedback after every guess.
7. Tell the player when a letter is correct, misplaced, or absent.
8. End the game when the player guesses the word or uses all six attempts.
9. Display the secret word if the player loses.
10. Ask whether the player would like to play again.
"""

import wordle_functions

guesses = 6
keep_playing = True
random_word = ""
user_word = "1"

# Welcome Player
print(f"Welcome to Poorman's Wordle! \n\nGuess the five-letter word. \n\nG = correct letter and position \n\
Y = correct letter, wrong position \n- = letter is not in the word")


while (keep_playing == True) :
    random_word = wordle_functions.choose_word()
    
    while guesses > 0 and user_word != random_word.upper():
        print(f"\nGuesses remaining: {guesses}")
        user_word = wordle_functions.get_guess()
        correct_letters = wordle_functions.evaluate_guess(user_word, random_word)
        wordle_functions.display_guess(correct_letters, user_word)
        guesses -= 1
        user_word = ""
    
    keep_playing = wordle_functions.has_won(user_word, random_word)
    guesses = 6

        



