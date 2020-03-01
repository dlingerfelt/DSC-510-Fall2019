# File : assignment12.1-Weather_Program.py
# Name : Bhargava Gaggainpali
# Date : MAR-1-2020
# Course : Introduction to Programming - python
# Assignment :
#-For your class project we will be creating an application to interacts with a webservice in order to obtain data. Your program will use all of the information you’ve learned in the class in order to create a useful application.
#-Your program must prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap. Your program must display the weather information in a READABLE format to the user.
#-Create a header for your program just as you have in the past.
#-Create a Python Application which asks the user for their zip code or city.
#-Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
#-Display the weather forecast in a readable format to the user.
#-Use comments within the application where appropriate in order to document what the program is doing.
#-Use functions including a main function.
#-Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
#-Validate whether the user entered valid data. If valid data isn’t presented notify the user.
#-Use the Requests library in order to request data from the webservice.
#-Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
#-Use Python 3
#-Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful
# Desc : Program is to take input on zip code or city name and display the weather of the city.
# Usage :
# -Program is to take input on zip code or city name and display the weather of the city.

import pytemperature        # Import pytemperature library for conversions
import requests             # Import requests library for WebServices

def Build_URL(user_input, input_type):                                      # define Build_URL method to construct the URL with the Zip code or City name
    apiKey = 'd42daf07fc2261bfaac82892fa0e0e2b'                             # hard code key value
    url = 'http://api.openweathermap.org/data/2.5/weather?'                 # hard code the static URL value
    if input_type == 'zip_code':
        fullUrl = url + 'appid=' + apiKey + '&q=' + user_input
    else:
        fullUrl = url + 'appid=' + apiKey + '&q=' + user_input + ',us'
    return(fullUrl)                                                         # return Full_URL to call Webservice

def Execute_URL(Weather_app_url):                                           # define Execute_URL method to call the webservice
    try:
        Response = requests.get(Weather_app_url)                            # Call the Webservice
        URL_Res = Response.json()                                           # convert the response to json format
        return(URL_Res)                                                     # return the value of webservice
    except:
        print('\nConnection UnSuccessful or Error retrieving data for the given Zip Code or City.') # display the message when the Webservice connection is broken

def Print_Response(URL_Response):                                           # define the Print_Response method to print all the values from the Webservice response
    cityname = URL_Response['name']                                         # get the City name and other values fr from webservice
    coord = URL_Response['coord']
    longtitude = coord['lon']
    latitude = coord['lat']
    gentemp = URL_Response['main']
    temp = pytemperature.k2f(gentemp['temp'])                               # pytemperature.k2f turns kelvin into farenheit
    maxtemp = pytemperature.k2f(gentemp['temp_max'])
    mintemp = pytemperature.k2f(gentemp['temp_min'])
    humidity = gentemp['humidity']
    wind = URL_Response['wind']
    speed = wind['speed']
    desc = URL_Response['weather'][0]['description']
    print("*** In '{}' its '{}' now ***".format(cityname,desc))         # printing the values to the user
    print("Current Temperature      : {}F".format(temp))
    print("Today's High Temperature : {}F".format(maxtemp))
    print("Today's Low Temperature  : {}F".format(mintemp))
    print('Humidity                 : {}%'.format(humidity))
    print('Wind Speed               : {}mph'.format(speed))
    print('Location Coordinates     : Longtitude {} & Latitude {}'.format(longtitude, latitude))

def main():                                                             # define main program
    print('\n***** Welcome to the Weather Program..!! *****')           # print welcome message

    get_user_input = True
    while get_user_input:                                               # Run the loop to get weather for multiple cities.
        try:                                                            # Try block to catch any errors or exceptions
            print('\n-------------------------------------------------------------------------------------------------------------------------------')
            user_input = input("Please Enter the 'Valid 5 digit ZIP-CODE' or 'CITY NAME,STATE CODE' to check the weather condition or Enter 'Q' to Exit Program: ")  # retrive the user input

            if user_input.lower() == 'q':                               # check the condition to quit the program
                get_user_input = False
                continue
            else:
                if user_input.isnumeric():
                    Weather_app_url = Build_URL(user_input, 'zip_code') # Call the Build_URL method with Zipcode
                else:
                    Weather_app_url = Build_URL(user_input, 'city_name')    # Call the Build_URL method with City Name to construct the URL

            URL_Response = Execute_URL(Weather_app_url)                 # Call the Execute_URL method call the webservice

            Print_Response(URL_Response)                                # Call the Print_Response method print the values to the user
        except:
            print("\n***** Error retrieving data for the given ZipCode/City '{}'. Please try again. *****".format(user_input)) # print response to the user for errors

    print('\n***** Thank you for using the Weather Program..!! *****')


if __name__ == '__main__': main()