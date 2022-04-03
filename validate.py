"""Validation file"""


class User():
    """
    This Function will create a user object
    """
    def __init__(self, username):
        self.username = username

    def _get_user(self):
        """
        Allows user to enter their name

        Maxium characters of 12 is valid
        Profanity not allowed.  Use profanity_filter
        to check
        """
