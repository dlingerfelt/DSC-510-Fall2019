# File :    main.py
# Name :    Pradeep Jaladi
# Date :    02/18/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#     Create a header for your program just as you have in the past.
#     Create a Python Application which asks the user for their zip code or city.
#     Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
#     Display the weather forecast in a readable format to the user.
#     Use comments within the application where appropriate in order to document what the program is doing.
#     Use functions including a main function.
#     Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
#     Validate whether the user entered valid data. If valid data isn’t presented notify the user.
#     Use the Requests library in order to request data from the webservice.
#         Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
#     Use Python 3
#     Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful
# Desc : Weather Report display

from JALADI_DSC510.final.Weather import Weather
from JALADI_DSC510.final.WeatherReport import WeatherReport
from JALADI_DSC510.final.WeatherDisplay import WeatherDisplay


# Define the main() function to ask the user for zipcode or city
def main():
    print(
        "Welcome to Weather report.  The valid inputs are 'zipcode', 'zipcode, country code', 'city', 'city, statecode', 'city, state code, country code'")
    while True:
        try:
            user_input = input('Enter the zip code or city : ')

            # If user press enter or spaces with out any other character, then we need to ask him again for input
            if user_input.strip() == None or user_input.strip() == '':
                continue

            if user_input == 'q':  # if user enter q the program is exited
                break

            # Removing the extra spaces between the user input string
            user_input = ','.join([x.strip() for x in user_input.split(',')])
            split_str = user_input.split(',')

            # Initialization of weather object
            w = Weather()

            # If the first string of split object is numeric it is consider as zipcode, else as city
            if split_str[0].isnumeric():
                w.zipcode = user_input
            else:
                w.city = user_input

            # Fetching the weather report details
            wr = WeatherReport(w)
            wd = wr.fetch_weather()

            # if weather display object is returned we are printing the details.
            if wd is not None:
                wd.print_report()

        except Exception as err:
            print('Something went wrong, please try again {}'.format(err))


if __name__ == '__main__':
    main()
