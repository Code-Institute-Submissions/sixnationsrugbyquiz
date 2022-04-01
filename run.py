"""True or False Quiz Game"""
import gspread
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
    print("You got " + str(score) + '/' + str(len(questions)) + " correct")

def game_choice():
    """
    This function gets the users choice on which game they want to play
    """
    print('You have the choice of six quiz sections to play:')
    print('To answer questions about England type "eng"')
    print('To answer questions about Ireland type "ire"')
    print('To answer questions about Wales type "wal"')
    print('To answer questions about France type "fr"')
    print('To answer questions about Scotland type "sc"')
    print('To answer questions about Italy type "it"')
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


def validate_choice(choices):
    """
    Inside the try, converts all values into lowercase.  
    Rais
    """


def main_quiz_start():
    """
    Main function to run all program functions
    """
    print('Hello and welcome to the Six Nations Rugby Quiz\n')
    print()
    print()
    print('Would you like to see the rules or go ahead and play the game?\n')
    player_choice = input('Type "r" to see the rules, "p" to play: \n')
    if player_choice == 'r':
        print("Here are the rules")
    elif player_choice == 'p':
        game_choice()
    else:
        print('You must enter a valid choice either "r" or "p"')


main_quiz_start()
