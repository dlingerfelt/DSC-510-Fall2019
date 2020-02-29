#!/usr/bin/env python3

# File: Assignment_12_1.py
# Name: Jubyung Ha
# Date: 12/14/2019
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc:
# For your class project we will be creating an application to interacts with a webservice in order to obtain data.
# Your program will use all of the information you’ve learned in the class in order to create a useful application.
# Your program must prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap.
# Your program must display the weather information in a READABLE format to the user.

# Requirements:
# Create a header for your program just as you have in the past. X
# Create a Python Application which asks the user for their zip code or city.
# Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
# Display the weather forecast in a readable format to the user.
#
# Use comments within the application where appropriate in order to document what the program is doing. X
# Use functions including a main function. X
# Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
# Validate whether the user entered valid data. If valid data isn’t presented notify the user.
# Use the Requests library in order to request data from the webservice.
# Use Try blocks to ensure that your request was successful.
# If the connection was not successful display a message to the user.
# Use Python 3
# Use try blocks when establishing connections to the webservice.
# You must print a message to the user indicating whether or not the connection was successful

# Deliverable:
#
# Final Program in a .py file (Due week 12)
#
# Project Notes:
#
# Be creative. This assignment is a real world program. Use it as an opportunity to improve your knowledge.
# Sign up for API Key.
# The API key will look something similar to this: d5751b1a9e2e4b2b8c7983646072da8b
# Make a connection to the API using the Requests library.

# Usage:

import zipcodes
import requests

def isAnswer(answer):
    """ Test if an answer is in Y or N and return True or False
    """
    if answer.upper() in ('Y', 'N'):
        return True

def get_keyword():
    keyword = input('Please enter Zip Code or City Name: ')

def validate_keyword(keyword):
    pass

def validate_zip(self):
    pass

def validate_city(self):
    pass

class WeatherDisplay(object):
    def __init__(self):
        self.keyword = None
        self._url = 'https://api.openweathermap.org/data/2.5/weather'
        self._key = 'd8a620617540a1b64554015f7304d205'





def main():
    print('---------------------------------------------------')
    print('------------Welcome to Weather Forecast------------')
    print('---------------------------------------------------')
    while True:
        print('Do you want to display weather?')
        answer = input('Y for yes, N for quit the program: ')
        # If the answer is not in Y or N, then send a warning and continue
        if not isAnswer(answer):
            print('Only enter Y or N for your answer!')
            continue
        # If the answer is N, then quit the program
        elif answer.upper() == 'N':
            break
        else:

    weather = WeatherDisplay()
    weather.get_keyword()


if '__name__' == '__main__':
    main()
