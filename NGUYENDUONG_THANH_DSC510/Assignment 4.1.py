"""
File: Assignment_4.1.py
Author: Thanh Nguyen-Duong
Date: 9/19/19
Course: DSC 510-T304 Fall 2019
Assignment: 4.1
Desc: This program displays a welcome message. Then retrieves a company name &
    the number of feet of fiber optic cable to be installed from the user.
    Evaluates the installation cost of fiber optic cable based on number of feet requested with bulk discount using
    a function with two parameters.
    Prints a receipt for the user with company name, number of feet of fiber installed, calculated cost,
    cost per foot based on number of feet requested, and total cost.
    Include appropriate comments throughout the program.
Usage: Prompts user for input of company name and number of feet of fiber optic cable.
       Calculate the installation cost based on number of feet requested and apply bulk discount.
       performs calculations and outputs a receipt for fiber optic cable installed.
"""


from datetime import datetime

def get_costPerFoot(lengthInFeet):
    """
    This function will calculate the cost per foot based on the length of optic fiber in feet.
    greater or equal to 500 feet = $0.50/foot
    greater or equal to 250 feet = $0.70/foot
    greater or equal to 100 feet = $0.80/foot
    less than 100 feet = $0.87/foot
    """
    if lengthInFeet >= 500:
        costPerFoot = 0.50
    elif lengthInFeet >= 250:
        costPerFoot = 0.70
    elif lengthInFeet >= 100:
        costPerFoot = 0.80
    else:
        costPerFoot = 0.87
    return costPerFoot


def calculateTotalCost(lengthInFeet, costPerFoot):
    """
    This function will calculate total cost by multiplying the length in feet and cost per foot

    """
    return lengthInFeet*costPerFoot

#######################################################################


# Display Welcome Message to user
Name = input("What is your name?")
print("Welcome to the Store,", Name, "!")

# Retrieve company name from user
Company_Name = input("What is your company name?")

# Retrieve number of feet of fiber optic cable to be installed from user
length_in_Feet = float(input("How many feet of fiber optic cable do you need to install?"))

# Calculate cost per foot, round to 2 decimal places
cost_per_foot = round(get_costPerFoot(length_in_Feet), 2)

# calculate the total cost
totalCost = round(calculateTotalCost(length_in_Feet, cost_per_foot), 2)

# Print a receipt for user including company name, number of feet to be installed, cost per foot, total cost
print("Receipt")

today = datetime.today()
print(today.strftime("%m/%d/%y %I:%M"))

print("Company:", Company_Name)
print("Number of feet of fiber to be installed =", length_in_Feet)
print("Cost per foot =", cost_per_foot)
print("Total Cost =", totalCost)
