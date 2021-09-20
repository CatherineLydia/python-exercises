import random
from os import system, name

stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
''', '''
    +---+
    |   |
    O   |
        |
        |
        |
=========
''', '''
    +---+
    |   |
        |
        |
        |
        |
=========
''']
game_name = '''
    _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/       
'''


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

easy_level = ['apple', 'bat', 'tree', 'snow']
medium_level = ['skate', 'hockey', 'cowboy']
hard_level = ['dominoes', 'roller blading', 'electricity']
play_game = True
total_play = 0
correct_word = 0
print(game_name)
username = input("What is you name:").title()

while play_game :
    total_play +=1
    clear()
    game_completed = False
    lives = len(stages) - 1
    display = []
    wrong_guess=[]

    print(game_name)

    print(f"Welcome!!! {username}\n")

    while True:
        print("1.Easy")
        print("2.Medium")
        print("3.Hard")
        game_level = input("Type number to select a level : ")
        
        if game_level == "1":
            chosen_word = random.choice(easy_level)
            selected_level="EASY"
            break
        elif game_level == "2":
            chosen_word = random.choice(medium_level)
            selected_level = "MEDIUM"
            break
        elif game_level == "3":
            chosen_word = random.choice(hard_level)
            selected_level = "HARD"
            break
        else:
            print("Enter a valid input number.\n")

    word_length=len(chosen_word)

    for letter in chosen_word:
        if letter != ' ':
            display += "_"
        else:
            display +=" "
        

    clear()

    print(game_name)

    print(f"LEVEL  : {selected_level}\n")

    print(f"{' '.join(display)}\n")

    while not game_completed:
        guess =(input("\nGuess a letter .... ")).lower()
        
        clear()

        if guess in display:
            print(f"You've already guessed '{guess}'.\n")
        else:
            no_occur = 0
            for pos in range(word_length):
                letter = chosen_word[pos]
                if letter == guess:
                    display[pos] = letter
                    no_occur +=1
            if no_occur == 1:
                print(f"\nHooray !!! Your guess '{guess}' is in the word.\n")
            elif no_occur > 1 :
                print(f"\nHooray !!! Your guess '{guess}' appears {no_occur} times in the word.\n")

        
        
        if guess not in chosen_word:
            
            if guess not in wrong_guess:
                wrong_guess.append(guess)
                lives -= 1
                print(f"\nYour guess '{guess}' is not in the word. You lose a life.")
            else:
                if(selected_level == "EASY"):
                    print(
                        f"\nYour guess '{guess}' is not in the word.")
                else:
                    lives -= 1
                    print(f"\nYour guess '{guess}' is not in the word. You lose a life.")
            
            if lives == 0:
                game_completed= True
                status="LOSE"

        print(f"\n{' '.join(display)}")

        if not "_" in display:
            game_completed = True
            status="WIN"
            correct_word +=1

        print(stages[lives])
        print(f"\nLIVES LEFT : {lives}")

        if selected_level != "HARD" or len(wrong_guess) !=0 :
            print(f"\nWrong Guesses : {' ,'.join(wrong_guess)}\n")

    if status == "WIN" :
        print("\nCongratulations!!! YOU WIN !!!")
    elif status == "LOSE":
        print(f"\nYOU LOSE !!! \nThe word is {(chosen_word).title()}")

    while True:
        option=input("\nDo you want to play again ? Type 'y' for yes or 'n' for no :" ).lower()

        if(option == 'y'):
            play_game = True
            break
        elif(option == 'n'):
            clear()
            print(game_name)
            print(f"\nYou have played {total_play} games.\n\nCORRECT GUESS : {correct_word}\n\nWRONG GUESS : {(total_play - correct_word)}")
            print(f"\n\nGoodBye!!! {username}\n")
            play_game = False
            break
        else:
            print("Invalid input.")



