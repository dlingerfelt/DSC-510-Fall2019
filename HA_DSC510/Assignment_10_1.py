#!/usr/bin/env python3

# File: Assignment_8_1.py
# Name: Jubyung Ha
# Date: 02/16/2020
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc: We’ve already looked at several examples of API integration from a Python perspective and
# this week we’re going to write a program that uses an open API to obtain data for the end user.
#
# Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
# The program will receive a JSON response which includes various pieces of data.
# You should parse the JSON data to obtain the “value” key.
# The data associated with the value key should be displayed for the user (i.e., the joke).
#
# Your program should allow the user to request a Chuck Norris joke as many times as they would like.
# You should make sure that your program does error checking at this point.
# If you ask the user to enter “Y” and they enter y, is that ok? Does it fail?
# If it fails, display a message for the user. There are other ways to handle this.
# Think about included string functions you might be able to call.
#
# Your program must include a header as in previous weeks.
# Your program must include a welcome message for the user.
# Your program must generate “pretty” output.
# Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”

# Usage: Run main() function to call welcome_message() function, and in the following loop,
# the program will ask for Y or N to get_joke() and prettify the joke.
# When an user ends the program, it will run end_message() function.


import requests
import textwrap
from urllib.error import HTTPError
from urllib.error import URLError


# Chuck Norris API address
url = 'https://api.chucknorris.io/jokes/random'


def welcome_message():
    print('------------------------------------------------')
    print('----------Welcome to Chuck Norris Joke----------')
    print('------------------------------------------------')


def end_message():
    print('------------------------------------------------')
    print('-------Thanks for using Chuck Norris Joke-------')
    print('------------------------------------------------')


def get_joke():
    """Gets response from API and return a value from the JSON
    Args:
        None
    :return:
        A String from JSON
    """
    try:
        response = requests.get(url)
        return response.json()["value"]
    except HTTPError as e:  # Exception if the page is not found
        print("The page could not be found!")
    except URLError as e:  # Exception if the server is down
        print("The server could not be found!")


def prettify_joke(joke):
    """ Prettify a string by wrapping
    :param joke:
    :return:
        NONE
    """
    print('------------------------------------------------')
    # Create a wrapper object and wrap a string
    wrapper = textwrap.TextWrapper(width=48)
    wrapped_string = wrapper.wrap(text=joke)
    # Print the wrapped string line by line
    for line in wrapped_string:
        print(line)
    print('------------------------------------------------')


def isAnswer(answer):
    """ Test if an answer is in Y or N and return True or False
    """
    if answer.upper() in ('Y', 'N'):
        return True


def main():
    welcome_message()
    while True:
        print('Do you like to have another Chuck Norris Joke?')
        answer = input('Y for yes, N for quit the program: ')
        # If the answer is not in Y or N, then send a warning and continue
        if not isAnswer(answer):
            print('Only enter Y or N for your answer!')
            continue
        # If the answer is N, then quit the program
        elif answer.upper() == 'N':
            break
        else:
            prettify_joke(get_joke())
    end_message()


if __name__ == '__main__':
    main()
