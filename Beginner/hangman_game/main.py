import random
from os import system, name
from image import game_name,stages
from word_list import easy_level,medium_level,hard_level


def clear():
    """Clears the screen"""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def game_level_select():
    """User can select from EASY,MEDIUM,HARD LEVEL.
    Once user selects the level, a random word 'chosen_word' is selected from that level's word list.
    It returns the chosen_word and selected LEVEL"""

    level=[]
    # Game Level Selection 
    while True:
        print("1.Easy")
        print("2.Medium")
        print("3.Hard")
        game_level = input("Type number to select a level : ")

        if game_level == "1":
            chosen_word = random.choice(easy_level)
            level.append(chosen_word)
            selected_level = "EASY"
            level.append(selected_level)
            return level
        elif game_level == "2":
            chosen_word = random.choice(medium_level)
            level.append(chosen_word)
            selected_level = "MEDIUM"
            level.append(selected_level)
            return level
        elif game_level == "3":
            chosen_word = random.choice(hard_level)
            level.append(chosen_word)
            selected_level = "HARD"
            level.append(selected_level)
            return level
        else:
            print("Enter a valid input number.\n")

def guess_game(chosen_word,display):
    """User can guess a letter in the word until all lives are lost.
    User guess is correct, it is displayed in the screen. 
    User guess is wrong,loses a life."""
    
    game_completed= False
    lives = len(stages) - 1
    wrong_guess = []

    while not game_completed:
        # Prompts user to guess a letter
        while True:
            guess = (input("\nGuess a letter .... ")).lower()
            if(len(guess) == 0):
                print("Invalid input.Enter an input.")
            elif(len(guess) > 1):
                print("Invalid input.Enter only one character.")
            elif(not guess.isalpha()):
                print("Invalid input.Enter only alphabets.")
            elif(len(guess)==1 and guess.isalpha()):
                break

        clear()
        
        # If user already guessed it correct 
        if guess in display:
            print(f"You've already guessed '{guess}'.\n")
        # If user guessed letter is in the word
        else:
            # no_occur keeps track number of occurences of the guessed letter in the word.
            no_occur = 0
            for pos in range(word_length):
                letter = chosen_word[pos]
                if letter == guess:
                    display[pos] = letter
                    no_occur += 1
            if no_occur == 1:
                print(f"\nHooray !!! Your guess '{guess}' is in the word.\n")
            elif no_occur > 1:
                print(
                    f"\nHooray !!! Your guess '{guess}' appears {no_occur} times in the word.\n")

        # If user guessed letter is not in the word
        if guess not in chosen_word:
            # wrong_guess keeps track of all wrongly guessed letters
            if guess not in wrong_guess:
                wrong_guess.append(guess)
                lives -= 1
                print(f"\nYour guess '{guess}' is not in the word. You lose a life.")
            else:
                # 
                if(selected_level == "EASY"):
                    print(f"\nYour guess '{guess}' is not in the word.")
                else:
                    lives -= 1
                    print(
                        f"\nYour guess '{guess}' is not in the word. You lose a life.")
            # If user loses all lives
            if lives == 0:
                game_completed = True
                status = "LOSE"

        print(f"\n{' '.join(display)}")
        # Checks whether all letters are guessed correct
        if not "_" in display:
            game_completed = True
            status = "WIN"
            
        # Prints Hangman Stages to display remaining lives
        print(stages[lives])
        print(f"\nLIVES LEFT : {lives}")
        # Display Wrong guess letters for users, only for "EASY" and "MEDIUM" level
        if selected_level != "HARD":
            print(f"\nWrong Guesses : {' ,'.join(wrong_guess)}\n")

    return status


def continue_game():
    """ Whether user wants to continue playing game"""

    global total_play,username,correct_word
    while True:
        option = input("\nDo you want to play again ? Type 'y' for yes or 'n' for no :").lower()
        # User wants to continue playing
        if(option == 'y'):
            return True
        # User wants to exit the game
        elif(option == 'n'):
            clear()
            print(game_name)
            print(f"\nYou have played {total_play} games.\n\nCORRECT GUESS : {correct_word}\n\nWRONG GUESS : {(total_play - correct_word)}")
            print(f"\n\nGoodBye!!! {username}\n")
            return False
        else:
            print("Invalid input.")



play_game = True
total_play = 0
correct_word = 0
print(game_name)
username = input("What is you name:").title()

while play_game:

    total_play += 1
    clear()
    
    display = []
    
    print(game_name)

    print(f"Welcome!!! {username}\n")

    level=game_level_select()
    chosen_word=level[0]
    selected_level=level[1]

    word_length = len(chosen_word)
    # display holds _ for number of letters in the chosen_word
    for letter in chosen_word:
        if letter != ' ':
            display += "_"
        else:
            display += " "

    clear()

    print(game_name)

    print(f"LEVEL  : {selected_level}\n")

    print(f"{' '.join(display)}\n")

    status = guess_game(chosen_word,display)

    if status == "WIN":
        print("\nCongratulations!!! YOU WIN !!!")
        correct_word +=1
    elif status == "LOSE":
        print(f"\nYOU LOSE !!! \nThe word is {(chosen_word).title()}")

    play_game=continue_game()
