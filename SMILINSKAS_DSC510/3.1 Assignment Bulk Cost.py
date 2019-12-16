# File: Cost Estimate.py
# Name: Vilius Smilinskas
# Date: 12/213/2019
# Course: DSC510: Introduction to Programming
# Desc: Program calculates the cost of installation per foot of fiber cable, including discounts for buying in bulk
# Usage: The program will prompt for the name of the company and the number of
#       feet of cable to install and return a receipt with the appropriate cost

import sys  # importing "sys" module to be able to execute sys.exit() later
install_cost = .87    # set up variables
print('Welcome to the Cost Estimator')
print('Please enter your company name:')
company_name = input()  # stores company name
print('Please enter the amount of fiber cable desired in feet:')
cable_amount = input()  # store amount of cable
while True:
    try:  # attempt to process information IF Input is incorrect and can't be turned into a float variable go to LINE 36
        cable_amount_float = float(cable_amount)
        # test for bulk pricing
        if cable_amount_float > 100:
            install_cost = .80
        if cable_amount_float > 250:
            install_cost = .70
        if cable_amount_float > 500:
            install_cost = .50
        calc_cost = cable_amount_float * install_cost
        calc_cost = round(calc_cost, 2)  # round the calculated cost
        print('Here is your receipt:')
        print('Company Name: ' + company_name)
        # variables have to be turned into a string using the str() function
        # to be combined together into a longer string
        print('Number of feet: ' + str(cable_amount_float) + ' * Cost per foot: $' + str(install_cost))
        print('Calculated cost: ' + '$' + str(calc_cost))
        print('Total cost: ' + '$' + str(calc_cost))
        sys.exit()  # ends the loop together with the program
    except ValueError:  # if the above try block causes an error, trigger this block
        print('Invalid')
        print('Please enter the number of feet:')
        cable_amount = input()  # requests for inout again
