'''
File: Loops.py
Name: Mohammed A. Frakso
Date: 12/01/2020
Course: DSC_510 - Introduction to Programming
Desc: This program will contain a variety of loops and functions:
The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
This function will print the calculated value for the end user.
Define a function named calculateAverage which takes no parameters.
This function will ask the user how many numbers they wish to input.
This function will use the number of times to run the program within a for loop in order to calculate the total and average.
This function will print the calculated average.
'''
import operator
# Function to do math operations
def calc(number1: float, number2: float, op: str) -> float:
    operands = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv}
    return operands[op](number1, number2)

# Function to get the valid input number
def get_number(message: str) -> float:
    number = 0
    while number == 0:
        try:
            number: float = float(input(message))
            break
        except ValueError:
            print('Invalid input please try again!')
            continue
    return number
# This function will perform math operations based on operation entered
def performCalculation(operation: str):
    number1 = get_number('Enter first number: ')
    number2 = get_number('Enter second number: ')
    output = calc(number1, number2, operation)
    print("the output is " + str(output), end="\n")


# This function will calculate total and average of numbers
def calculateAverage():
    num = int(input('How many numbers you want to enter? '))
    total_sum = 0
    for n in range(num):
        number = get_number('Please enter the number: ')
        total_sum += number

    avg = total_sum / num
    print("the average is " + str(avg), end="\n")

# Display the welcome statement


def main():
    print('Welcome to the math calculator:')
    print("Enter '+', '-', '*', '/', 'avg' for math operations, and 'cancel' for quiting the program", end="\n")

    while True:
        operation: str = input("Enter your choice \n")
        if operation == 'cancel':
            break

        if ("+" == operation) or ("-" == operation) or ("*" == operation) or ("/" == operation):
            performCalculation(operation)
        elif operation == 'avg':
            calculateAverage()
        else:
            print("Invalid input entered please try again", end="\n")

if __name__ == '__main__':
    main()




