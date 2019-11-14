# File : Safari_DSC510_WeatherReporter.py
# Name: Edris Safari
# Date:11/06/2019
# Course: DSC510 - Introduction To Programming
# Desc:
# This program
# Usage:
# Execute this program from the command line by entering the program name Safari_DSC510_WeatherReporter

import requests
import textwrap
import zipcodes
import tkinter

open_weather_url = "https://api.openweathermap.org/data/2.5/weather"
yes_replies = ['y', 'yes']
no_replies = ['n', 'no']


def is_valid_zip_code(zip_code):
    # This function validates the pattern of the zip code. The regular expression below
    # returns valid for five digit value as well as five digits with hyphen followed by four or 5 digits.:
    # Example of valid patterns : 78133, 78133-3212
    # Example pf invalid patterns: Los Angels, 8976541,87676-123456
    return zipcodes.matching(zip_code.split('-')[0])


def welcome_screen():
    # This function prints the welcome screen. It is called by the main
    # function upon start of this application.
    welcome_message = 'Welcome to Python WeatherReporter'
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the welcome message line surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * (len(welcome_message) + 20)
    welcome_line = "-" * 10 + welcome_message + "-" * 10
    print(decoration_line)
    print(welcome_line)
    print(decoration_line)


def kelvin_to_fahrenheit(kelvin):
    return str(int(((float(kelvin) - 273.15) * 1.8) + 32)) + ' '


def goodbye_screen():
    # This function prints the goodbye screen. It is called by the main
    # function upon normal exit from this application.
    goodbye_message = 'Thank you. Please come back to get more weather reports'
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the goodbye message line surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * (len(goodbye_message) + 20)
    goodbye_line = "-" * 10 + goodbye_message + "-" * 10
    print(decoration_line)
    print(goodbye_line)
    print(decoration_line)


def report_screen(report):
    # This function prints the joke screen. It is called by the main
    # function after getting the joke from Chuck Norris API. The joke is passed by main.
    # Create a wrapper of 50 characters long
    wrapper = textwrap.TextWrapper(width=70)
    # Wrap the text of the joke in 70 character long lines/chunks.
    word_list = wrapper.wrap(text=report)
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


def google_map(zip_code_or_city):
    querystring = {"zip": zip_code_or_city, "APPID": "AIzaSyCNhfKTAsADVd_p271YaYn8fMeFKwPjrw4"}


def get_a_report(zip_code_or_city):
    # This function connects to the open weather API and executes its get method.
    # The response is converted to JSON and the following values are retrieved
    # This function is called by main.
    try:
        if is_valid_zip_code(zip_code_or_city):
            querystring = {"zip": zip_code_or_city.split('-')[0], "APPID": "f985b93ed77c52ad1dc90147bb8aa29e"}
        else:
            querystring = {"q": zip_code_or_city, "APPID": "f985b93ed77c52ad1dc90147bb8aa29e"}

        headers = {'cache-control': 'no-cache'}
        response = requests.get(open_weather_url, headers=headers, params=querystring)
        if response.status_code != 200:
            print('Error requesting Get ' + str(response.status_code))
            exit(response.status_code)
        else:
            print('Success in getting web service ' + str(response.status_code))
        temp_pressure_humidity = response.json()['main']
        return kelvin_to_fahrenheit(temp_pressure_humidity['temp'])
    except EnvironmentError:
        exit('Exception connecting to open_weather_url API!!')


def main():
    # Display welcome screen
    welcome_screen()
    # Initialize user reply
    user_reply = ''
    first_time = True
    # Valid replies are stored in 'yes_replies' and 'no_replies' global variable
    while not user_reply.lower() in (yes_replies + no_replies):
        if first_time:
            print('Would you like to get a weather report?')
            first_time = False
        else:
            print('Would you like to get another weather report?')

        user_reply = input('Please \'y\'  or \'yes\' to continue and \'n\'  or \'no\' to quit) >>> ')
        if user_reply.lower() in no_replies:  # Break out of the loop if user enters 'n' or 'no' and exit the program,
            break
        elif not user_reply.lower() in (yes_replies + no_replies):  # keep promoting until valid response is given.
            continue
        else:  # User wants to see a joke. Get her one.
            zip_code_or_city = input("please enter a zip code or city name >>>")
            report_screen(str(get_a_report(zip_code_or_city)))  # Display the  report

        # re-init user reply.
        user_reply = ''

    # Display goodbye screen
    goodbye_screen()


# Execute main function is this file is primary.
if __name__ == '__main__':
    main()
else:
    print("This Module's name is :" + __name__)
