#%%
#File: Assignment 5
#Name: April Meyer
#Assignment 5
#Date: 9.26.2019
"""Desc: This program will prompt the user for an arithmetic operation.
It wil then perform the operation and prompt the user for another arithmetic until the user types none."""

#Defines a function named performCalculation which takes one parameter.
#The parameter will be the operation being performed (+, -, *, /).
def performCalculation (x):
    userNum_input = int(input('What is your first number?'))
    userNum_input2 = int(input('What is your second number?'))
    if x in ('+','add','addition'):
        print(userNum_input + userNum_input2)
    elif x in ('-','minus','subtraction'):
        print(userNum_input - userNum_input2)
    elif x in ('*','multiply','multiplication'):
        print(userNum_input * userNum_input2)
    elif x in ('/','divide','division'):
        print(userNum_input / userNum_input2)

#Define a function named calculateAverage which takes no parameters and prints the average
def calculateAverage ():
    userAvg_input = int(input('How many numbers would you like to average?'))
    total = 0
    for i in range(0, userAvg_input): # set up loop to run the amount from the user
        number = int(input('Please enter a number: ')) # prompt user for number for total
        total = total + number
    print('Your average is ', total/userAvg_input) #prints average

cal_set = ['+','add','addition','-','minus','subtraction','*','multiply','multiplication','/','divide','division']
cal_set2 = ['+','add','addition','-','minus','subtraction','*','multiply','multiplication','/','divide','division', 'average']
while True: #loop for user to do calculations & continues until they type none
    userOp_input = input('What arithmetic operation would you like to perform? \n'
                         'Addition(+), Subtraction(-), Multiplication(*), Division(/), Average, or None')
    userOp_input = userOp_input.lower() #converts to lower case
    if userOp_input in cal_set:   #checks if it is in the first list
        performCalculation (userOp_input)
    if userOp_input == 'average': #checks the user input to see if it is average
        calculateAverage()
    if userOp_input == 'none': #breaks the loop if it is user_input is none
        break
    if userOp_input not in cal_set2 : #all other inputs will receive this message
        print('Invalid Option. Please try again')
print('All Done!')
