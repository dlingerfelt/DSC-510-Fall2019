# File: Cost Estimate.py
# Name: Vilius Smilinskas
# Date: 11/29/2019
# Course: DSC510: Introduction to Programming
# Desc: Program calculates the cost of installation per foot of fiber cable.
# Usage: The program will prompt for the name of the company and the number of
#       feet of cable to install

import sys #importing "sys" module to be able to execute sys.exit() later
install_cost = .87    #set up variables
print('Welcome to the Cost Estimtor')
print('Please enter your company name:')
company_name = input()  # stores company name
print('Please enter the amount of fiber cable desired in feet:')
cable_amount = input()  # store amount of cable
while True: #start an infinite loop

    try: #attempt to process information IF Input is incorrect and can't be turnt into a float variable go to LINE 24
        cable_amount_float = float(cable_amount)
        cable_amount_float = round(calc_cost,2) #round the calculated cost
        calc_cost = float(cable_amount) * install_cost
        print('Here is your receipt:')
        print('Company Name: ' + company_name)
        #variables have to be turnt into a string usting the str() function
        #to be combined together into a longer string
        print('Number of feet: ' + str(cable_amount) + ' * Cost per foot: $' + str(install_cost))
        print('Calculated cost: ' + '$' + str(calc_cost))
        print('Total cost: ' + '$' + str(calc_cost))
        sys.exit() #ends the loop together with the program

    except ValueError: #IF above section causes error, trigger this section
        print('Invalid')
        print('Please enter the number of feet:')
        cable_amount = input() #requests for inout again

