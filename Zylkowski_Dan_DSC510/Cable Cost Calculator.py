# File: Cable Cost Calculator.py
# Name: Dan Zylkowski
# Date: 9/8/19
# Course: DSC 510 Introduction to Programming
# Assignment 2.1
# Desc: The program calculates the installation cost of fiber optic cable
#       and prints a receipt.
# Usage: The program prompts the user for the name of their Business
#        and the length of cable to be installed.

print("Welcome to the fiber optic cable cost calculator.\n")
company_name=input("Please enter your company name:")
cable_length=float(input("Please enter the number of feet of fiber optic"
                   " cable to be installed: "))
install_cost=float(cable_length*.87) # Calculates the installation cost

print("\n") # line break to separate user input from receipt
print("-" * 13 + "RECEIPT" + "-" * 13 ) # start of receipt
print("\nCompany Name: " + company_name)
print("\nFiber Optic cable requested: " + str(cable_length) + " ft")
print("Total Cost: " + "$"+ str(install_cost))
print("\nThank you and please come again!\n")
print("-" * 13 + "RECEIPT" + "-" * 13 ) # end of receipt

