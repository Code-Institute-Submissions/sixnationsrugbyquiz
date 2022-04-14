"""Six Nations Rugby Quiz Game"""

# Allows a time delay
from time import sleep

# to get random questions
import random

# to access google sheets
import gspread
from google.oauth2.service_account import Credentials

#  To create tables
from tabulate import tabulate

# To add color
from colorama import Fore, Style

# For ascii text
from pyfiglet import figlet_format

# Imports from info file
from info import welcome_message
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

# access sheet for leaderboard
score_data = SHEET.worksheet('scores')

# Object to get data for scores, choices, and leaderboard
user_scores = {"Name": "",
               "England": "0",
               "Ireland": "0",
               "Scotland": "0",
               "Wales": "0",
               "France": "0",
               "Italy": "0",
               "Total": "0"}
choices_out = []
choices_in = ["eng", "ire", "wal", "sc", "fr", "it"]

# User


class User():
    """
    Creates a User object which can take
    the users name, display a message to user
    and validate user input for name and answers

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
        is longer than 10 characters or has any characters at all or
        if there are numbers in the username
        """

        try:
            if len(name.strip()) == 0:
                raise ValueError('...name cannot be blank\n')
            elif len(name) > 10:
                raise ValueError("..sorry only 10 characters"
                                 " allowed\n")
            elif name.isdigit():
                raise ValueError('...numbers on their own not'
                                 ' allowed\n')
            else:
                return True

        except ValueError as err:
            print(f'Please try again {err}'.center(80))
            return False

# Functions for scores, choices and leaderboards


def get_total_score():
    """
    Function to get total score for each section and
    append to score_data object
    """
    get_score_data = list(user_scores.values())[1:7]
    change_score = list(map(int, get_score_data))
    user_scores.update({"Total": sum(change_score)})


def update_score_sheet():
    """
    A function to use the score_data object to update google sheets
    so the user can see top scores
    """

    new_list = list(user_scores.values())
    score_data.append_row(new_list)


def display_score_board():
    """
    This function uses the score_data object to update google sheets
    Then sorts the sheet to put max scores on top
    Slices the first 4 rows
    and prints out the leaderboard in table format with banner
    """
    blank_spacer()
    score_data.sort((8, 'des'), range='A2:H1000')
    new_data = score_data.get_all_values()
    max_score = new_data[slice(0, 4)]
    print(Fore.GREEN)
    print(figlet_format('LEADERS',
                        font="banner3-D", justify="center"))
    print(Style.RESET_ALL)
    print(tabulate(max_score, tablefmt="pretty",))


def display_choices_left():
    """
    A Function to display game choices left for user
    This function will check what games the user has played
    already and output remaining games
    """
    blank_spacer()
    print('You have the following choices left to play:'.center(80))
    sleep(1)

    for i, left in enumerate(choices_in, 1):
        print(f"Choice {i}: {left}".center(80))


# Quiz Functions


def game_choice():
    """
    A function to get the users choice of game.
    The choice is then appended to the choices_out array and
    removed from choices_in array.
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
    Get users scores are appended to scores_data object
    to update leaderboard
    """
    clear()
    score = 0

    for question in random.sample(questions, 5):
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
            print(Fore.GREEN + 'Correct Answer!'.center(80))
            print(Style.RESET_ALL)
            sleep(2)
            clear()
        else:
            print()
            print(Fore.RED + 'Sorry you got that one wrong!'.center(80))
            print(Style.RESET_ALL)
            sleep(2)
            clear()
    sleep(2)
    blank_spacer()
    print(Fore.YELLOW + f'You scored {score} for {choice_name}'.center(80))
    print(Style.RESET_ALL)

    if row_no == "b1":
        user_scores.update({"England": str(score)})
        get_total_score()
    elif row_no == "c1":
        user_scores.update({'Ireland': str(score)})
        get_total_score()
    elif row_no == "d1":
        user_scores.update({'Scotland': str(score)})
        get_total_score()
    elif row_no == "e1":
        user_scores.update({'Wales': str(score)})
        get_total_score()
    elif row_no == "f1":
        user_scores.update({'France': str(score)})
        get_total_score()
    elif row_no == "g1":
        user_scores.update({'Italy': str(score)})
        get_total_score()

    print("Updating scores...".center(80))
    sleep(3)
    updating_mid_way()


def updating_mid_way():
    """
    This function allows the user to continue play
    or quit the quiz at the end of each section.  It is
    also used to complete the quiz and update
    scoreboard.
    """

    if len(choices_in) != 0:
        print()
        print('Would you like to continue playing or quit?\n'.center(80))
        print('If you quit now all scores will be lost'.center(80))
        continue_play = input('Type p to play or q to quit\n'.center(80))
        print()
        if continue_play == "p":
            clear()
            display_choices_left()
            game_choice()
        elif continue_play == "q":
            clear()
            quit_game_leader()
        elif continue_play != "q" and continue_play != "p":
            print("Invalid choice please try again".center(80))
            updating_mid_way()
    else:
        print("You have answered all sections".center(80))
        print()
        print("Type s for Leader score board or q to quit".center(80))
        print()
        what_next = input("So what would you like to do?\n".center(80))
        if what_next == "s":
            clear()
            get_total_score()
            update_score_sheet()
            display_score_board()
            print("Goodbye, thanks for playing".center(80))
            print("If you change your mind and want to play...".center(80))
            print("Click the Let's Play Button below the terminal".center(80))
        elif what_next == "q":
            quit()
        else:
            print("Invalid choice, try again".center(80))
            updating_mid_way()


def quit_game_leader():
    """
    This function will quit the game giving the user the option
    to view the leaderboard before quitting
    """
    blank_spacer()
    print("Would you like to see leaderboard before you go?".center(80))
    so_long = input("Type 's' for Leader score "
                    "board or 'q' to quit\n".center(80))
    if so_long == 'q':
        clear()
        quit_game()
    elif so_long == 's':
        clear()
        update_score_sheet()
        display_score_board()
        print("Thanks for playing, click Let's Play "
              "below if you change your mind".center(80))
        print()
        print()
    elif so_long != "s" and so_long != "p":
        print("Not a valid input, you must enter 'q' or 's'".center(80))


def quit_game():
    """
    Function to just quit game after Rules, no leaderboard required.
    """
    blank_spacer()
    print("Goodbye, sorry to see you go.".center(80))
    print("If you change your mind and want to play again".center(80))
    print("Click Let's Play below".center(80))

# Functions for Rules


def rules():
    """
    A function that displays rules to the user from google sheets
    """
    blank_spacer()
    print("Rules".center(80))
    print()
    print("The Rules are simple.  The Six Nations Championships".center(80))
    print("consist of six countries: Ireland, England, Wales".center(80))
    print("Scotland, Italy and France.  You will be asked five".center(80))
    print("questions on a country in each section.  All questions".center(80))
    print("are multiple choice. Answer with 'a', 'b' or 'c'".center(80))
    print("")
    print("Let's see which country you favour".center(80))
    print("")
    print('Type "p" to play or "q" to quit'.center(80))
    after_rules()


def after_rules():
    """
    Function to get choice after rules are displayed
    """

    rules_reply = input('Would you like to play or quit?\n'.center(80))
    if rules_reply == "p":
        choices()
        game_choice()
    elif rules_reply == "q":
        clear()
        quit_game()
    else:
        print("Not valid, please enter p or q to proceed".center(80))
        after_rules()


def rules_or_play():
    """
    Function to get players choice of rules or to play game
    at the start of the game
    """
    blank_spacer()
    blank_spacer()
    player_choice = input('Type "r" for rules, "p" to play: \n'.center(80))
    if player_choice == 'r':
        clear()
        rules()
    elif player_choice == 'p':
        clear()
        choices()
        game_choice()
    else:
        print('You must enter a valid choice either "r" or "p"')
        rules_or_play()


# Main Quiz Function


def main_quiz_start():
    """
    Main function to run quiz
    """

    welcome_message()
    user = User()
    user.get_user_name()
    sleep(2)
    clear()
    rules_or_play()


main_quiz_start()
