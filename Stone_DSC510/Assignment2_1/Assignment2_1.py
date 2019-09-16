# 2.1 Programming Assignment Calculate Cost of Cabling
# Name: Zachary Stone
# File: Assignment 2.1.py
# Date: 09/08/2019
# Course: DSC510-Introduction to Programming

# Greeting
print('Welcome to the ABC Cabling Company')
# Get Company Name
companyName = input('What is the name of you company?\n')
# Get Num of feet
feet = float(input('How any feet of fiber optic cable do you need installed?\n'))
# calculate cost
cost = float(feet*0.87)

# print receipt
print("********Receipt********")
print('Thank you for choosing ABC Cable Company.\n')
print('Customer:', companyName)
print('Feet of fiber optic cable:', feet)
print('Cost per foot:', '$0.87')
print('The cost of your installation is', '${:,.2f}'.format(cost))
print('Thank you for your business!\n')
