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
    print('Would you like to see the rules or go ahead and play the game?\n')
