"""True or False Quiz Game"""
# clear terminal screen

import os

# Allows a time delay
from time import sleep

# to get random questions
import random

import gspread
from google.oauth2.service_account import Credentials

#  To create tables
from tabulate import tabulate

# For ascii art
from pyfiglet import figlet_format

# Contains User()
from user import User

# get questions
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

# Get data for scores, choices, rules and leaderboard
score_data = SHEET.worksheet('scores')
quiz_choices = SHEET.worksheet('quizchoices')
rules_info = SHEET.worksheet('rules')


# Functions below to display messages


def welcome_message():
    """
    Displays welcome message to user
    """
    print(figlet_format('Six Nations', font="slant", justify="center"))
    print(figlet_format('Rugby Quiz', font="slant", justify="center"))
    print('Hello and welcome to the Six Nations Rugby Quiz\n')
    sleep(2)
    print('Here you will be tested on your knowledge of Six Nations Rugby')
    sleep(2)
    print('There are six sections in total, one for each country')


def rules():
    """
    Displays the rules to the user from google sheets
    """

    rules_data = rules_info.get_all_values()
    rules_list = []
    for ind in rules_data:
        rules_list.append(ind)
    display_rules = rules_list
    print(tabulate(display_rules, tablefmt="pretty",))


def choices():
    """
    Displays choices for user
    """
    blank_spacer()
    print("Here are your six choices:".center(80))
    print()
    print('To answer questions on England, type "eng"'.center(80))
    sleep(2)
    print('To answer questions on Ireland, type "ire"'.center(80))
    sleep(2)
    print('To answer questions on Scotland, type "sc"'.center(80))
    sleep(2)
    print('To answer questions on Wales, type "wal"'.center(80))
    sleep(2)
    print('To answer questions on France, type "fr"'.center(80))
    sleep(2)
    print('To answer questions on Italy, type "it"'.center(80))


def display_score_board():
    """
    Collects high scores to display
    """

    high_scores = score_data.get_all_values()
    result = []
    for ind in high_scores:
        result.append(ind)
    load_scores = result
    print(tabulate(load_scores, tablefmt="pretty",))


# Miscellanous functions to tweek game

def blank_spacer():
    """
    Function to display multiple blank lines
    """
    print()
    print()
    print()
    print()
    print()


def clear():
    """
    Function to clear console
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# Game Functions


def game_choice():
    """
    Will get users choice on which game they want to play
    """
    print("")
    # choice_list = ["eng", "ire", "wal", "fr", "sc", "it"]
    get_choice = input("Which game would you like to play?: \n".center(80))
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
    This function will get the questions for each section
    Get users answers
    Get users scores
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
            sleep(3)
            clear()
        else:
            print('Sorry you got that one wrong!')
            sleep(3)
            clear()
    sleep(3)
    print(f'You got {score} out of {len(questions)}')
    print('Would you like to continue playing or quit?')
    continue_play = input('Type p to play or q to quit')
    if continue_play == "p":
        game_choice()
    elif continue_play == "q":
        quit()
    else:
        print("That wasn't a valid choice, please try again")


def rules_or_play():
    """
    Function to get players choice of rules or to play game
    """
    player_choice = input('Type "r" to see the rules, "p" to play: \n')
    if player_choice == 'r':
        clear()
        rules()
        player_choice = input('Play or Quit?: \n')
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

# Main Quiz


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
