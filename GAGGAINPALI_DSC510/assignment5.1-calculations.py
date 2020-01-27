# File : assignment5.1-calculations.py
# Name : Bhargava Gaggainpali
# Date : JAN-12-2020
# Course : Introduction to Programming - python
# Assignment :
#-Your program must have a header. Use the programming style guide for guidance.
#-This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
#-This program will contain a variety of loops and functions.
#-The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
#-Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
#-This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
#-This function will print the calculated value for the end user.
#-Define a function named calculateAverage which takes no parameters.
#-This function will ask the user how many numbers they wish to input.
#-This function will use the number of times to run the program within a for loop in order to calculate the total and average.
#-This function will print the calculated average.
#-This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
#-The main program should prompt the user for the operation they wish to perform.
#-The main program should evaluate the entered data using if statements.
#-The main program should call the necessary function to perform the calculation.
# Desc : Program to calculate the math operation between two numbers and calculate sum and average.
# Usage :
# -This program is built to take the math operation +,-,*,/ and two numbers to calculate sum/average for the given numbers.


def performCalculation(x):
    #Perform the calculation for (+,-,*,/) will ask user to input 2 numbers.
    user_num1 = float(input('Enter your first number: \n'))
    user_num2 = float(input('Enter your second number: \n'))
    if x == '+':
        print('Sum of two numbers is', user_num1 + user_num2)
    elif x == '-':
        print(user_num1, ' minus ', user_num2, 'is', user_num1 - user_num2)
    elif x == '*':
        print('multiplication of two numbers is', user_num1 * user_num2)
    elif x == '/':
        print(user_num1, ' divided by ', user_num2, 'is', user_num1 / user_num2)


def calculateAverage():
    # Perform the calculation of average, will ask user to input 2 numbers.
    num = int(input('Please enter the number of values would you like to average:'))
    total_sum = 0
    for n in range(num):
        numbers = float(input('Enter the number : '))
        total_sum += numbers
    avg = total_sum/num
    print('Average of', num, 'numbers is :', avg)

if __name__ == "__main__":
    op_set = ['+', '-', '*', '/']
    print('Welcome to the Math Calculations...!!')
    print('Choose to Enter one of the functions (+, -, *, /, average) to calculate or none to exit.')

    while True:
        print('----------------------------------------------------------------------------------------------')
        user_info = input('Please enter the operation you like to use? (+, -, *, /, average) or none to exit the program:')
        if user_info in op_set: # this will ask the user to input 2 numbers and preform calculation.
            performCalculation(user_info)
            continue
        if user_info == 'average': # this will ask the user how many numbers they wish to average and preform the calculation.
            calculateAverage()
            continue
        if user_info == 'none': # this will close the program and let the user know they are all done.
            break
    print('Thank you for using the Math Calculations program.')
