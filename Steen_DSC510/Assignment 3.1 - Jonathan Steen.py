# File: Assignment 3.1 - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 12/9/2019
# Course: DSC510 - Introduction to Programing
# Desc: Program calculates cost of fiber optic installation.
# Usage:  The program gets company name,
#         number of feet of fiber optic cable, calculate
#         installation cost, bulk discount and print receipt.

#welcome statement and get user input
print('Welcome to the fiber optic installation cost calculator.')
companyName = input('Please input company name.\n')
fiberOpticLength = input('Please input number of feet of fiber optic cable to be installed.\n')

#if statement to calculate bulk discount
fiberOpticCost = 0
if float(fiberOpticLength) > 499:
    fiberOpticCost = .50
elif float(fiberOpticLength) > 249:
    fiberOpticCost = .70
elif float(fiberOpticLength) > 99:
    fiberOpticCost = .80
elif float(fiberOpticLength) < 100:
    fiberOpticCost = .87

#calculate cost
totalCost = float(fiberOpticLength) * float(fiberOpticCost)

#print receipt
print('\n')
print('Receipt')
print(companyName)
print('Costs: ' + str(fiberOpticLength) + ' ft' + ' @ ' + '${:,.2f}'.format(fiberOpticCost) + ' Per Foot')
print('Total: ' + '${:,.2f}'.format(totalCost))
