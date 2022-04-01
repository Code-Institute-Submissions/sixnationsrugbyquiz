"""True or False Quiz Game"""
import gspread
from colorama import Fore
from info import welcome_message
from info import rules
from google.oauth2.service_account import Credentials
from quest import eng_question_list
from quest import ire_question_list
from quest import wales_question_list
from quest import france_question_list
from quest import scot_question_list
from quest import italy_question_list


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


def get_questions(questions):
    """
    This function will get the questions for each section and get user
    scores
    """
    score = 0
    for question in questions:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
    print(f"{Fore.GREEN}You got " + str(score) + '/' + str(len(questions)) + " correct")


def game_choice():
    """
    This function gets the users choice on which game they want to play
    """
    print('You have the choice of six quiz sections to play:')
    print(f'To answer questions about England type {Fore.RED}"eng"{Fore.WHITE}')
    print(f'To answer questions about Ireland type {Fore.GREEN}"ire"{Fore.WHITE}')
    print(f'To answer questions about Scotland type {Fore.BLUE}"sc"{Fore.WHITE}')
    print(f'To answer questions about Wales type {Fore.LIGHTRED_EX}"wal"{Fore.WHITE}')
    print(f'To answer questions about France type {Fore.BLUE}"fr"{Fore.WHITE}')
    print(f'To answer questions about Italy type {Fore.CYAN}"it"{Fore.WHITE}')
    get_choice = input("So what's it going to be?: \n")
    if get_choice == "eng":
        get_questions(eng_question_list)
    elif get_choice == "ire":
        get_questions(ire_question_list)
    elif get_choice == "wal":
        get_questions(wales_question_list)
    elif get_choice == "fr":
        get_questions(france_question_list)
    elif get_choice == "sc":
        get_questions(scot_question_list)
    elif get_choice == "it":
        get_questions(italy_question_list)
    else:
        print('You must choose a valid selection, please choose again...\n')
        game_choice()


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
            game_choice()
        if player_choice == 'q':
            print('ok bye')
    elif player_choice == 'p':
        game_choice()
    else:
        print('You must enter a valid choice either "r" or "p"')


main_quiz_start()
