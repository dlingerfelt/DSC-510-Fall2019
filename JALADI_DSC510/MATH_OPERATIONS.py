# File :    MATH_OPERATIONS.py
# Name :    Pradeep Jaladi
# Date :    01/06/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#	Your program must have a header. Use the programming style guide for guidance.
#	This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
#	This program will contain a variety of loops and functions.
#	The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
#	Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
#		This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
#		This function will print the calculated value for the end user.
#	Define a function named calculateAverage which takes no parameters.
#		This function will ask the user how many numbers they wish to input.
#		This function will use the number of times to run the program within a for loop in order to calculate the total and average.
#		This function will print the calculated average.
#	This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
#	The main program should prompt the user for the operation they wish to perform.
#	The main program should evaluate the entered data using if statements.
#	The main program should call the necessary function to perform the calculation.
import operator


# This function will perform the desire math operation
def calculate(number1: float, number2: float, op: str) -> float:
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv}
    return operators[op](number1, number2)  # we are using the operator import and using the in built functions


# This function will get the valid input number
def get_input_number(message: str) -> float:
    number = 0
    while number == 0:
        try:
            number: float = float(input(message))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            continue
    return number


# This function will perform math operations add, subtract, multiple and division
def performCalculation(operation: str):
    number1 = get_input_number("Enter first number: ")
    number2 = get_input_number("Enter second number: ")
    output = calculate(number1, number2, operation)
    print("the output is " + str(output), end="\n")


# This function will perform average of the specified numbers
def calculateAverage():
    num = int(input('How many numbers: '))
    total_sum = 0
    for n in range(num):
        number = get_input_number("enter the number: ")
        total_sum += number  # Adding the numbers

    avg = total_sum / num  # Calculation of average
    print("the average is output is " + str(avg), end="\n")


def main():
    print("Welcome to math calculations program")
    print("Enter '+', '-', '*', '/', 'avg' for math operations and 'q' for quiting the program", end="\n")

    while True:
        operation: str = input("Enter your choice \n")
        if operation == 'q':
            break

        if ("+" == operation) or ("-" == operation) or ("*" == operation) or ("/" == operation):
            performCalculation(operation)
        elif operation == 'avg':
            calculateAverage()
        else:
            print("Invalid operation entered please reenter", end="\n")


if __name__ == '__main__':
    main()
