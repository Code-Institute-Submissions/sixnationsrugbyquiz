"""True or False Quiz Game"""
import gspread
from google.oauth2.service_account import Credentials
from info import welcome_message
from info import rules
from info import choices
from info import game_choice


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


def main_quiz_start():
    """
    Main function to run all program functions
    """
    welcome_message()
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


main_quiz_start()
