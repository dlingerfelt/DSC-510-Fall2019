# File: Assignment 12.1 Final Project - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 1/21/2020
# Course: DSC510 - Introduction to Programing
# Desc: Program will pull weather information from OpenWeatherMap
# Usage:  The program will display weather based zip code input by user

# import libraries
import requests, sys

def main():

    print('Welcome to the Weather Program!')
    print('Feel free to check as many weather conditions as you would like.')

    loop = True

    while loop:

        cityNameZip = input("\nEnter city name or Zip Code: ")

        #if statement to get correct city and country
        if isinstance(cityNameZip, int) == int:

            apiKey = 'd42daf07fc2261bfaac82892fa0e0e2b'
            url = 'http://api.openweathermap.org/data/2.5/weather?'

            fullUrl = url + 'appid=' + apiKey + '&q=' + cityNameZip

        else:
            apiKey = 'd42daf07fc2261bfaac82892fa0e0e2b'
            url = 'http://api.openweathermap.org/data/2.5/weather?'

            fullUrl = url + 'appid=' + apiKey + '&q=' + cityNameZip + ',us'

        # function to convert to usa measurements
        def convert(currentTemp, currentPressure):

            global fahrenheitTemp, inchPressure

            fahrenheitTemp = float((currentTemp - 273.15) * 9 / 5 + 32)
            inchPressure = float(currentPressure) / 33.863886666667
            return (fahrenheitTemp, inchPressure)

        #function to format and display weather to user
        def printWeather():
            print('\n The weather for ' + str(currentCity) +
                  '\n Temperature is ' + str(fahrenheitTemp).split('.')[0] + '\xb0' +
                  '\n Pressure is ' + str('{:.2f}'.format(inchPressure)) + ' in' +
                  '\n Humidity is ' + str(currentHumidity) + '%' +
                  '\n Description is ' + str(weather))

        # try statement to catch error if connection is not made
        try:
            #api connection
            response = requests.get(fullUrl)

        except:
            sys.exit("\nConnection unsuccessful. Try again later.")

        # get data from api
        x = response.json()

        # if statement to get specific data from API with error checking
        if x['cod'] != '404':
            try:
                currentCity = x['name']

                y =x['main']

                currentTemp = y['temp']
                currentPressure = y['pressure']
                currentHumidity = y['humidity']


                z = x['weather']
                weather = z[0]['description']
            except:
                sys.exit(print('\nError retrieving data. Please try again later.'))

            convert(currentTemp, currentPressure)

            printWeather()

            checkErrorsLoop = True

            # loop to check for user input error throughout the program
            while checkErrorsLoop:

                answer = input("\nWould you like to check another city's weather forecast? Please input 'yes' or 'no'.\n")
                answer =answer.lower()

                if 'yes' == answer:
                    checkErrorsLoop = False
                    loop = True

                elif 'no' == answer:
                    checkErrorsLoop = False
                    print("\nHave a good day.")
                    loop = False

                else:
                    checkErrorsLoop = True
                    print('\n*Incorrect Input! Please input "yes" or "no" only.*\n')

        else:
            print('\nCity not found! Please input correct format. 5 digit zip code or "city, state"')

            checkErrorsLoop = True

            while checkErrorsLoop:

                answer = input("\nWould you like to try again? Please input 'yes' or 'no'.\n")
                answer.lower()

                if 'no' == answer:
                    checkErrorsLoop = False
                    loop = False
                    print("\n\nHave a good day!")
                elif 'yes' == answer:
                    checkErrorsLoop = False
                    loop = True
                else:
                    checkErrorsLoop = True
                    print('\n*Incorrect Input! Please input "yes" or "no" only.*\n')

if __name__ == '__main__': main()
