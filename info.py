""" File to display messages and format game """

import os
from time import sleep

# For ascii art
from pyfiglet import figlet_format

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
