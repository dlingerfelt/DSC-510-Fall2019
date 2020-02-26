#!/usr/bin/env python3

# File: Assignment_6_1.py
# Name: Jubyung Ha
# Date: 12/20/2019
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc: This week we will create a program which works with lists.
# Your goal is to create a program which contains a list of temperatures.
# Your program will populate the list based upon user input.
# Your program will determine the number of temperatures in the program,
# determine the largest temperature, and the smallest temperature.
#
# Your program must have a header. Use the programming style guide for guidance.
# Create an empty list called temperatures.
# Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
# Evaluate the temperature list to determine the largest and smallest temperature.
# Print the largest temperature.
# Print the smallest temperature.
# Print a message tells the user how many temperatures are in the list.

# Usage: The getNumber function will get an input number from an user and validate it.
# The getTemperature function will receive a number of temperature to be input into temperatures list and call getNumber
# The main function will call getTemperature function and evaluate the temperatures variable. i.e. min, max, and length

temperatures = []


def getNumber():
    """Gets a number from an end user"""
    while True:
        try:
            num = float(input("Please enter a number:"))
            break
        except ValueError:
            print("You need to enter a number")
    return num


def getTemperature():
    """Gets a number of temperature"""

    while True:
        try:
            length = int(input("How many number of temperature do you want to enter: "))
            if isinstance(length, int) and length >= 1:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

    for i in range(length):
        temperatures.append(getNumber())


def main():
    getTemperature()
    print("The max temperature is {} degree.".format(max(temperatures)))
    print("The min temperature is {} degree.".format(min(temperatures)))
    print("There are {} temperatures in the list".format(len(temperatures)))


if __name__ == '__main__':
    main()
