# File: Week 2 Programming Assignment
# Name: Courtney Klatt
# Date: 30 August 2019
# Course: DSC510-T304
# Desc: Calculates cost of fiber optic cable installation based on input of cable length at a fixed cost ($0.87/ft)
# Usage: Prompts for company name and length of cable required. Prints a receipt for cost of installation.
print("Hello and welcome!")
print("What is your company's name?")
companyName = input()                                                # input company name
print("How many feet of fiber optic cable do you need installed?")
feetOfCable = input()                                                # input length of cable needed
cost = float(float(feetOfCable) * float(0.87))                       # calculate cost at $0.87/ft
print("Company: " + companyName)
print("Total cost: $" + str(cost))
print("Total length of fiber optic cable to be installed: " + str(feetOfCable) + " feet")
