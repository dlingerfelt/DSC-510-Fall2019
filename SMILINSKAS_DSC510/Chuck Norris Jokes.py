# File: Chuck Norris Jokes.py
# Name: Vilius Smilinskas
# Date: 2/15/2020
# Course: DSC510: Introduction to Programming
# Desc: Program will ask for input, enter Y to get a joke and N to quit
# Usage: Run the program and respond to the prompts

import requests  # provides tools to interact with API
import json   # provides tools to parse JSON data

url = "https://api.chucknorris.io/jokes/random"  # set variable to the url
print('Welcome to Chuck Norris Jokes, would you like to hear a joke?')


def main():
    condition = set()  # using a set as a mutable input
    condition = input('Type in Y for Yes\nType in N to Quit\n')
    if condition == 'Y':
        joke()
        main()  # reset program to continue loop
    if condition == 'N':
        exit('Goodbye')  # closes program with ending code 'Goodbye'
    else:
        print('Invalid entry please try again')
        main()  # start again


def joke():
    response = requests.request("GET", url)  # requests response from the URL
    file = json.loads(response.text)  # parses json data into file
    print(file['value'])  # request key for 'value'
    print('')


main()
