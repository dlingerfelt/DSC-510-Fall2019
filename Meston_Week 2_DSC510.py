# File: Week 2 Assignment
# Name: Ryan Meston
# Date: 20190903
# Course: DSC510
# Desc: Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Use the SIUE Style Guide as a reference.
# Usage: Retrieve user company info, fiber length, and display receipt for user.
# Display a welcome message for your user.
print("Welcome to your one stop fiber shop!")
# Retrieve the company name from the user.
companyName = input("What is your companies name?")
# Retrieve the number of feet of fiber optic cable to be installed from the user.
fiberLength = input("How much cable do you need in feet?")
# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
installCost = 0.87
a = float(fiberLength)
b = float(installCost)
c = a * b
# Print a receipt for the user including the company name, number of feet to be installed, the calculated cost, and total cost in a legible format.
print("Company Name:", companyName)
print("Number of feet installed:", fiberLength)
print("Total Cost: $", c)
