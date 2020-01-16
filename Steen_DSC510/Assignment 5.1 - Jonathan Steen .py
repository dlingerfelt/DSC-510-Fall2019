# File: Assignment 5.1 - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 01/10/2020
# Course: DSC510 - Introduction to Programing
# Desc: Program does mathematical operations including averaging
# Usage:  The program gets an mathematical operator from the user
#         calculates two numbers from user input base on selected operation
#         The program then gets a set of defined set of numbers and calculates
#         the average

loop = True

# while loop to allow user to run calculations multiple times
while loop:

    sign = input("What operation would you like to perform?\nPlease input +, -, *, / for respective operation\n")

    # define function to do calclations
    def performCalculation(sign):

        x = float(input("Provide first number.\n"))
        y = float(input("Provide the second number.\n"))

        if sign == "+":
            print("\nSum is ", x+y,"\n")
        elif sign == "-":
            print("Subtraction is ", x-y, "\n")
        elif sign == "*":
            print("Multiplication is ", x*y, "\n")
        elif sign == "/":
            print("Division is ", x/y, "\n")
        else:
            print('You have not typed a valid operator, please run the program again.')

    # define function to calculate average
    def calculateAverage():

        totalNumbersToAverage = int(input("How many numbers would you like to input to get an average?\n"))
        count = 0
        total = 0.0

        for totalNumbersToAverage in range(totalNumbersToAverage):
            count = count + 1
            enteredNumber = float(input("Enter number " + str(count) + "\n"))
            total = float(enteredNumber + total)

        print("The average is", total/count, "\n")

    performCalculation(sign)

    calculateAverage()

    # if statement to end program or complete another calculation
    answer = input("Would you like to do another calculation? Please input 'yes' or 'no'.\n")
    if answer == "no":
        loop = False
        print("\nThank you. Have a good day!\n")
    elif answer == "yes":
        loop = True
