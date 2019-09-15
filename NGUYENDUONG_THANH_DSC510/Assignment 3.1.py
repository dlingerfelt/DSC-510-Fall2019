"""
File: Assignment_3.1.py
Author: Thanh Nguyen-Duong
Date: 9/12/19
Course: DSC 510-T304 Fall 2019
Assignment: 3.1
Desc: This program displays a welcome message. Then retrieves a company name &
    the number of feet of fiber optic cable to be installed from the user.
    Evaluates the installation cost of fiber optic cable based on number of feet requested with bulk discount.
    Prints a receipt for the user with company name, number of feet of fiber installed, calculated cost,
    cost per foot based on number of feet requested, and total cost.
    Include appropriate comments throughout the program.
Usage: Prompts user for input of company name and number of feet of fiber optic cable.
       Calculate the installation cost based on number of feet requested and apply bulk discount.
       performs calculations and outputs a receipt for fiber optic cable installed.
"""
from datetime import datetime
# Display Welcome Message to user
Name = input("What is your name?")
print("Welcome to the Store,", Name, "!")

# Retrieve company name from user
Company_Name = input("What is your company name?")

# Retrieve number of feet of fiber optic cable to be installed from user
Fiber = float(input("How many feet of fiber optic cable do you need to install?"))

# Calculate installation cost based on number of feet requested
if Fiber >= 500:
    Subtotal = 0.50 * Fiber             # more than 500 feet, $0.50 per foot
elif Fiber >= 250:
    Subtotal = 0.70 * Fiber             # more than 250 feet, $0.70 per foot
elif Fiber >= 100:
    Subtotal = 0.80 * Fiber             # more than 100 feet, $0.80 per foot
else:
    Subtotal = 0.87 * Fiber             # less than 100 feet, $0.87 per foot

# Calculate cost per feet, round to 2 decimal places
Cost_per_foot = round(Subtotal/Fiber, 2)

# Calculate Tax amount with CA sales tax of 9.25%, round to 2 decimal places
Tax = round(Subtotal * 0.0925, 2)

# Calculate Total cost with Tax Included, round to 2 decimal places
Total_cost = round(Subtotal + Tax, 2)

# Print a receipt for user including company name, number of feet to be installed, calculated cost, total cost
print("Receipt")

today = datetime.today()
print(today.strftime("%m/%d/%y %I:%M"))

print("Company:", Company_Name)
print("Number of feet of fiber to be installed =", Fiber)
print("Cost per foot =", Cost_per_foot)
print("Subtotal =", round(Subtotal, 2))
print("Sales Tax 9.25% =", Tax)
print("Total Cost =", Total_cost)
