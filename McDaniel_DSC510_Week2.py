# File: McDaniel_DSC510_Week2.py
# Name: Brian McDaniel
# Date: 09/08/2019
# Course: DSC510 Introduction to Programming, Section T303
# Desc: This program calculates a cost for Fiber Optic Cable installation and prints a receipt.
#       It prompts the user for a company name and length of fiber optic cable needed.  Cost is
#       calculated at $0.87 per foot.
# Usage: The user types in company name and length.  Imports date to provide today's date.

from datetime import date

todayDate = date.today()
# Setting cost of FiberOptic installation as .87, can change here if needed.
perFootCostFiberOptic = .87

print ('Welcome!  Need some Fiber Optic cable?')

companyName = input('Please enter the name of your company: ')

# Converting the input to a float to avoid error.  Need to figure out correct way later.
numFeetFiberOptic = float(input('Enter how many feet of fiber optic cable are to be installed: '))

print ('You are requesting ', numFeetFiberOptic, ' of fiber optic cable to be installed.')
jobCostFiberOptic = round(numFeetFiberOptic * perFootCostFiberOptic,2)
print ('The total cost will be $', jobCostFiberOptic, '/(Cost is 87 cents per foot/)')

print ('---------------------------------------------------------')
print ('---     FIBER OPTIC CABLE INSTALLATION RECEIPT        ---')
print ('---------------------------------------------------------')
print ('---  Customer: ' + companyName)
print ('---')
print ('---  Date: ', todayDate)
print ('---  Number of feet requested',numFeetFiberOptic)
print ('---  Cost per foot: $', perFootCostFiberOptic)
print ('---  Total cost of installation: $', jobCostFiberOptic)
print ('---')
print ('---------------------------------------------------------')
print ('---           THANK YOU FOR YOUR BUSINESS             ---')
print ('---------------------------------------------------------')
