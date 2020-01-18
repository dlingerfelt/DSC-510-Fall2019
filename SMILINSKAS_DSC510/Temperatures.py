# File: Temperatures.py
# Name: Vilius Smilinskas
# Date: 1/18/2020
# Course: DSC510: Introduction to Programming
# Desc: Program will collect multiple temperature inputs, find the max and min values and present the total
#       number of values in the list
# Usage: Input information when prompted, input go to retrieve the output
import sys
temperature = []   # list for temperatures to be stored
number = []   # list for input variable
count = 0     # int variable for keeping count of loops
while number != 'go':   # go is set up as sentinel value to break the input
    try:    # to not add go or any ineligible value into the program, if error: the exception will run line 17
        number = int(input('Enter a temperature or to run program enter go:'))
        temperature.append(number)   # append adds the parameter to the end of temperature
        count = count + 1   # counts the loops
    except ValueError:   # if line 15 triggers error run the below block of code
        print('The highest temperature is:' + str(max(temperature)))   # max() determines the maximum value
        print('The lowest temperature is:' + str(min(temperature)))    # min() determines the minimum value
        print('The number of values entered is:' + str(count))
        sys.exit()   # exits the program
