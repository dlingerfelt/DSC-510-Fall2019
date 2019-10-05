# File : Safari_DSC510_MinMaxTemperature.py
# Name:Edris Safari
# Date:10/04/2019
# Course: DSC510 - Introduction To Programming
# Desc:
# This program will populate a list of temperatures from user input.
# This program will display the number of temperatures entered by user,
# the maximum temperature entered and the minimum temperature entered by the user.# Usage: Provide input when prompted.

#   Some global variables
# List of temperatures is initialized here
temperatures = []



def welcome_screen():
    """Print welcome screen"""
    # Welcome Screen
    print("-------------------------")
    print("Welcome to Python Temperature display  .")
    print("-------------------------")

welcome_screen()

temperature = ''

# Prompt for temperature until user enters the letter F or f.
while temperature.lower() != 'f':
    # Enter temperature value
    temperature = input('Please enter a temperature value (Enter \'f\' when done. ) >>> ')

    # Make sure user enters numeric value. they can enter f to end entering numbers.
    while not temperature.isnumeric() and temperature.lower() != 'f':
        temperature = input('Please enter a numeric value for temperature value or enter \'f\' to end. >>> ')
    # If user enters f, we continue. The while above will exit the loop and results displayed
    if temperature.lower() == 'f':
        continue
    else:
        # Add temperature value to the list
        temperatures.append(temperature)
print("List before the sort " + str(temperatures))
# The sort operation on the list affects the list permanently
temperatures.sort()
print("List after the sort " + str(temperatures))
print("....................")
print("....................")
print('Number of temperatures entered: ' + str(len(temperatures)))
print('Max Temperature:    ' + str(temperatures[-1]))
print('Min Temperature:    ' + str(temperatures[0]))
print("....................")
print("....................")
# Exit the program
print("Thank You. Please come back.")
