"""Validation file"""


# class User():
#     """
#     This Function will create a user object
#     """
#     def __init__(self, username):
#         self.username = username

#     def get_user_name(self):
#         """
#         Allows user to enter their name

#         Maxium characters of 12 is valid
#         Profanity not allowed.  Use profanity_filter
#         to check
#         """
#         while True:
#             print("Please enter your name....")
#             print("Your name can not be longer than 10 characaters")
#             print("and cannot contain any numbers")

#             user_str = input("So Player what shall I call you?: /n")

#             username = user_str.split()

#             if validate_name(username):
#                 print(f"Hello {username} let's get started...")
# #     def validate_name(values):
#         """
#         Inside the try it checks if the user has inputed a name with
#         less than six characters and hasn't entered any numbers
#         """

#         try:
#             if values > 10:
#                 raise ValueError(
#                     f"Sorry only 10 characters allowed you had {len(values)}'
#                     )
#         pass
