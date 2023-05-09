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


def game_loop(word, username):
    """
    Function handle the main Game loop.
    Initialize the variables being tracked during game loop
    Then request valid guesses until word is found or out of guesses.
    Finally calls score calculator function.
    """
    hidden_word = []
    for i in range(len(word)):
        if word[i] == " ":
            print("found a space")
            hidden_word.insert(i, " ")
        else:
            hidden_word.insert(i, "_")
    score = 0
    guesses = 10
    guessed = []
    while guesses > 0 and "_" in hidden_word:
        print(f"Guesses left: {guesses}")
        print("Guessed Words:")
        print(*guessed, sep=',')
        print(*hidden_word, sep=" ")
        guess = input("Input letter or guess the word:\n").upper()
        if not (any(char.isdigit() for char in guess)) and (guess not in guessed):
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
                    guessed.append(guess)
                    continue
                else:
                    guessed.append(guess)
                    guesses -= 1
                    continue
            else:
                guessed.append(guess)
                print("Length of guessed word does not match the Hidden Word")
                continue
        elif guess in guessed:
            print(f"You have already guessed {guess} ")
            continue
        else:
            print("No intergers allowed")
    print(f"Word is: {word}")
    score_calculator(score, word, guesses, username)


def score_calculator(score, word, guesses, username):
    """
    Function sets the score depending on parameters
    SCORE for correct guessed letters,
    length of WORD and GUESSES left
    """
    if score == 0:
        print(f"Hangman is definitly not your thing.. Your score is:{score}")
    else:
        score += pow(len(word), guesses)
    print(f"Your final score is:{score}")
    add_to_leaderboard(score, username)
    main_menu()


def add_to_leaderboard(score, username):
    """
    Function takes accuired score and assosicated username
    and adds it to a new row in leaderboards.
    """
    number = len(leaderboard.col_values(1))
    new_row = [number, username, score]
    leaderboard.append_row(new_row)


def show_leaderboard():
    """
    Function prints out current Leaderboard from google spreadsheet
    and awaits enter key press to go back to main menu.
    """
    score_sheet = leaderboard.get_all_values()
    score_head = score_sheet[0]
    score_sheet.pop(0)
    score_sheet.sort(reverse=True, key=lambda l: int(l[2]))
    if len(score_sheet) > 10:
        top_ten = score_sheet[:10]
    else:
        top_ten =score_sheet
    position = 1
    top_ten.insert(0, score_head)
    for row in top_ten:
        if row[0].isalpha():
            print(f"{row[0]:<10} {row[1]:<20} {row[2]}")
            continue
        else:
            row[0] = position
            position += 1
            print(f"{row[0]:<10} {row[1]:<20} {row[2]}")
    input("Press ENTER to get back to Main menu\n")
    main_menu()


def new_game(category):
    """
    Function calls helper function for random word depending
    on the category selected. Then request user to select a
    valid username and call to start.
    Calls game_loop and sends the random word and username through.
    """
    random_word = get_word(category)
    # print(random_word)
    while True:
        username = input("Enter your name:\n")
        if len(username) < 2 or len(username) > 20:
            print("Please enter a valid username longer than "
                  "2 and less than 20 characters!")
            continue
        elif username.isdigit():
            print("Username must include letters!")
            continue
        else:
            break
    input("PRESS ENTER TO START\n")
    game_loop(random_word, username)


def exit_game():
    """
    Helper function to print farwell message
    and exit the game.
    """
    print("Thank you for playing Hangman! Hope to see you again soon!")
    exit()


def main_menu():
    """
    Function displays Main menu waiting for input
    1 to starting a new game
    2 to call function to display Leaderboard
    """
    while True:
        try:
            x = int(input("To start game type 1 or 2 for"
                          "Leaderboards and 3 to exit:\n"))
            if (x == 1):
                print("Starting new game")
                category = int(input("Choose word Category:1 for Animals,"
                                     "2 for Countries, 3 for Foods:\n"))
                break
            elif (x == 2):
                print("Showing the Leaderboard")
                show_leaderboard()
            elif (x == 3):
                while True:
                    exit_condition = str(input("Are you sure?"
                                               "Press y/n:\n")).upper()
                    if (exit_condition == "Y"):
                        exit_game()
                    elif (exit_condition == "N"):
                        break
                    else:
                        print(f"Expected option Y or N. Not:{exit_condition}")
            else:
                print(f"Expected option is 1, 2 or 3. Not:{x}")
        except ValueError:
            print(f"Sorry, a valid option number is expected!")

    new_game(category)


def welcome_message():
    """
    Function gives the initial Welcome message.
    """
    print("Welcome to hangman")
    print("To play, select a category and input your username")
    print("Game rules: type a letter or guess the word")
    print("The few wrong guesses = high score")


welcome_message()
main_menu()
