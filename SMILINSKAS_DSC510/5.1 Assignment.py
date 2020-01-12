# File: 5.1 Assignment.py
# Name: Vilius Smilinskas
# Date: 1/11/2020
# Course: DSC510: Introduction to Programming
# Desc: Program performs different mathematical calculations corresponding to the inputs of the user.
# Usage: Input information when prompted, input Q to quit the program.
import sys   # importing sys to access sys.exit()


def calculateaverage():   # function for average calculation
    num_of_nums = input('How many numbers do you want to average?')   # storing the number of inputs that will be collected
    total = 0   # define initial total sum as 0
    for n in range(1, int(num_of_nums)+1):  # will make a loop from 1 to the number that will be collected + 1
        num_input = float(input('Enter a number to calculate the average:'))   # collects value for each input
        total = total + num_input
        average = total / float(n)
    print('The average is', average)   # once loop is done prints the final average


def performcalculation(calc):   # function for sorting and performing calculations
    if calc == 'avg':   # checks if it is the avg function
        calculateaverage()
    else:
        first_number = float(input('Please enter the first number for the operation'))
        second_number = float(input('Please enter the second number for the operation'))
    if calc == '+':   # checks if it is addition
        answer = first_number + second_number
        print('The answer is:', answer)
    elif calc == '-':    # checks if it is subtractions
        answer = first_number - second_number
        print('The answer is:', answer)
    elif calc == '*':   # checks if it is multiplication
        answer = first_number * second_number
        print('The answer is:', answer)
    elif calc == '/':   # checks if it is division
        answer = first_number / second_number
        print('The answer is:',  answer)


while True:   # establishes an infinite loop
    operation = str(input('Please choose a mathematical operation(+,-,*,/) or avg for Average, you can type in Q to Quit'))
    if operation == 'Q':   # tests for Quiting
        sys.exit('Closing Program')   # imported module sys triggers functions exit with the message 'Closing Program'
    performcalculation(operation)  # executes the defined function with operation as parameter
