# File: Week 5 Assignment
# Name: Ryan Meston
# Date: 201909229
# Course: DSC510
# Desc: Week 5 Assignment
# Usage: performCalculation - parameter will be the operation being performed (+,-,*,/). calculateAverage - no parameters. Ask user for function and numbers to be entered.


def performCalculation(x):
    '''
    defines the calculation we will be using (+,-,*,/).
    we will ask user to input 2 numbers.
    '''
    user_num1 = float(input('Enter your first number: \n'))
    user_num2 = float(input('Enter your second number: \n'))
    if x is '+':
        print('Your answer is', user_num1 + user_num2)
    elif x is '-':
        print('Your answer is', user_num1 - user_num2)
    elif x is '*':
        print('Your answer is', user_num1 * user_num2)
    elif x is '/':
        print('Your answer is', user_num1 / user_num2)


def calculateAverage():
    '''
    will ask for numbers to input
    wil calculate average
    '''
    num = int(input('How many numbers would you like to average:'))
    total_sum = 0
    for n in range(num):
        numbers = float(input('Enter number : '))
        total_sum += numbers
    avg = total_sum/num
    print('Average of', num, 'numbers is :', avg)


op_set = ['+', '-', '*', '/']
print('Enter the function out of the operation set you would like to use, or type average or none.')
print('Operation sets to use: +, -, * , /')
while True:
    user_info = input('What operation would you like to use?')
    if user_info in op_set: # this will ask the user to input 2 numbers and preform calculation.
        performCalculation(user_info)
        break
    if user_info == 'average': # this will ask the user how many numbers they wish to average and preform the calculation.
        calculateAverage()
        break
    if user_info == 'none': # this will close the program and let the user know they are all done.
        break
print('Thank you for using are program.')


