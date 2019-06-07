import random
import math
import os

os.system("clear")


#Open word file and create a list of them
file = open("words.txt").read()
master_list = file.split()

easy_list = []
medium_list = []
hard_list = []
mystery_word = ""
correct_letters = []
right_letters =""
#print(correct_letters)
current_guesses = []
already_guessed = True
game_over = False
game_input = False
lives = 8
newword=[]

#Make three lists (Easy, Medium, Hard) from the master_list of words
for word in master_list:
    if len(word) >= 4 and len(word) <= 6:
            easy_list.append(word)
    elif len(word) >= 6 and len(word) <= 8:
            medium_list.append(word)
    elif len(word) >= 8:
            hard_list.append(word)


def generate_mystery_word (game_mode):
    if int(game_mode) == 1:
        list_length = len(easy_list)
        selected_word = random.randint(0,list_length)
        mystery_word = easy_list[selected_word]
        mystery_word = mystery_word.upper()

    elif int(game_mode) == 2:
        list_length = len(medium_list)
        selected_word = random.randint(0,list_length)
        mystery_word = medium_list[selected_word]
        mystery_word = mystery_word.upper()
    elif int(game_mode) == 3:
        list_length = len(hard_list)
        selected_word = random.randint(0,list_length)
        mystery_word = hard_list[selected_word]
        mystery_word = mystery_word.upper()

    return mystery_word

#def play_game (mystery_word):
    #guess = input("Guess a letter >>> ")
    #if mystery_word != "":
        #print ("OMG IT WORKS")



def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"


def print_word(word, guesses):
    output_letters = [display_letter(letter, guesses) 
                      for letter in word]
    print(" ".join(output_letters))
    

    
#print_word(word, current_guesses)    

while game_input == False:
    game_mode = input("""Welcome to Mystery Word! Type in the number to select your level of difficulty:
1 - Easy
2 - Medium
3 - Hard
>>> """)

    if game_mode != "1" and game_mode != "2" and game_mode != "3":
        os.system("clear")
        print("That's not a valid selection. Please enter 1, 2, or 3 to select difficulty")
    else:
        
        mystery_word = generate_mystery_word(game_mode)
        game_input = True





x = 0
while x < len(mystery_word):
    if mystery_word[x] not in correct_letters:
        letter = mystery_word[x]
        correct_letters.append(letter)
    x = x + 1


#print (mystery_word)
#print (correct_letters)



#Gameplay loop
while game_over == False:
    already_guessed = True
    os.system("clear")

    while already_guessed == True:
        
        print_word(mystery_word, current_guesses)
        print("**************")
        print("Used Letters:",current_guesses)
        print("Lives:",lives)
        guess_letter = input("Guess a letter: ")
        guess_letter = guess_letter.upper()
        if guess_letter in current_guesses:
            os.system("clear")
            print("You already guessed that letter. Pick again.")
        else:
            os.system("clear")
            print("**************")
            current_guesses.append(guess_letter)
            print_word(mystery_word, current_guesses)
            already_guessed = False
    
            
    #print_word(mystery_word, current_guesses)
    
    if current_guesses[-1] not in correct_letters:
            #breakpoint()
        lives = lives - 1
        already_guessed = True
        os.system("clear")
  
   
    if lives == 0:
        print("You are out of lives. The correct answer is:",mystery_word)
        game_over = True 
        playagain = input("Do you want to play again? Y/N: ")
    

  




