# File: Assignment 12.1 Final Project - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 1/21/2020
# Course: DSC510 - Introduction to Programing
# Desc: Program will pull weather information from OpenWeatherMap
# Usage:  The program will display weather based zip code input by user

#import libraries
import requests, json, sys

print('Welcome to the Weather Program!')

loop = True

while loop:

    #function to handle api connection address
    def defineConnection():

        #if statement to get correct city and country
        if isinstance(cityNameZip, int) == int:
            global fullUrl
            global apiKey
            global url

            apiKey = 'd42daf07fc2261bfaac82892fa0e0e2b'
            url = 'http://api.openweathermap.org/data/2.5/weather?'

            fullUrl = url + 'appid=' + apiKey + '&q=' + cityNameZip

        else:
            apiKey = 'd42daf07fc2261bfaac82892fa0e0e2b'
            url = 'http://api.openweathermap.org/data/2.5/weather?'

            fullUrl = url + 'appid=' + apiKey + '&q=' + cityNameZip + ',us'

    #function to convert to usa measurements
    def convert(currentTemp, currentPressure):
        global fahrenheitTemp
        global inchPressure

        fahrenheitTemp = float((currentTemp - 273.15) * 9 / 5 + 32)
        inchPressure = float(currentPressure) / 33.863886666667
        return (fahrenheitTemp, inchPressure)

    #function to print weather
    def printWeather():
        print('\n The weather for ' + str(currentCity) +
              '\n Temperature is ' + str(fahrenheitTemp).split('.')[0] + '\xb0' +
              '\n Pressure is ' + str('{:.2f}'.format(inchPressure)) + ' in' +
              '\n Humidity is ' + str(currentHumidity) + '%' +
              '\n Description is ' + str(weather))

    cityNameZip = input("\nEnter city name or Zip Code: ")

    defineConnection()

    #try statement to catch error if connection is not made
    try:
        #api connection
        response = requests.get(fullUrl)

    except:
        sys.exit("\nConnection unsecessful. Try again later.")

    #get data from api
    x = response.json()

    if x['cod'] != '404':
        currentCity = x['name']

        y =x['main']

        currentTemp = y['temp']
        currentPressure = y['pressure']
        currentHumidity = y['humidity']


        z = x['weather']
        weather = z[0]['description']

        convert(currentTemp, currentPressure)

        printWeather()

        answer = input("\nWould you like to check another city's weather forecast? Please input 'yes' or 'no'.\n")

        if answer == 'no':
            loop = False
            print("\nHave a good day.")
        elif answer == "yes":
            loop = True

    else:
        print('\nCity not found!')
        answer = input("\nWould you like to try again? Please input 'yes' or 'no'.\n")
        if answer == 'no':
            loop = False
            print("\n\nHave a good day!")
        elif answer == "yes":
            loop = True
