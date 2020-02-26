# File: Assignment 10.1 - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 2/12/2020
# Course: DSC510 - Introduction to Programing
# Desc: Program will connect to API and retrieve Chuck Norris jokes.
# Program will retrieve JSON data and all display results and
# allow users to requests jokes multiple times
# Usage:  The program will get Chuck Norris jokes for users

#import libraries
import requests, textwrap, sys

def main():

    print('Welcome to the Chuck Norris Jokes Program')
    print('Where you can get as many Chuck Norris jokes as you like.')
    print("Get ready! Here's your first joke!")

    loop = True

    while loop:

         #function to retrieve joke from api
        def retrieveJoke():
            try: #error-checking connection
                response = requests.get("http://api.icndb.com/jokes/random?exclude=explicite").json()
                print('\n' + textwrap.fill(response['value']['joke'])) #textwrap to keep joke in readable format
            except:
                sys.exit('Error connecting to Server. Please try again later.')

        #retrieve joke from api
        retrieveJoke()

        checkInputErrors = True

        #loop to check for user input errors
        while checkInputErrors:

            answer = input('\nWould you like a new joke? Please enter yes or no.\n')
            answer.lower()

            if 'yes' == answer:
                checkInputErrors = False
                loop = True

            elif 'no' == answer:
                checkInputErrors = False
                loop = False
                print("\nHave a good day.\n")

            else:
                checkInputErrors = True
                print('\n*Incorrect Input! Please input "yes" or "no" only.*\n')

main()
