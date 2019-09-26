# File: Week 3 Assignment
# Name: Ryan Meston
# Date: 20190910
# Course: DSC510
# Desc: Week 3 assignment
# Usage: Retrieve name from user, get number of feet of fiber from user, evaluate cost based on feet of fiber, display calculated info including feet requested and company name.
# Display a welcome message.
print("Welcome to your one stop fiber shop!")
# What is the user's company name.
print("What is your companies name?")
companyName = input()
# How many feet of cable does the user need.
print("How much cable do you need in feet?")
fiberLength = input()
# Evaluate bulk discount.
# Default install cost is $0.87
# More than 100 feet is $0.80.
# More than 250 feet is $0.70.
# More than 500 feet is $0.50.
if float(fiberLength) <= 100:
    cost1 = float(float(fiberLength) * float(0.87))
    print("Company: " + companyName)
    print("Total cost: $" + str(cost1))
    print("Total length of fiber optic cable to be installed: "
          + fiberLength + " feet")
elif float(fiberLength) <= 250:
    if float(fiberLength) > 100:
        cost2 = float(float(fiberLength) * float(0.80))
        print("Company: " + companyName)
        print("Total cost: $" + str(cost2))
        print("Total length of fiber optic cable to be installed: "
              + fiberLength + " feet")
elif float(fiberLength) <= 500:
    if float(fiberLength) > 250:
        cost3 = float(float(fiberLength) * float(0.70))
        print("Company: " + companyName)
        print("Total cost: $" + str(cost3))
        print("Total length of fiber optic cable to be installed: "
               + fiberLength + " feet")
else:
    if float(fiberLength) > 500:
        cost4 = float(float(fiberLength) * float(0.50))
        print("Company: " + companyName)
        print("Total cost: $" + str(cost4))
        print("Total length of fiber optic cable to be installed: "
               + fiberLength + " feet")
