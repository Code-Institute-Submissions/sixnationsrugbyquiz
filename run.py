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
choices_out = []
choices_in = ["eng", "ire", "wal", "sc", "fr", "it"]


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

    print("Rules".center(80))
    print("The Rules are simple.  The Six Nations Championships".center(80))
    print("consist of six countries: Ireland, England, Wales".center(80))
    print("Scotland, Italy and France.  You will be asked five".center(80))
    print("questions on a country in each section.  All questions".center(80))
    print("are multiple choice. Answer with 'a', 'b' or 'c'".center(80))
    print("")
    print("Let's see which country you favour".center(80))
    print("")
    print('Type "p" to play or "q" to quit'.center(80))


def choices():
    """
    Displays choices for user
    """

    blank_spacer()
    print("Here are your six choices:".center(80))
    sleep(2)
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
    sleep(2)


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


def display_choices_left():
    """
    A Function to display game choices left for user
    """

    print('You have the following choices left to play:'.center(80))
    sleep(1)

    for i, left in enumerate(choices_in, 1):
        print(f"Choice {i}: {left}")


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

    global choices_out
    global choices_in
    print("")

    get_choice = input("Which game would you like to play?: \n".center(80))
    if get_choice == "eng" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(eng_question_list)
    elif get_choice == "ire" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(ire_question_list)
    elif get_choice == "wal" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(wales_question_list)
    elif get_choice == "fr" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(france_question_list)
    elif get_choice == "sc" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(scot_question_list)
    elif get_choice == "it" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(italy_question_list)
    elif get_choice in choices_out:
        print(f'You have already played {get_choice}')
        print("")
        game_choice()
    else:
        print('Did you type your choice correctly...\n')
        print('Please check and try again')
        print("")
        game_choice()


def get_questions(questions):
    """
    This function will get the questions for each section
    Get users answers
    Get users scores
    """
    clear()
    score = 0
    for question in random.sample(questions, 5):
        while True:
            answer = input(question.question).lower()
            if answer not in {'a', 'b', 'c'}:
                print("You must enter a, b or c, please try again")

            else:
                break
        if answer == question.answer:
            score += 1
            print('Correct Answer!')
            sleep(2)
            clear()
        else:
            print('Sorry you got that one wrong!')
            sleep(2)
            clear()
    sleep(2)
    print(f'You got {score} in that round')
    print('Would you like to continue playing or quit?\n')
    continue_play = input('Type p to play or q to quit\n')
    if continue_play == "p":
        display_choices_left()
        game_choice()
    elif continue_play == "q":
        quit()
    else:
        print("That wasn't a valid choice, please try again")


def rules_or_play():
    """
    Function to get players choice of rules or to play game
    """
    player_choice = input('Type "r" for rules, "p" to play: \n'.center(80))
    if player_choice == 'r':
        clear()
        rules()
        player_choice = input('Play or Quit?: \n'.center(80))
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
    display_score_board()
    welcome_message()
    user = User()
    user.get_user_name()
    sleep(2)
    clear()
    rules_or_play()


main_quiz_start()
