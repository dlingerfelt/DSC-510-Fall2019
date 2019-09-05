"""
File: Assignment_2.1.py
Author: Thanh Nguyen-Duong
Date: 9/5/19
Course: DSC 510-T304 Fall 2019
Assignment: 2.1
Desc: This program displays a welcome message. Then retrieves a company name &
    the number of feet of fiber optic cable to be installed from the user.
    Calculates the installation cost of fiber optic cable by multiplying by $0.87
    Prints a receipt for the user with company name, number of feet of fiber installed, calculated cost, and total cost
    Include appropriate comments throughout the program.
Usage: Prompts user for input of company name and number of feet of fiber optic cable.
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

# Cost of installation of fiber optic cable in feet * cost per feet ($0.87)
Cost_per_feet = 0.87
Subtotal = Fiber * Cost_per_feet

# Calculate Tax amount with CA sales tax of 9.25%
Tax = Subtotal * 0.0925

# Calculate Total cost with Tax Included
Total_cost = Subtotal + Tax

# Print a receipt for user including company name, number of feet to be installed, calculated cost, total cost
print("Receipt")

today = datetime.today()
print(today.strftime("%m/%d/%y %I:%M"))

print("Company:", Company_Name)
print("Number of feet of fiber to be installed =", Fiber)
print("Subtotal =", Subtotal)
print("Sales Tax 9.25% =", Tax)
print("Total Cost =", Total_cost)
