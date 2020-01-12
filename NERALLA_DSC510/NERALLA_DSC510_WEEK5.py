'''
File: NERALLA_DSC510_WEEK5.py
Name: Ravindra Neralla
Course:DSC510-T303
Date:01/11/2020
Description: This program will Define 2 functions
        This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
        This program will contain a variety of loops and functions.
        The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
        Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
        This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
        This function will print the calculated value for the end user.
'''

def get_valid_number(message: str):
    #This function will show the prompt from parameter then validate the user input and return valid int or float
    number = 0
    while number == 0:
        try:
            # Enter the input number
            number: float = float(input(message))
            break
        except ValueError:
            print("Invalid input number.  Please try again..")
            continue
    return number

# Function to add, subtract, multiply or divide

def performCalculation(operator: str):

 # This function prompts user to input two numbers and then perform the desired operation on the two numbers (+,-,*,/)
 #This function will print the calculated value for the end user.
 #This function has the input parameter named operator: +, -, *, /
    # Enter the valid number1
    number1 = get_valid_number("Enter first number:")
    # Enter the valid number2
    number2 = get_valid_number("Enter second number:")
    result = None
    # When the operator is + then, perform addition
    if operator is "+":
        result = number1 + number2
    # When the operator is - then, perform subtraction
    elif operator is "-":
        result = number1 - number2
    # When the operator is * then,perform multiplication
    elif operator is "*":
        result = number1 * number2
    # When the operator is / then,perform division
    elif operator is "/":
        # handle zero division error
        try:
            result = number1 / number2
        except ZeroDivisionError:
            print("Second number (Denominator) value should not be zero")

    if result is None:
        print("The invalid input operator {} for the input values".format(operator))
    else:
        print("Result: {} {} {} = {}".format(number1, operator, number2, result))

# Function to calculate average of the given numbers
def calculateAverage():

    # get how many numbers, convert it to int in case it's float
    count = int(get_valid_number("How many numbers to average:"))
    # initialize sum and average variables to zero
    sum_val = 0;
    avg_val = 0;
    # iterate over numbers to get the number and calculate sum
    for i in range(0, count):
        # get the number and add the number to sum
        number = get_valid_number("Enter the number:")
        sum_val += number
    # if count of numbers greater than 0 then calculate average
    if count > 0:
        avg_val = sum_val / count
    print("Average for {} numbers and sum {} is: {}".format(count, sum_val, avg_val))

# Function to print menus
def print_menu():

    #    This function will print the all menu options available

    print("***** Menu *****", end="\n")
    print("1. Add", end="\n")
    print("2. Subtract", end="\n")
    print("3. Multiply", end="\n")
    print("4. Divide", end="\n")
    print("5. Average", end="\n")
    print("0. Exit", end="\n")

# Check for main is called
if __name__ == "__main__":
    #This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.

    # list for operations
    operation = ["", "+", "-", "*", "/"]
    # print welcome message
    print("Welcome !!!")
    option = None
    # iterate until menu 0 is selected to exit
    while option is not 0:
        # show menu
        print_menu()
        # get menu choice from user
        menu = int(get_valid_number("Select operation from menu(0 to exit) :"))
        # if menu 0 selected then break the while loop
        if menu == 0:
            break
        # if menu selected is one of =, - , * or / call performCalculation with operator
        elif 0 < menu < 5:
            performCalculation(operation[menu])
        # if menu selected is 5 i.e. average, call calculate average
        elif menu == 5:
            # call calculateAverage
            calculateAverage()
        else:
            # show message if invalid choice selected
            print("Invalid choice...")
        # pause for user to read result
        input("Press Enter to continue...")