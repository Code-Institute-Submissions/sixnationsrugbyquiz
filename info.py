"""
Information Messages for users
"""

import time
import random
from pyfiglet import figlet_format
from colorama import Fore
from quest import eng_question_list
from quest import ire_question_list
from quest import wales_question_list
from quest import france_question_list
from quest import scot_question_list
from quest import italy_question_list


def welcome_message():
    """
    Function to display welcome message to user
    """
    print(figlet_format('Six Nations Rugby Quiz', font="slant"))
    print('Hello and welcome to the Six Nations Rugby Quiz\n')
    time.sleep(3)
    print('Here you will be tested on your knowledge of Six Nations Rugby')
    time.sleep(2)
    print('There are six sections in total, one for each country')
    time.sleep(2)


def rules():
    """
    A Function that displays the rules to the user
    """
    print('The Rules are simple.....')
    time.sleep(2)
    print('The Six-Nations Championships consist of six countries...')
    time.sleep(2)
    print('Ireland, England, Scotland, Wales, Italy and France...')
    time.sleep(2)
    print('You will be asked 5 questions in each section...')
    time.sleep(2)
    print('Each section will have questions about each country...')
    time.sleep(2)
    print('All questions are multiple choice...')
    time.sleep(2)
    print('You answer with a, b, or c...')
    time.sleep(2)
    print("Let's see what country you cheer for...")
    time.sleep(2)


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


def choices():
    """
    Function to display choices for user
    """
    time.sleep(2)
    print('You have the choice of six quiz sections to play:')
    time.sleep(1)
    print(f'To answer questions about England type {Fore.RED}"eng"\
    {Fore.WHITE}')
    time.sleep(1)
    print(f'To answer questions about Ireland type {Fore.GREEN}"ire"\
    {Fore.WHITE}')
    time.sleep(1)
    print(f'To answer questions about Scotland type {Fore.BLUE}"sc"\
    {Fore.WHITE}')
    time.sleep(1)
    print(f'To answer questions about Wales type {Fore.LIGHTRED_EX}\
    "wal"{Fore.WHITE}')
    time.sleep(1)
    print(f'To answer questions about France type {Fore.BLUE}"fr"\
    {Fore.WHITE}')
    time.sleep(1)
    print(f'To answer questions about Italy type {Fore.CYAN}"it"\
    {Fore.WHITE}')
    time.sleep(2)


def get_questions(questions):
    """
    This function will get the questions for each section and get user
    scores
    """
    score = 0
    random.shuffle(questions)
    for question in questions:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
    print(f' your score is {score} out of {questions}')


def blank_line():
    """
    Function to display a blank line
    """
