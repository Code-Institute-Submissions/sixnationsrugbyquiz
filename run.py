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
    This function will get the questions for each section
    """
    score = 0
    for question in questions:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + '/' + str(len(questions)) + " correct")


def main_quiz_start():
    """
    Main function to run
    """
    print('Hello and welcome to the Six Nations Rugby Quiz\n')
    print()
    print()
    print('Would you like to see the rules or go ahead and play the game?\n')
    player_choice = input('Type "r" to see the rules, "p" to play and "q" to quit: \n')
    if player_choice == 'r':
        print("Here are the rules")
    elif player_choice == 'p':
        print("Which game would you like to play? ")
    elif player_choice == 'q':
        print("Goodbye")
        
    # get_questions(eng_question_list)


main_quiz_start()
