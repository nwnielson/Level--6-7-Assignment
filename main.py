import wordle_functions

# Variables
guesses = 6
keep_playing = True
random_word = ""
user_word = "1"
previous_guesses = []

# Welcome Player
print(f"\nWelcome to Poorman's Wordle! \n\nGuess the five-letter word. \n\nG = correct letter and position \n\
Y = correct letter, wrong position \n- = letter is not in the word")

# Runs as long as the player agrees to
while (keep_playing == True) :
    random_word = wordle_functions.choose_word()
    
    # Runs if there are guesses remaining, and word hasn't been guessed
    while guesses > 0 and user_word != random_word.upper():
        print(f"\nGuesses remaining: {guesses}")
        user_word = wordle_functions.get_guess()
        
        # Checks if word has been guessed before. If so, ask for new input
        if user_word not in previous_guesses :
            feedback = wordle_functions.evaluate_guess(user_word, random_word)
            wordle_functions.display_guess(feedback, user_word)
            guesses -= 1
            # Adds guess to list of guesses
            previous_guesses.append(user_word)
        else :
            print("You already guessed that. Guess again.")
    
    keep_playing = wordle_functions.has_won(user_word, random_word)
    guesses = 6
    previous_guesses = []
    user_word = "1"
