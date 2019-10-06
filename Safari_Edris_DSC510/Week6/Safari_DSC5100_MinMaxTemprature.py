# File : Safari_DSC510_MinMaxTemperature.py
# Name:Edris Safari
# Date:10/04/2019
# Course: DSC510 - Introduction To Programming
# Desc:
# This program will populate a list of temperatures from user input.
# This program will display the number of temperatures entered by user,
# This program displays the maximum temperature and minimum temperature from the list entered by the user.
# Usage: Provide input when prompted.

# Some global variables
# List of temperatures is initialized here
temperatures = []

def isnegative(number):
    # This function determines if given input is a negative number
    # Return value is initialized to flse
    retval = False
    # Try & except are used to catch error if value given is string
    try:
        # Float function will fail if value is not numeric
        if float(number) < 0:
            retval = True
        else:
            rretval = false
    except:
        retval = False
    return retval


def getmax():
    # This function returns maximum value in the list between integers and floats.
    # This line gets maximum integer number
    max_num = max(i for i in temperatures if isinstance(i, int))
    # This line gets maximum float number
    max_float = max(i for i in temperatures if isinstance(i, float))

    # This conditional returns the higher value between int and float
    if max_float > max_num:
        return max_float
    else:
        return max_num

def getmin():
    # This function returns minimum value in the list between integers and floats.
    # This line gets minimum integer number
    min_num = min(i for i in temperatures if isinstance(i, int))
    # This line gets minimum integer number
    min_float = min(i for i in temperatures if isinstance(i, float))

    # This conditional returns the lesser value between int and float
    if min_float < min_num:
        return min_float
    else:
        return min_num

def isfloat(value):
    # This function return tru is the given value is float.
    # If the value give has one dot '.' in it, it is considered a float.
    retval = False
    numbers = str(value).split(".")
    # This makes sure it's a float with only one '.'
    if len(numbers) == 2:
        retval = True

    return retval


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
    while temperature.lower() != 'f' and not (temperature.isnumeric() or isfloat(temperature) or isnegative(temperature)):
        temperature = input('Please enter a numeric value for temperature value or enter \'f\' to end. >>> ')
    # If user enters f, we continue. The while above will exit the loop and results displayed
    if temperature.lower() == 'f':
        continue
    else:
        # Add temperature value to the list
        if temperature.isnumeric():
            # store as int if type is int
            temperatures.append(int(temperature))
        elif isfloat(temperature):
            # store as float if type is float
            temperatures.append(float(temperature))
        elif isnegative(temperature):
            # store negative number
             temperatures.append(float(temperature))

if len(temperatures) > 0:
    print("....................")
    print("....................")
    print("List of numbers" + str(temperatures))
    print('Number of temperatures entered: ' + str(len(temperatures)))
    print('Max Temperature:    ' + str(getmax()))
    print('Min Temperature:    ' + str(getmin()))
    print("....................")
    print("....................")

# Exit the program
print("Thank You. Please come back.")
