"""True or False Quiz Game"""
import os
from time import sleep
import random
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from pyfiglet import figlet_format
from validate import User
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
quiz_choices = SHEET.worksheet('quizchoices')
rules_info = SHEET.worksheet('rules')


def welcome_message():
    """
    Function to display welcome message to user
    """
    print(figlet_format('Six Nations Rugby Quiz', font="slant"))
    print('Hello and welcome to the Six Nations Rugby Quiz\n')

    print('Here you will be tested on your knowledge of Six Nations Rugby')

    print('There are six sections in total, one for each country')


def rules():
    """
    A Function that displays the rules to the user
    """

    rules_data = rules_info.get_all_values()
    rules_list = []
    for ind in rules_data:
        rules_list.append(ind)
    display_rules = rules_list
    print(tabulate(display_rules, tablefmt="pretty",))


def blank_line():
    """
    Function to display a blank line
    """
    print("")


def game_choice():
    """
    This function gets the users choice on which game they want to play
    """
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


def get_questions(questions):
    """
    This function will get the questions for each section and get user
    scores
    """
    clear()
    score = 0
    random.shuffle(questions)
    for question in questions:
        while True:
            answer = input(question.question).lower()
            if answer not in {'a', 'b', 'c'}:
                print("You must enter a, b or c, please try again")

            else:
                break
        if answer == question.answer:
            score += 1
            print('Correct Answer!')
        else:
            print('Sorry you got that one wrong!')
    print(f'You got {score} out of {len(questions)}')


def choices():
    """
    Function to display choices for user
    """

    qchoices = [['For Questions On:', 'Type:'], ["England", "eng"],
                ["Ireland", "ire"], ["Scotland", "sc"],
                ["Wales", "wal"], ["France", "fr"],
                ["Italy", "it"]]
    print(
        tabulate
        (qchoices, headers='firstrow', tablefmt='psql', stralign="center"))


def display_score_board():
    """
    Collects high scores to display
    """

    high_scores = data.get_all_values()
    result = []
    for ind in high_scores:
        result.append(ind)
    load_scores = result
    print(tabulate(load_scores, tablefmt="pretty",))


def rules_or_play():
    """
    Function to get players choice of rules or to play game
    """
    player_choice = input('Type "r" to see the rules, "p" to play: \n')
    if player_choice == 'r':
        clear()
        rules()
        player_choice = input('Type p to play or q to quit: \n')
        if player_choice == 'p':
            clear()
            choices()
            game_choice()
        if player_choice == 'q':
            print('ok bye')
    elif player_choice == 'p':
        clear()
        choices()
        game_choice()
    else:
        print('You must enter a valid choice either "r" or "p"')


def clear():
    """
    Function to clear console
    """
    os.system('clear')


def main_quiz_start():
    """
    Main function to run all program functions
    """
    # display_score_board()
    welcome_message()
    user = User()
    user.get_user_name()
    sleep(2)
    clear()
    rules_or_play()


main_quiz_start()
