import wordle_functions

# Variables
guesses = 6
keep_playing = True
random_word = ""
guess = "1"
previous_guesses = []

# Welcome Player
print(f"\nWelcome to Poorman's Wordle! \n\nGuess the five-letter word. \n\nG = correct letter and position \n\
Y = correct letter, wrong position \n- = letter is not in the word")

# Runs as long as the player agrees to play
while (keep_playing == True) :
    
    random_word = wordle_functions.choose_word()
    
    # Runs if there are guesses remaining, and word hasn't been guessed
    while guesses > 0 and guess != random_word.upper():
        
        # Tries to get guess and display feedback
        try :
            print(f"\nGuesses remaining: {guesses}")
            guess = wordle_functions.get_guess()
            feedback = wordle_functions.evaluate_guess(guess, random_word, previous_guesses)
        
        # Runs if guess != 5 characters or guess has already been guessed
        except ValueError:
            continue
        
        # Runs if rando error happens, restarts game.
        except :
            print("Unknown error. Restarting game.")
            guesses = 6
            previous_guesses = []
            guess = "1"
            continue
        
        # Runs if no errors and word is valid
        else :

            wordle_functions.display_guess(feedback, guess)
            guesses -= 1
            # Adds guess to list of guesses
            previous_guesses.append(guess)
            
    # Resets values after every game.
    keep_playing = wordle_functions.has_won(guess, random_word)
    guesses = 6
    previous_guesses = []
    guess = "1"
