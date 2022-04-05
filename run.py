"""True or False Quiz Game"""
# import os
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from info import welcome_message
from info import rules
from info import choices
from info import game_choice
from validate import User


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('true_false')

data = SHEET.worksheet('scores')


# def validate_choice(choices):
#     """
#     Inside the try, converts all values into lowercase.
#     """

#     if choices != 'a' or 'b' or 'c' or 'd':
#             raise ValueError(
#                 f"That is not a valid answer, you must chose either a,
#               b, c or d"
#             )
#     except ValueError as e:
#         print(f"Invalid data: {e}, please try again.\n")
#         return False

#     return True

def rules_or_play():
    """
    Function to get players choice of rules or to play game
    """
    player_choice = input('Type "r" to see the rules, "p" to play: \n')
    if player_choice == 'r':
        rules()
        player_choice = input('Type p to play or q to quit: \n')
        if player_choice == 'p':
            choices()
            game_choice()
        if player_choice == 'q':
            print('ok bye')
    elif player_choice == 'p':
        choices()
        game_choice()
    else:
        print('You must enter a valid choice either "r" or "p"')


# def clear_terminal():
#     """
#     clears terminal
#     """
#     os.system("printf")


def main_quiz_start():
    """
    Main function to run all program functions
    """
    table = [["Sun", 696000, 1989100000], ["Earth", 6371, 5973.6],
             ["Moon", 1737, 73.5], ["Mars", 3390, 641.85]]
    print(tabulate(table))
    welcome_message()
    user = User()
    user.get_user_name()
    # clear_terminal()
    rules_or_play()


main_quiz_start()
