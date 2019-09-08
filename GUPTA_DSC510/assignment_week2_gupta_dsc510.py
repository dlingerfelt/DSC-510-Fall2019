'''
File: main.py
Python Version : 3
Name: Rahul Gupta
Date: 9/3/2019
Course: DSC 510 - Inroduction to Programming
Desc: 2.1 Programming Assignment 
 Display a welcome message for your user.
 Retrieve the company name from the user.
 Retrieve the number of feet of fiber optic cable to be installed from the user.
 Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
 Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
 Include appropriate comments throughout the program.
Usage:
    The program prompts the user for 
        1) their company's name
        2) the number of feet of fiber optic cable to purchase
    Then it outputs the billing report for the user containing the company name, installation cost, and number of feet of fiber optic cable that is to be purchased.
'''
# Print Welcome Message
print('Welcome to our site') 

# Ask Company name
print("Please enter your company's name:")
company_name = input()

# Ask no of unit user want
print('how many feet of fiber optic cable would you like to purchase?')
num_feet = int(input())

# Calcutaion
installation_cost = num_feet * 0.87

# Generate Receipt
print(company_name, 'will be billed $', installation_cost, 'for', num_feet, 'feet of fiber optic cable.')
