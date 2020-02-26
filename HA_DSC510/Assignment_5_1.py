#!/usr/bin/env python3

# File: Assignment_5_1.py
# Name: Jubyung Ha
# Date: 12/16/2019
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc: Tis program will perform various calculations
# (addition, subtraction, multiplication, division, and average calculation)
# This program will contain a variety of loops and functions.
# The program will add, subtract, multiply, divide two numbers
# and provide the average of multiple numbers input by the user.

# Define a function named performCalculation which takes one parameter.
# The parameter will be the operation being performed (+, -, *, /).
# This function will perform the given prompt the user for two numbers
# then perform the expected operation depending on the parameter that's passed into the function.
# This function will print the calculated value for the end user.

# Define a function named calculateAverage which takes no parameters.
# This function will ask the user how many numbers they wish to input.
# Use the number of times to run the program within a for loop in order to calculate the total and average.
# This function will print the calculated average.
# This program will have a main section which contains a while loop.

# The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
# The main program should prompt the user for the operation they wish to perform.
# The main program should evaluate the entered data using if statements.
# The main program should call the necessary function to perform the calculation.

# Usage: Create an instance of Calculator class
# Get operator and evaluate the input using getOperator()
# Get two numbers and evaluate the inputs using setNumbers()
# Perform operation using performCalculation(operator)
# Perform average using calculateAverage()


def getOperator():
    """Test if an argument is an operator"""
    operators = ['+', '-', '*', '/']
    while True:
        operator = input("Please enter an operator you want to perform (+, -, *, /): ")
        if operator in operators:
            break
    return operator


def getNumber():
    """Gets a number from an end user"""
    while True:
        try:
            num = float(input("Please enter a number:"))
            break
        except ValueError:
            print("You need to enter a number")
    return num


class Calculator:
    """Performs (+, -, *, /) operation and calculate average"""

    def __init__(self):
        self.__num1 = None
        self.__num2 = None
        self.__num_list = []
        self.__operator = None
        print("Thanks for using Calculator.")

    def setNumbers(self, operator):
        """Gets two number and set up number attributes"""
        self.__num1 = getNumber()
        while True:
            self.__num2 = getNumber()
            if self.__num2 == 0 and operator == '/':
                print("You can not divide a number by 0.")
                continue
            else:
                break

    def performCalculation(self, operator):
        """Performs operation based on argument"""
        if operator == '+':
            print(self.__num1 + self.__num2)
        elif operator == '-':
            print(self.__num1 - self.__num2)
        elif operator == '*':
            print(self.__num1 * self.__num2)
        elif operator == '/':
            print(self.__num1 / self.__num2)
        else:
            print("Undefined operation.")

    def calculateAverage(self):
        """Gets a number of numbers for average and performs average"""
        total_sum = 0

        while True:
            try:
                length = int(input("How many number do you wish to enter: "))
                if isinstance(length, int) and length >= 1:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a positive integer.")

        for i in range(length):
            self.__num_list.append(getNumber())

        for i in range(length):
            total_sum += self.__num_list[i]

        print(total_sum / length)


def main():
    calculator = Calculator()  # Create an instance of Calculator class

    while True:
        print()
        print("1 : Basic operation of two numbers")
        print("2 : Average of multiple numbers")
        print("N : Stop calculator")
        print()
        while True:
            command = input("Choose an operation to perform:")
            if command in ['1', '2', 'N', 'n']:
                break
            else:
                print("Please enter a valid value.")

        if command == 'N' or command == 'n':
            break
        elif command == '1':
            operator = getOperator()  # Get operator and evaluate the input
            calculator.setNumbers(operator)  # Get two numbers and evaluate the inputs
            calculator.performCalculation(operator)  # Perform operation
        else:
            calculator.calculateAverage()  # Perform average


if __name__ == '__main__':
    main()
