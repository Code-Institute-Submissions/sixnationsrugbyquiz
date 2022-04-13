"""True or False Quiz Game"""
# clear terminal screen


# Allows a time delay
from time import sleep

# to get random questions
import random

import gspread
from google.oauth2.service_account import Credentials

#  To create tables
from tabulate import tabulate

# import numpy as np
from info import welcome_message
from info import rules
from info import choices
from info import clear
from info import blank_spacer


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

score_data = SHEET.worksheet('scores')

# Get data for scores, choices, rules and leaderboard
user_scores = {"Name": "",
               "England": "0",
               "Ireland": "0",
               "Scotland": "0",
               "Wales": "0",
               "France": "0",
               "Italy": "0", }
choices_out = []
choices_in = ["eng", "ire", "wal", "sc", "fr", "it"]


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
                user_scores.update({"Name": username})
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


def update_score_sheet():
    """
    Use the score dictionary to update google sheets
    so the user can see top scores
    """

    new_list = list(user_scores.values())
    score_data.append_row(new_list)


def display_score_board():
    """
    This function uses the score dictionary to update google sheets
    Then sorts the sheet to put max scores on top
    Slices the first 4 rows
    and prints out the leaderboard in table format
    """

    score_data.sort((8, 'des'), range='A2:H1000')
    new_data = score_data.get_all_values()
    max_score = new_data[slice(0, 4)]
    print(tabulate(max_score, tablefmt="pretty",))


def display_choices_left():
    """
    A Function to display game choices left for user
    """
    blank_spacer()
    print('You have the following choices left to play:'.center(80))
    sleep(1)

    for i, left in enumerate(choices_in, 1):
        print(f"Choice {i}: {left}".center(80))


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
            print()
            print('Correct Answer!'.center(80))
            sleep(2)
            clear()
        else:
            print()
            print('Sorry you got that one wrong!'.center(80))
            sleep(2)
            clear()
    sleep(2)
    blank_spacer()
    print(f'You scored {score} for {choice_name}'.center(80))

    if row_no == "b1":
        user_scores.update({"England": str(score)})
    elif row_no == "c1":
        user_scores.update({'Ireland': str(score)})
    elif row_no == "d1":
        user_scores.update({'Scotland': str(score)})
    elif row_no == "e1":
        user_scores.update({'Wales': str(score)})
    elif row_no == "f1":
        user_scores.update({'France': str(score)})
    elif row_no == "g1":
        user_scores.update({'Italy': str(score)})

    print("Updating scores...".center(80))
    sleep(3)
    updating_mid_way()


def updating_mid_way():
    """
    Function to update scores for single game
    """

    if len(choices_in) != 0:
        print('Would you like to continue playing or quit?\n'.center(80))
        continue_play = input('Type p to play or q to quit\n'.center(80))
        if continue_play == "p":
            clear()
            display_choices_left()
            game_choice()
        elif continue_play == "q":
            quit_game_leader()
        elif (continue_play != "q" and continue_play != "p"):
            print("Invalid choice please try again".center(80))
            updating_mid_way()
    else:
        print("No choices left")
        print("Type l for leaderboard, q to quit or p to play again")
        what_next = input("So what would you like to do?\n")
        if what_next == "l":
            update_score_sheet()
            display_score_board()
            print("Goodbye, thanks for playing".center(80))
        elif what_next == "q":
            quit()
        elif what_next == "p":
            print("Play again")
        else:
            print("Invalid choice, try again")
            updating_mid_way()


def quit_game_leader():
    """
    Function to let user quit game
    """

    print("Would you like to see leaderboard before you go?".center(80))
    so_long = input("Type 'l' for leaderboard or 'q' to quit\n".center(80))
    if so_long == 'q':
        quit_game()
    elif so_long == 'l':
        update_score_sheet()
        display_score_board()
        print("Thanks for playing, click Let's Play "
              "above if you change your mind".center(80))


def quit_game():
    """
    Function to just quit game
    """
    print("Goodbye, sorry to see you go.  If you change your mind"
          " click Let's Play above".center(80))
    print()
    print()


def rules_or_play():
    """
    Function to get players choice of rules or to play game
    """
    blank_spacer()
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
