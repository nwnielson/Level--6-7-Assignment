import random

# Selects and returns a random word.
def choose_word() :
    #A list of real 5-letter words
    word_list = [
    "flour", "grape", "house", "train", "beach", "smart", "cloud",
    "brick", "plane", "water", "night", "stone", "dream", "flame",
    "brush", "chair", "lunch", "paint", "money", "ghost", "black",
    "crane", "pearl", "shirt", "blind", "think", "bread", "fruit",
    "dance", "horse", "mouse", "sugar", "table", "woman", "spice",
    "quiet", "glove", "voice", "jumpy", "knife", "plant", "blame",
    "spoil", "whale", "north", "giant", "flask", "drive", "lemon",
    "pilot"
    ]

    # Picks one word randomly from the list
    random_word = random.choice(word_list)

    return random_word

# Gets and validates the player’s guess.
def get_guess(previous_guesses) :
    guess = input("Guess: ").upper()
    
    # Makes sure guess is the right length and hasn't been guessed yet
    if (len(guess) == 5) and (guess not in previous_guesses) :
        return guess
    
    # Raises exception to get another guess if has been guessed
    elif guess in previous_guesses :
        print("You already guessed that. Guess again.")
        raise ValueError
    
    # Raises exception to get another guess if guess != 5 characters long
    else :
        print("Input must be exactly 5 characters long. Guess again. ")
        raise ValueError

# Compares the guess with the secret word and returns feedback.
def evaluate_guess(guess, random_word) :
    
    # Lists to split the guesses into, and one to store the # of correct answers
    user_letters = [] 
    random_letters = []
    feedback = []
    
    # Separates words into lists
    for letters in guess :
        user_letters.append(letters)
    for letters in random_word :
        random_letters.append(letters.upper())
        
    # Check for green and yellow letters
    for u_letters in range(len(user_letters)) :
        letter_added = False
        
        for r_letters in range(len(random_letters)) :
            
            # Checks if letter from first loop is same as letter in second loop
            if user_letters[u_letters] == random_letters[r_letters] :
                
                # Checks if matching letters are from the same index. If so, appends G to feedback
                if user_letters[u_letters] == random_letters[u_letters] :
                    feedback.append("G")
                    letter_added = True
                # If not, append Y to feedback
                else :
                    feedback.append("Y")
                    letter_added = True
            
        # If not G or Y, append - to feedback
        if not letter_added :
            feedback.append("-")
            
    return feedback

# Displays the guess and its feedback.
def display_guess(feedback, guess) :
    # Prints user guess
    print(f"\nYour Guess: {guess[0]} {guess[1]} {guess[2]} {guess[3]} {guess[4]}")
    # Prints feedback
    print(f"Feedback:   {feedback[0]} {feedback[1]} {feedback[2]} {feedback[3]} {feedback[4]}")

# Determines whether the player has guessed the word.
def has_won(guess, random_word) :
    # Checks if guess matches random_word (win condition). If so, ends loop
    if guess == random_word.upper() :
        print("\nCongratulations! You won!\n")
        keep_playing = True
    else:
        keep_playing = False
        print("\nSorry, you lost.")
        print(f"The correct answer was: {random_word}\n")
        
    # Gets input if user wants to play again.
    play_again = input("Would you like to play again? Yes or no? ").upper()
    while play_again not in ("YES", "NO") :
        play_again = input("Yes and no are all I know. Please enter yes or no. ").upper()
    if play_again == "YES" :
        return True
    elif play_again == "NO" :
        print("Thanks for playing!")
        return False
        