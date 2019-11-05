# File : Safari_DSC510_ChuckNorrisJokes.py
# Name: Edris Safari
# Date:10/29/2019
# Course: DSC510 - Introduction To Programming
# Desc:
# This program gets a joke from the "ChuckNorris" API
# This API generates a random Joke every time it is called.
# This program parses the JSON reply and displays the joke to the user.
# The user is allowed to get as many jokes as they wish by answering 'Y', or 'y',
# or 'yes' in all variations(YeS,YES,etc.) They can enter 'n' or 'no,also is same variations.
# The program presents the Yes/No question if any other response is made by the user(i.e. q, quit, xyz,jason, etc.)
# Usage:
# Execute this program from the command line by entering the program name Safari_DSC510_ChuckNorrisJokes


def welcome_screen():
    # This function prints the welcome screen. It is called by the main
    # function upon start of this application.
    welcome_message1 = 'Welcome to Object Oriented Cash Register'
    welcome_message2 = 'Enter items with price and get totals.'
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the welcome message line surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * ((max(len(welcome_message1),len(welcome_message2))) + 20)
    total_length = len(decoration_line)
    welcome_line1 = "-" * int((total_length-len(welcome_message1))/2) + welcome_message1 + "-" * int((total_length-len(welcome_message1))/2)
    welcome_line2 = "-" * int((total_length-len(welcome_message2))/2) + welcome_message2 + "-" * int((total_length-len(welcome_message2))/2)
    print(decoration_line)
    print(welcome_line1)
    print(welcome_line2)
    print(decoration_line)


def goodbye_screen():
    # This function prints the goodbye screen. It is called by the main
    # function upon normal exit from this application.
    goodbye_message = 'Thank you. Please come again.'
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the goodbye message line surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * (len(goodbye_message) + 20)
    goodbye_line = "-" * 10 + goodbye_message + "-" * 10
    print(decoration_line)
    print(goodbye_line)
    print(decoration_line)


def main():
    welcome_screen()

    print()
    print()

    goodbye_screen()


# Execute main function is this file is primary.
if __name__ == '__main__':
    main()
else:
    print("This Module's name is :" + __name__)