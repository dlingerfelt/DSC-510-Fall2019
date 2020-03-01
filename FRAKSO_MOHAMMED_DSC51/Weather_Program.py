'''
File: WeatherProgram.py
Name: Mohammed A. Frakso
Date: 03/01/2020
Course: DSC_510 - Introduction to Programming
Desc: This program will interact with a webservice in order to obtain data.:

Create a header for your program just as you have in the past.
Create a Python Application which asks the user for their zip code or city.
Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
Display the weather forecast in a readable format to the user.
Use comments within the application where appropriate in order to document what the program is doing.
Use functions including a main function.
Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
Validate whether the user entered valid data. If valid data isn’t presented notify the user.
Use the Requests library in order to request data from the webservice.
Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
Use Python 3
Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful
'''

import requests
import json
import datetime

My_key = '831b68734bd5967f63970da2fca49f89'  # key provided by openweathermap.com

# asking user for input
def main():
    entry = input('Enter zip code or city: ')
    current_cond(entry)
    forecast(entry)
# Displaying welcome message
print('**************Welcome to the Weather Forecast Program*************** \n')

def input_check(entry):
    if entry.isdigit() == True:
        inptstring = zip_code(entry)
    elif entry.isalpha() == True:
        inptstring = city(entry)
    else:
        print('Invalid  Entry')
        main()

    return inptstring

def zip_code(entry):  # handle zip-code
    inptstring = {'zip': entry, 'units': 'imperial', 'APPID': '831b68734bd5967f63970da2fca49f89'}
    return inptstring

def city(entry):      # handle punctuation and spaces in city names
    inptstring = {'q': entry, 'units': 'imperial', 'APPID': '831b68734bd5967f63970da2fca49f89'}
    return inptstring

def current_cond(entry):  # request for current weather
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    headers = {'cache-control': 'no-cache'}
    inptstring = input_check(entry)

    response = requests.request('GET', url, headers=headers, params=inptstring)  # try block for connection

    dic = (response.text)   # fail or success message
    info = json.loads(dic)

    print('\nCurrent conditions for {}'.format(info['name']))   # printing info full dictionary
    new_list = info['weather']

    for new_dic in new_list:
        print('Sky: {}'.format(new_dic['main']))
    # print("\n{}".format(info['main']))
    new_dic2 = info['main']
    # print(new_dic2)
    print('Temperature: {}\N{DEGREE SIGN}F'.format(round(new_dic2['temp'])))
    print('Feels Like: {}\N{DEGREE SIGN}F'.format(round(new_dic2['feels_like'])))
    print('Humidy: {}%'.format(new_dic2['humidity']))

    return


def forecast(entry): # request for the forecast weather
    url = 'http://api.openweathermap.org/data/2.5/forecast?'   # try block for connection with server
    headers = {'cache-control': 'no-cache'}
    inptstring = input_check(entry)

    response = requests.request("GET", url, headers=headers, params=inptstring)

    dic = (response.text)
    info = json.loads(dic)

    print('\nForecast: ')

    for item in info['list']:              # get date and time
        temperature = item['main']['temp']
        temperature = round(temperature)
        weather = item['weather'][0]['main']
        date = item['dt_txt'].split()
        day = date[0]
        time = date[1]
        print('{} {}: {}\N{DEGREE SIGN}F and {}'.format(date[0], date[1], temperature, weather))
        # print(temperature)
        # print(weather)
    return

def pretty_print(line):
    info = json.loads(line)
    current_cond(info)
    forecast(info)
    # print("\n{}".format(info['weather']))

    return


main()