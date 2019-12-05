# File: Assignment 2.1 - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 12/2/2019
# Course: DSC510 - Introduction to Programing
# Desc: Program calculates cost of fiber optic installation.
# Usage:  The program gets company name,
#         number of feet of fiber optic cable, calculate
#         installation cost and prints a receipt.

print('Welcome to the fiber optic installation cost calculator.')

companyName = input('Please input company name.\n')
fiberOpticLength = input('Please input number of feet of fiber optic cable to be installed.\n')

fiberOpticCost = .87 #define the varible to hold the cost per ft of fiber optic.
totalCost = float(fiberOpticLength) * float(fiberOpticCost) #convert user input to float and calculate price.

print('\n')
print('Receipt')
print(companyName)
print('Costs: ' + str(fiberOpticLength) + ' ft' + ' @ ' + '$' + str(fiberOpticCost) + ' Per Foot') #convert float varible to string
totalCost = totalCost - totalCost % 0.01 #format output to two decimal points without rounding up or down to get accurate amount.
print('Total: ' + '$' + str(totalCost))
