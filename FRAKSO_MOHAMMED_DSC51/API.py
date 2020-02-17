'''
File: API.py
Name: Mohammed A. Frakso
Date: 02/16/2020
Course: DSC_510 - Introduction to Programming
Desc: This program uses an open API to obtain data for the end user:
Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
Your program should allow the user to request a Chuck Norris joke as many times as they would like. You should make sure that your program does error checking at this point. If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user. There are other ways to handle this. Think about included string functions you might be able to call.
Your program must include a header as in previous weeks.
Your program must include a welcome message for the user.
Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”
'''

import requests
import json


def get_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.request("GET", url)
    line = (response.text)
    info = json.loads(line)

    print("\n{}".format(info['value']))

    return


def main():
    print("Welcome to the Chuck Norris Jokes Program")

    get_joke()

    while True:
        try:
            joke = str(input('\nWould you like a new joke? Enter Y to read more jokes, or Q to quit the program:\n'))
        except ValueError:
            print("Invalid input")
        if joke.upper() == "Y":
            get_joke()
        else:
            if joke.upper() == "Q":
                print('\nExiting Chuck Norris Joke Program')
                break
            else:
                print('Invalid input, please try again')


if __name__ == '__main__':
    main()