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

import requests
import textwrap

chuck_norris_url = "https://api.chucknorris.io/jokes/random"
yes_replies = ['y', 'yes']
no_replies = ['n', 'no']


def welcome_screen():
    # This function prints the welcome screen. It is called by the main
    # function upon start of this application.
    welcome_message = 'Welcome to Chuck Norris Joke site'
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the welcome message line surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * (len(welcome_message) + 20)
    welcome_line = "-" * 10 + welcome_message + "-" * 10
    print(decoration_line)
    print(welcome_line)
    print(decoration_line)


def goodbye_screen():
    # This function prints the goodbye screen. It is called by the main
    # function upon normal exit from this application.
    goodbye_message = 'Thank you. Please come back for more Chuck Norris Jokes'
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the goodbye message line surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * (len(goodbye_message) + 20)
    goodbye_line = "-" * 10 + goodbye_message + "-" * 10
    print(decoration_line)
    print(goodbye_line)
    print(decoration_line)


def joke_screen(joke):
    # This function prints the joke screen. It is called by the main
    # function after getting the joke from Chuck Norris API. The joke is passed by main.

    # Create a wrapper of 50 characters long
    wrapper = textwrap.TextWrapper(width=70)
    # Wrap the text of the joke in 70 character long lines/chunks.
    word_list = wrapper.wrap(text=joke)
    # Calculations below construct three decoration lines which are '-' ,'*' and '+' repeated 70 times
    # and the joke message line in 70 character long lines, followed by another three decoration lines.
    decoration_line1 = "-" * 70
    decoration_line2 = "*" * 70
    decoration_line3 = "+" * 70
    print(decoration_line1)
    print(decoration_line2)
    print(decoration_line3)
    # Print each line.
    for element in word_list:
        print(element)
    print(decoration_line1)
    print(decoration_line2)
    print(decoration_line3)


def get_a_joke():
    # This function connects to the chuck norris API and executes its get method.
    # The response is converted to JSON and the joke is obtained from the key 'value'.
    # This function is called by main.
    try:
        response = requests.get(chuck_norris_url)
        if response.status_code != 200:
            print('Error requesting Get ' + str(response.status_code))
            exit(response.status_code)
        else:
            print('Success in getting web service ' + str(response.status_code))
        return response.json()["value"]
    except:
        exit('Exception connecting to chuck norris API. Maybe he is not RESTful!!')


def main():
    # Display welcome screen
    welcome_screen()
    # Initialize user reply
    user_reply = ''
    first_time = False
    # Valid replies are stored in 'yes_replies' and 'no_replies' global variable
    while not user_reply.lower() in (yes_replies + no_replies):
        if first_time:
            print('Would you like to get a chuck norris joke?')
            first_time = True
        else:
            print('Would you like to get another chuck norris joke?')

        user_reply = input('Please \'y\'  or \'yes\' to continue and \'n\'  or \'no\' to quit) >>> ')
        if user_reply.lower() in no_replies:  # Break out of the loop if user enters 'n' or 'no' and exit the program,
            break
        elif not user_reply.lower() in (yes_replies + no_replies):  # keep promoting until valid response is given.
            continue
        else:  # User wants to see a joke. Get her one.
            joke_screen(get_a_joke())  # Display the  joke returned by get_a_joke

        # re-init user reply.
        user_reply = ''

    # Display goodbye screen
    goodbye_screen()


# Execute main function is this file is primary.
if __name__ == '__main__':
    main()
else:
    print("This Module's name is :" + __name__)
