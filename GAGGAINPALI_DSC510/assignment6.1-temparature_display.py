# File : assignment6.1-temparature_display.py
# Name : Bhargava Gaggainpali
# Date : JAN-19-2020
# Course : Introduction to Programming - python
# Assignment :
#-Your program must have a header. Use the programming style guide for guidance.
#-Create an empty list called temperatures.
#-Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
#-Evaluate the temperature list to determine the largest and smallest temperature.
#-Print the largest temperature.
#-Print the smallest temperature.
#-Print a message tells the user how many temperatures are in the list.
# Desc : Program to request user to enter temperatures and then display min, max and count of temperatures entered.
# Usage :
# -This program is built to use Lists in Python program and request user to enter temperatures, then display min, max and count of temperatures entered.

if __name__ == "__main__":
    print("Welcome to temperature calculator program ....")

    temperature = []   # define a list

    # this will ask the user to list of temperatures.
    while True:
        input_value = input('\n Please enter a temperature. Type "d" when done: ')
        if input_value.lower() == 'd':  # check for sentinel value
            break
        try:
            temperature.append(float(input_value))  # verifies float number and adds to list
        except ValueError:
            print('Value entered is Invalid. Please enter a valid value.')

    print('Max temperature value you entered is : ', max(temperature)) # display max temperature entered
    print('Min temperature value you entered is : ', min(temperature)) # display min temperature entered
    print('The total number of temperature values you entered are ', len(temperature))  # display's count of temperatures entered.