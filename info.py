"""
Information Messages for users
"""

import time
from pyfiglet import figlet_format


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


def blank_line():
    """
    Function to display a blank line
    """
