'''
File: NERALLA_DSC510_WEEK12.py
Name: Ravindra Neralla
Course:DSC510-T303
Date:02/23/2020
Description: This program is to get weather forecast of a city.
    Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
    Display the weather forecast in a readable format to the user.
    Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
    Validate whether the user entered valid data. If valid data isn’t presented notify the user.
    Use the Requests library in order to request data from the webservice.
   Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful
'''
import requests
import sys

def main():

    print('Welcome to the Weather Report Program!!')
    print('\nPlease enter city or ZIP to check weather conditions in your city')

    loop = True
    while loop:

        City_Zip = input("\nEnter city or Zip Code: ")
        apiKey = 'd42daf07fc2261bfaac82892fa0e0e2b'
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        #if statement to get correct city and zip
        if City_Zip[0].isnumeric():

           full_url = base_url + 'appid=' + apiKey + '&q=' + City_Zip
        else:
           full_url = base_url + 'appid=' + apiKey + '&q=' + City_Zip + ',us'

        # Function to convert temperature to USA measurements, i.e. Fahrenheit

        def convert_temp(kelvintemp):
            return float(9 / 5 * (kelvintemp - 273.15)) + 32
        #Function to convert the output in standard format
        def print_report():
            print('\n Current Weather Conditions in ' + str(currentCity) +
                  '\n Current Temperature is ' + str(currenttemp).split('.')[0] + '\xb0' +
                  '\n Current  Feels Like Temperature is ' + str(feelslike_temp).split('.')[0] + '\xb0' +
                  '\n Lowest  Temperature Today is ' + str(temp_min).split('.')[0] + '\xb0' +
                  '\n Highest Temperature Today is ' + str(temp_max).split('.')[0] + '\xb0' +
                  '\n Pressure is ' + str('{:.2f}'.format(currentPressure_In)) + ' in' +
                  '\n Humidity is ' + str(currentHumidity) + '%' +
                  '\n Outside it looks like ' + str(weather_desc))

        # Use try and except, while connecting to web service
        try:

            response = requests.get(full_url)

        except:
            sys.exit("\nCould not connect to WebService. Please try again later.")

        # get data from webservice in json format
        dict = response.json()
        #print(dict)
        # if statement to handle error received from webservice call
        if dict['cod'] != '404':
            try:
                currentCity = dict['name']

                main_params =dict['main']

                currenttemp = main_params['temp']
                feelslike_temp = main_params['feels_like']
                temp_min = main_params['temp_min']
                temp_max = main_params['temp_max']
                currentPressure = main_params['pressure']
                currentHumidity = main_params['humidity']

                weather_desc = dict['weather'][0]['description']

            except:
                sys.exit(print('\nError retrieving data. Please try again later.'))

            currenttemp = convert_temp(currenttemp)
            feelslike_temp = convert_temp(feelslike_temp)
            temp_min = convert_temp(temp_min)
            temp_max = convert_temp(temp_max)
            currentPressure_In = float(currentPressure) / 33.863886666667

            print_report()

            checkuserinput_loop = True

            # loop to check for user input error throughout the program
            while checkuserinput_loop:

                answer = input("\nWould you like to check another city's weather forecast? Please input 'yes' or 'no'.\n")
                answer =answer.lower()

                if 'yes' == answer:
                    checkuserinput_loop = False
                    loop = True

                elif 'no' == answer:
                    checkuserinput_loop = False
                    print("\nHave a good day.")
                    loop = False

                else:
                    checkuserinput_loop = True
                    print('\n*Input value is incorrect! Please enter "yes" or "no" only.*\n')

        else:
            print('\nCity not found! Please input correct format. 5 digit zip code or "city, state"')

            checkuserinput_loop = True

            while checkuserinput_loop:

                answer = input("\nWould you like to try again? Please enter 'yes' or 'no'.\n")
                answer.lower()

                if 'no' == answer:
                    checkuserinput_loop = False
                    loop = False
                    print("\n\nHave a nice day!")
                elif 'yes' == answer:
                    checkuserinput_loop = False
                    loop = True
                else:
                    checkuserinput_loop = True
                    print('\n*Input value is incorrect! Please enter "yes" or "no" only.*\n')

if __name__ == '__main__': main()
