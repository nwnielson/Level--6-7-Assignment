"""
choose_word() – Selects and returns a secret word.
• get_guess() – Gets and validates the player’s guess.
"""

"""

2. Select a secret five-letter word.




"""
import random



def choose_word() :
    #A list of real 5-letter words
    word_list = ["apple", "grape", "house", "train", "beach", "smart", "clock"]

    # Picks one word randomly from the list
    random_word = random.choice(word_list)

    return random_word

def get_guess() :
    user_word = input("Guess: ").upper()
    # Makes sure guess is the right length
    if (len(user_word) == 5) :
        return user_word
    else :
        print("\nOnly 5 letter word guesses please. Guess again.")
        get_guess()
        

def evaluate_guess(user_word, random_word) :
    # Lists to split the guesses into, and one to store the # of correct answers
    user_letters = [] 
    random_letters = []
    feedback = []
    
    # Separates words into lists
    for letters in user_word :
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
        

def display_guess(feedback, user_word) :
    # Prints user guess
    print(f"\nYour Guess: {user_word[0]} {user_word[1]} {user_word[2]} {user_word[3]} {user_word[4]}")
    # Prints feedback
    print(f"Feedback:   {feedback[0]} {feedback[1]} {feedback[2]} {feedback[3]} {feedback[4]}")
        
    

def has_won(user_word, random_word) :
    # Checks if user_word matches random_word (win condition). If so, ends loop
    if user_word == random_word.upper() :
        print("\nCongratulations! You won!\n")
        keep_playing = True
    else:
        keep_playing = False
        print("\nSorry, you lost.")
        print(f"The correct answer was: {random_word}\n")
        
    # Gets input if user wants to play again.
    play_again = input("Would you like to play again? Yes or no? ").upper()
    if play_again == "YES" :
        return True
    elif play_again == "NO" :
        print("Thanks for playing!")
        return False
    else :
        print("Please enter yes or no.")
        has_won