# File : Safari_DSC510_Calculator.py
# Name:Edris Safari
# Date:9/28/2019
# Course: DSC510 - Introduction To Programming
# Desc:
#	This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
#	This program will contain a variety of loops and functions.
#	The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
#	Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
#	This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
#	This function will print the calculated value for the end user.
#	Define a function named calculateAverage which takes no parameters.
#	This function will ask the user how many numbers they wish to input.
#	This function will use the number of times to run the program within a for loop in order to calculate the total and average.
#	This function will print the calculated average.
#	This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
#	The main program should prompt the user for the operation they wish to perform.
#	The main program should evaluate the entered data using if statements.
#	The main program should call the necessary function to perform the calculation.
# Usage: Provide input when prompted.

#   Some global variables
valid_operations = ['+', '-', '*', '/', 'avg', 'q']

valid_operations_dict = {
    "+": "Addition",
    "-": "Subtraction",
    "*": "Multiplication",
    "/": "Division",
    "avg": "Average"
}


def welcome_screen():
    """Print welcome screen"""
    # Welcome Screen
    print("-------------------------")
    print("-------------------------")
    print("Welcome to Python Calculator.")
    print("-------------------------")
    print("-------------------------")


def calculate_average():
    """ Calculate average of a given number of values"""
    """ Make sure valid values are inputted """
    number_of_values = input('Please enter number of values to average >>> ')
    while not number_of_values.isnumeric():
        number_of_values = input('Please enter a numeric value >>> ')

    numbers = []
    accumulate = 0
    for x in range(int(number_of_values)):
        number = input('Please enter number' + str(x + 1) + ' of values to average >>> ')
        while not number.isnumeric():
            number = input('Please enter a numeric value >>> ')
        accumulate += float(number)
        numbers.append(str(number))

    print("List of Numbers to Average:")
    print(numbers)

    average = float(accumulate) / int(number_of_values)
    return average


def perform_calculation(operation):
    """Perform Calculation based on operation"""
    """check for valid value entry. Avoid divide by zero error"""

    first_number = input('Please enter 1st number >>> ')
    while not first_number.isnumeric():
        first_number = input('Please enter a numeric value >>> ')
    second_number = input('Please enter 2nd number >>> ')
    while not second_number.isnumeric():
        second_number = input('Please enter a numeric value >>> ')
        print(second_number)

    if operation == '+':
        calc_result = float(first_number) + float(second_number)
    elif operation == '-':
        calc_result = float(first_number) - float(second_number)
    elif operation == '*':
        calc_result = float(first_number) * float(second_number)
    elif operation == '/':
        if second_number == '0':
            while second_number == '0' or not second_number.isnumeric():
                second_number = input('Please enter a numeric value greater than zero >>> ')
        calc_result = float(first_number) / float(second_number)

    return calc_result


welcome_screen()

# Initialize operator
operation = ''

# Calculate until quit
while operation.lower() != 'q':
    while not operation.lower() in valid_operations:
        operation = input('Please Enter operation +, -, *, /, avg (Enter \'q\' to quit) >>> ')
    if operation.lower() == 'q':
        break
    elif operation.lower() == 'avg':
        result = calculate_average()
    else:
        result = perform_calculation(operation)

    print("....................")
    print("....................")
    print('Operation: ' + valid_operations_dict[operation])
    print('Result:    ' + str(result))
    print("....................")
    print("....................")
    # Reinitialize operation
    operation = ''

# Exit the program
print("")
print("")
print("")
print("")
print("Thank You. Please come back.")
