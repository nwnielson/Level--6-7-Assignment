"""
choose_word() – Selects and returns a secret word.
• get_guess() – Gets and validates the player’s guess.
• evaluate_guess() – Compares the guess with the secret word and returns feedback.
• display_guess() – Displays the guess and its feedback.
• has_won() – Determines whether the player has guessed the word.
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
    print(random_word)

    return random_word

def get_guess() :
    user_word = input("Guess: ").upper()
    if (len(user_word) == 5) :
        return user_word
    else :
        print("Only 5 letter word guesses please. Guess again.")
        get_guess()
        

def evaluate_guess(user_word, random_word) :
    user_letters = [] 
    random_letters = []
    correct_letters = []
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
                
                # Checks if matching letters are from the same index
                if user_letters[u_letters] == random_letters[u_letters] :
                    correct_letters.append("G")
                    letter_added = True
                else :
                    correct_letters.append("Y")
                    letter_added = True
            
        # If not G or Y, add -
        if not letter_added :
            correct_letters.append("-")
            
    return correct_letters
        
    """# Check for green and yellow letters
            for index, u_letters in enumerate(user_letters) :
                letter_added = False
                for r_letters in random_letters :
                    if u_letters == r_letters :
                        print(u_letters, random_letters[index])
                        if u_letters == random_letters[index] :
                            correct_letters.append(" G ")
                            print(u_letters, random_letters[index])
                            letter_added = True
                        else :
                            print(u_letters, random_letters[index])
                            correct_letters.append(" Y ")
                            letter_added = True
                if not letter_added :
                    print(u_letters, random_letters[index])
                    correct_letters.append(" - ")
            return correct_letters"""
    """
    # Check for green and yellow letters
       for r_letters in random_letters :
           letter_added = False
           for index, u_letters in enumerate(user_letters) :
               if u_letters == r_letters :
                   print(r_letters, user_letters[index])
                   if r_letters == user_letters[index] :
                       correct_letters.append(" G ")
                       print(u_letters, random_letters[index])
                       letter_added = True
                   else :
                       print(u_letters, random_letters[index])
                       correct_letters.append(" Y ")
                       letter_added = True
           if not letter_added :
               print(print(r_letters, random_letters[index]))
               correct_letters.append(" - ")
       return correct_letters
   """
   
            
                    
            
    
    #Checks for yellow letters
        
    



def display_guess(correct_letters, user_word) :
    print(f"\nYour Guess: {user_word[0]} {user_word[1]} {user_word[2]} {user_word[3]} {user_word[4]}")
    print(f"Feedback:   {correct_letters[0]} {correct_letters[1]} {correct_letters[2]} {correct_letters[3]} {correct_letters[4]}")
        
    



def has_won(user_word, random_word) :
    if user_word == random_word.upper() :
        print("\nCongratulations! You won!")
        keep_playing = True
    else:
        keep_playing = False
        print("Sorry, you lost.")
        
    play_again = input("Would you like to play again? Yes or no? ").upper()
    if play_again == "YES" :
        return True
    elif play_again == "NO" :
        print("Thanks for playing!")
        return False
    else :
        print("Please enter yes or no.")
        has_won
