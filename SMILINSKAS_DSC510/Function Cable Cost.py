# File: Function Cable Cost.py
# Name: Vilius Smilinskas
# Date: 12/22/2019
# Course: DSC510: Introduction to Programming
# Desc: Program calculates the cost of installation per foot of fiber cable, while utilizing a function
# Usage: The program will prompt for the name of the company and the number of
#       feet of cable to install and return a receipt with the appropriate cost


def bulk(cable):  # cable is the amount of cable
    """Sets the install cost and triggers the receipt function"""
    install_cost = .87
    if cable > 100:
        install_cost = .80
    if cable > 250:
        install_cost = .70
    if cable > 500:
        install_cost = .50
    receipt(cable, install_cost)


def receipt(x, y):
    """Prints out the receipt where x is the amount of cable and y is the cost per foot"""
    print('Here is your receipt:')
    print('Company Name: ' + company_name)
    print('Number of feet: ' + str(x) + ' * Cost per foot: $' + str(y))
    print('Calculated cost: ' + '$' + str(x*y))


print('Welcome to the Cost Estimator')
print('Please enter your company name:')
company_name = input()  # stores company name
print('Please enter the amount of fiber cable desired in feet:')
amount = input()  # store amount of cable
while True:
    try:  # attempt to process information IF Input is incorrect and can't be turned into a float variable go to LINE 39
        float_amount = float(amount)
        break  # will break the while loop
    except ValueError:  # if the above try block causes an error, trigger this block
        print('Invalid')
        print('Please enter the number of feet:')
        amount = input()  # requests for inout again

bulk(float_amount)  # call defined function
