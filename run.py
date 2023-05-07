# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from words import *

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Leaderboard')

leaderboard = SHEET.worksheet('Leaderboard')
def game_loop(word):
    print("welcome to game loop")
    while True:
        username = input("Enter your name:")
        if len(username) == 0:
            print("Please enter a username!")
            continue
        elif username.isdigit():
            print("Username must include letters!") 
            continue
        else:
            break
    input("PRESS ANYTHING TO START")
    hidden_word = []
    for i in range(len(word)):
        hidden_word.insert(i, "_")
    score = 0
    guesses = 10
    guessed = []
    while guesses > 0 and "_" in hidden_word:
        print(f"Guesses left: {guesses}")
        print("Guessed Words:")
        print(*guessed, sep = ',')
        print(*hidden_word, sep = " ")
        guess = input("Input letter or guess the word:").upper()
        if guess.isalpha() and guess not in guessed:
            if len(guess) == len(word):
                if guess == word:
                    score += 500
                    break
                else:
                    guessed.append(guess)
                    guesses -= 1
                    continue
            elif len(guess) == 1:
                if guess in word:
                    for i in range(len(word)):
                        if guess == word[i]:
                            hidden_word[i] = guess
                            score += 50
                    continue
                else:
                    guessed.append(guess)
                    guesses -= 1
                    continue

            else:
                print("Length of guessed word does not match the Hidden Word")
                guesses -= 1
                guessed.append(guess)
                continue
        elif guess in guessed:
            print(f"You have already guessed {guess} ")
            continue
        else:
            print("No intergers allowed")
    print(f"Word is: {word}")
    set_score(score, word, guesses)
    
def set_score(score, word, guesses):
    if score == 0:
        print("Too bad, you are a hung one")
    #elif len(word) < 5:
        #score += pow(len(word),guesses)
    #elif len(word) > 7:
        #score += (guesses*200)
    #elif guesses > 8:
        #score += (guesses*300)
    else:
        score += pow(len(word),guesses)
    print(f"Your final score is:{score}")



def main_menu():
    while True:
        try:
            x = int(input("To start game type 1 or 2 to check the Leaderboards:"))
            print(x)
            if(x == 1):
                print("start game")
                category = int(input("Choose word Category:1 for animals, 2 for countries, 3 for "))
                random_word = get_word(category)
                print(random_word)
                break
            elif(x == 2):
                print(leaderboard)
            else:
                print("Expected value is 1 or 2")
        except ValueError:
            print('I said: Tell me a NUMBER!')
    
    game_loop(random_word)
        #raise Exception("Sorry, input should be 1 or 2")

def welcome_message():
    print("Welcome to hangman")
    print("To play, enter a letter or guess the word")

welcome_message()
main_menu()