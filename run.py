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
# from tabulate import tabulate

# For ascii art
from pyfiglet import figlet_format

# Contains User()

# import numpy as np


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
user_scores = {"Name": [], }
choices_out = []
choices_in = ["eng", "ire", "wal", "sc", "fr", "it"]

# array = np.array([[1, 2, 3], [4, 5, 6]])

# # Write the array to worksheet starting from the A2 cell
# worksheet.update('A2', array.tolist())

# Class for User


class User():
    """
    Creates a User object which can take
    the users name, display a welcome message
    validate user input for name and answers

    """

    def get_user_name(self):
        """
        Allows user to enter their name
        Maxium characters of 12 is valid
        Numbers are not allowed
        """
        while True:
            username = input("So Player what shall I call you?: \n".center(80))
            if self.validate_name(username):
                # clear_user = username.split()
                # score_data.append_row(clear_user)
                user_scores["Name"].append(username)
                print(f"Hello {username} let's get started...".center(80))
                break

    @staticmethod
    def validate_name(name):
        """
        Inside the try it checks if the user has inputed a name that
        is longer than 10 characters or has any characteres at all
        """

        try:
            if len(name.strip()) == 0:
                raise ValueError('...name cannot be blank')
            elif len(name) > 10:
                raise ValueError("..sorry only 10 characters allowed")
            elif name.isdigit():
                raise ValueError('...numbers on their own not allowed')
            else:
                return True

        except ValueError as err:
            print(f'Please try again {err}')
            return False


# Functions below to display messages


def welcome_message():
    """
    Displays welcome message to user
    """

    print(figlet_format('Six Nations', font="slant", justify="center"))
    print(figlet_format('Rugby Quiz', font="slant", justify="center"))
    print('Hello and welcome to the Six Nations Rugby Quiz\n'.center(80))
    sleep(2)
    print('Here you will be tested on your knowledge of Six'
          ' Nations Rugby'.center(80))
    sleep(2)
    print('There are six sections in total, one for each'
          ' country'.center(80))


def rules():
    """
    Displays the rules to the user from google sheets
    """
    blank_spacer()
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


# def update_score_sheet():
#     """
#     Use the score dictionary to update google sheets
#     so the user can see top scores
#     """
#     score_data = SHEET.worksheet('scores')
#     score_data.append

    # for key, value in user_scores.items():
    #     output = str.join(" - ", value)

    #     print(output)


# def display_score_board():
#     """
#     Collects high scores to display
#     """

#     high_scores = score_data.get_all_values()
#     result = []
#     for ind in high_scores:
#         result.append(ind)
#     load_scores = result
#     print(tabulate(load_scores, tablefmt="pretty",))


def display_choices_left():
    """
    A Function to display game choices left for user
    """
    blank_spacer()
    print('You have the following choices left to play:'.center(80))
    sleep(1)

    for i, left in enumerate(choices_in, 1):
        print(f"Choice {i}: {left}".center(80))


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
        get_questions(eng_question_list, "England", "b1")
    elif get_choice == "ire" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(ire_question_list, "Ireland", "c1")
    elif get_choice == "wal" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(wales_question_list, "Wales", "e1")
    elif get_choice == "fr" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(france_question_list, "France", "f1")
    elif get_choice == "sc" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(scot_question_list, "Scotland", "d1")
    elif get_choice == "it" and get_choice not in choices_out:
        choices_out.append(get_choice)
        choices_in.remove(get_choice)
        get_questions(italy_question_list, "Italy", "g1")
    elif get_choice in choices_out:
        print(f'You have already played {get_choice}'.center(80))
        print("")
        game_choice()
    else:
        print('Did you type your choice correctly...\n'.center(80))
        print('Please check and try again'.center(80))
        print("")
        game_choice()


def as_list(x):
    """
    Changes score to list
    """
    if isinstance(x, list):
        return x
    else:
        return [x]


def get_questions(questions, choice_name, row_no):
    """
    This function will get the questions for each section
    Get users answers
    Get users scores and update leaderboard
    """
    clear()
    score = 0

    for question in random.sample(questions, 2):
        while True:
            blank_spacer()
            answer = input(question.question.center(80)).lower()
            if answer not in {'a', 'b', 'c'}:
                print("You must enter a, b or c, please try again".center(80))

            else:
                break
        if answer == question.answer:
            score += 1
            print('Correct Answer!'.center(80))
            sleep(2)
            clear()
        else:
            print('Sorry you got that one wrong!'.center(80))
            sleep(2)
            clear()
    sleep(2)
    blank_spacer()
    print(f'You scored {score} for {choice_name}'.center(80))
    user_scores[choice_name] = str(score)
    print(user_scores)
    # new_score = as_list(score)

    # if row_no == "b1":
    #     country_score = score_data.col_values(2)
    #     country_score.append_col(new_score)
    # elif row_no == "c1":
    #     country_score = score_data.col_values(3)
    #     country_score.append_col(new_score)
    # elif row_no == "d1":
    #     country_score = score_data.col_values(4)
    #     country_score.append_col(new_score)
    # elif row_no == "e1":
    #     country_score = score_data.col_values(5)
    #     country_score.append_col(new_score)
    # elif row_no == "f1":
    #     country_score = score_data.col_values(6)
    #     country_score.append_col(new_score)
    # elif row_no == "g1":
    #     country_score = score_data.col_values(7)
    #     country_score.append_col(new_score)

    print("Updating scores...".center(80))
    # print(user_scores)
    sleep(3)
    if len(choices_in) != 0:
        print('Would you like to continue playing or quit?\n'.center(80))
        continue_play = input('Type p to play or q to quit\n'.center(80))
        if continue_play == "p":
            clear()
            display_choices_left()
            game_choice()
        elif continue_play == "q":
            print("ok good bye".center(80))
        elif continue_play != "q" and continue_play != "p":
            print("Invalid choice please try again".center(80))
    else:
        print("No choices left")
        print("Type l for leaderboard, q to quit or p to play again")
        what_next = input("So what would you like to do?\n")
        if what_next == "l":
            print("display_score_board")
        elif what_next == "q":
            quit()
        elif what_next == "p":
            print("Play again")
        else:
            print("Invalid choice, try again")


def rules_or_play():
    """
    Function to get players choice of rules or to play game
    """
    blank_spacer()
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

    welcome_message()
    user = User()
    user.get_user_name()
    sleep(2)
    clear()
    rules_or_play()


main_quiz_start()
