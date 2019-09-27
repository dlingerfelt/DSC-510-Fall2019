'''
    File: Assignment5-1.py
    Author: Sanjay Jaras
    Assignment: 5.1
    Date:09/21/2019
    Course: DSC 510 - Introduction to programming
    Desc: This program will Define 2 functions
        1 . performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
        2.  calculateAverage which takes no parameters.
        This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
'''


# Function to add, subtract, multiply or divide
def performCalculation(operator: str):
    """
     This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
    This function will print the calculated value for the end user.
    :param operator: Operator from +, -, *, /
    """
    # get the valid first operand
    operator1 = get_valid_number("Enter first number:")
    # get the valid second operand
    operator2 = get_valid_number("Enter second number:")
    result = None
    # performa addition
    if operator is "+":
        result = operator1 + operator2
    # perform subtraction
    elif operator is "-":
        result = operator1 - operator2
    # perform multiplication
    elif operator is "*":
        result = operator1 * operator2
    # perform division
    elif operator is "/":
        # added check to avoid divide by zero error
        if operator2 != 0:
            result = operator1 / operator2
        else:
            print("Divide by zero")
            result = 0
    if result is None:
        print("The invalid input operator{}".format(operator))
    else:
        print("Result: {} {} {} = {}".format(operator1, operator, operator2, result))


# Function to find average of n numbers
def calculateAverage():
    """
    This function will ask the user how many numbers they wish to input.
    This function will use the number of times to run the program within a for loop in order to calculate the total and average.
    This function will print the calculated average.
    """
    # get how many numbers, convert it to int in case it's float
    count = int(get_valid_number("How many numbers to average:"))
    # initialize sum and average
    sum = avg = 0;

    # iterate over numbers to get the number and calculate sum
    for i in range(0, count):
        # get the number and add the number to sum
        sum += get_valid_number("Enter {}th number:".format(i + 1))

    # if count of numbers greater than 0 then calculate average
    if count > 0:
        avg = sum / count

    print("Average for {} numbers and sum {} is: {}".format(count, sum, avg))


def get_valid_number(message: str):
    """
    This function will show the prompt from parameter then validate the user input and return valid int or float
    :param message: Prompt text
    :return: return valid int or float
    """
    number = None
    while number is None:
        # prompt for input number
        number_str = input(message)
        # check for valid int number
        try:
            number = int(number_str)
        except ValueError:
            # if invalid int check for valid decimal number
            try:
                number = float(number_str)
            except ValueError:
                # if invalid float get number again
                print("Invalid number...", end="\n")
                number = None
    return number


# Function to print menus
def print_menu():
    """
    This function will print the all menu options available
    :return:
    """
    print("***** Menu *****", end="\n")
    print("1. Add", end="\n")
    print("2. Subtract", end="\n")
    print("3. Multiply", end="\n")
    print("4. Divide", end="\n")
    print("5. Average", end="\n")
    print("0. Exit", end="\n")


# Check for main is called on this file
if __name__ == "__main__":
    """
    This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
    """
    # list for operations
    operation = ["", "+", "-", "*", "/"]
    # print welcome message
    print("Welcome !!!")
    choice = None
    # iterate until menu 0 is selected to exit
    while choice is not 0:
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
