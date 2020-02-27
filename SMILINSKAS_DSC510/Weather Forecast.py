# File: Weather Forecast.py
# Name: Vilius Smilinskas
# Date: 2/27/2020
# Course: DSC510: Introduction to Programming
# Desc: Program will ask for input, enter Q to quit or zipcode for the forecast in the area
# Usage: Run the program and respond to the prompts

import requests  # provides tools to interact with API
import json   # provides tools to parse JSON data
import pytemperature  # provides formulas to convert temperatures

key = '575c3fbd3590abbca581c923bcb452e4'  # key provided by openweathermap.cor


def main():
    zip = input('Enter the zipcode for the forecast:')
    url = 'http://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}'.format(zip, key)
    if zip == 'Q':
        exit('Goodbye')  # closes program with ending code 'Goodbye'
    try:
        int(zip)  # test if correct value, if entry includes letters it will ask for a new input
    except ValueError:
        print('Please enter a 5 digit US zip code:')
        main()  # restarts the main() function
    try:
        weather(url)
    except KeyError:  # if the API returns that the place isn't found
        print('Invalid Zip Code, try again')
    main()


def weather(url):
    forecast = requests.request("GET", url)  # requests response from the URL
    print('-------------------------------')
    print('Connected to OpenWeatherMap.org')
    file = json.loads(forecast.text)  # parses json data into file
    format(file)


def format(name):
    gentemp = name['main']
    temp = pytemperature.k2f(gentemp['temp'])   # pytemperature.k2f turns kelvin into farenheit
    maxtemp = pytemperature.k2f(gentemp['temp_max'])
    mintemp = pytemperature.k2f(gentemp['temp_min'])
    coord = name['coord']
    longtitude = coord['lon']
    latitude = coord['lat']
    humidity = gentemp['humidity']
    wind = name['wind']
    speed = wind['speed']
    cityname = name['name']
    print('Current Temperature in {} is {}F'.format(cityname, temp))
    print('High: {}F Low: {}F Humidity: {}%'.format(maxtemp, mintemp, humidity))
    print('Longtitude: {} Latitude: {}'.format(longtitude, latitude))
    print('Wind Speed: {}mph'.format(speed))


print('Welcome to the Weather Forecast Application\nEnter Q to quit')
main()
