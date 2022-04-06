"""Contains user class"""


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
            username = input("So Player what shall I call you?: \n")

            if self.validate_name(username):
                print(f"Hello {username} let's get started...")
                break

    @staticmethod
    def validate_name(name):
        """
        Inside the try it checks if the user has inputed a name that
        is longer than 10 characters or has any characteres at all
        """

        try:
            if len(name) == 0:
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
