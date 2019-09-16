# File: Week 2 Programming Assignment
# Name: Courtney Klatt
# Date: 31 August 2019
# Course: DSC510-T304
# Desc: Calculates cost of fiber optic cable installation
#       based on input of cable length and applies bulk discount
# Usage: Prompts for company name and length of cable required.
#        Prints a receipt for cost of installation.
print("Hello and welcome!")
print("What is your company's name?")
companyName = input()
print("How many feet of fiber optic cable do you need installed?")
feetOfCable = input()
# calculate cost for <=100 ft at $0.87/ft
if float(feetOfCable) <= 100:
    cost1 = float(float(feetOfCable) * float(0.87))
    print("Company: " + companyName)
    print("Total cost: $" + str(cost1))
    print("Total length of fiber optic cable to be installed: "
          + feetOfCable + " feet")
# calculate cost for >100 <=250 ft at $0.80/ft
elif float(feetOfCable) <= 250:
    if float(feetOfCable) > 100:
        cost2 = float(float(feetOfCable) * float(0.80))
        print("Company: " + companyName)
        print("Total cost: $" + str(cost2))
        print("Total length of fiber optic cable to be installed: "
              + feetOfCable + " feet")
# calculate cost for >250 <=500 ft at $0.70/ft
elif float(feetOfCable) <= 500:
    if float(feetOfCable) > 250:
        cost3 = float(float(feetOfCable) * float(0.70))
        print("Company: " + companyName)
        print("Total cost: $" + str(cost3))
        print("Total length of fiber optic cable to be installed: "
              + feetOfCable + " feet")
# calculate cost for >500 ft at $0.50/ft
elif float(feetOfCable) > 500:
    cost4 = float(float(feetOfCable) * float(0.50))
    print("Company: " + companyName)
    print("Total cost: $" + str(cost4))
    print("Total length of fiber optic cable to be installed: "
          + feetOfCable + " feet")
