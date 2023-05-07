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
    print(word)
    hidden_word = []
    for i in range(len(word)):
        hidden_word.insert(i, "_")
    print(*hidden_word, sep = " ")
    guesses = 10
    guessed = []
    while guesses > 0 and "_" in hidden_word:
        guess = input("Input letter or guess the word")
        if guess.isalpha() and not in guessed:
            if len(guess) == len(word):
                if guess == word:
                    break
                else:
                    guessed.append(guess)
                    guesses -= 1
                    continue
            elif len(guess) == 1:
                if guess in word:
                    for i in len(word):
                        word.index(guess)
                    


            else:
                print("Length of guessed word does not match the Hidden Word")
                guesses -= 1
                continue
        



        



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