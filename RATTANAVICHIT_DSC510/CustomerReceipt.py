# File: CustomerReceipt.py
# Name: Khouanekham Rattanavichit
# Date: 9/8/19
# Course: DSC 510-T304 Introduction to Programming (2201-1)
# Desc: First, the program calculates the installation cost of fiber
#       optic cable by multiplying the total cost as the
#       number of feet times $0.87.
#       Second, the program prints a receipt for the user
#       including the company name, number of feet of fiber to be
#       installed, the calculated cost, and the total cost in legible
#       format.
# Usage: Displays a welcome message to the user. User then types in
#        user's company name and the number of feet of fiber optic
#        cable to be installed.

# Declare the price of fiber optic cable per feet as a constant.
PRICE_OF_CABLE = 0.87

# Display a welcome message for the user.
print("Welcome valued customer!")

# Retrieve the company name from the user and store it in a variable
# named user_company_name.
user_company_name = input("Enter your company's name: ")

# Retrieve the number of feet of fiber optic cable to be installed from
# the user and store it in a variable named length_of_cable.
length_of_cable = input("Fiber optic cable required for installation (in feet)?: ")

# Cast the value stored in variable length_of_cable to a float for math operations.
amount_of_cable = float(length_of_cable)

# Calculate the installation cost.
calculated_install_cost = (amount_of_cable * PRICE_OF_CABLE)

# Format the total cost to two decimal places and round to a whole penny.
total_install_cost = round(calculated_install_cost, 2)

# Print the customer's receipt including company name, amount of fiber optic cable
# in feet, calculated cost, and total cost.
print('---------------------------------------------')
print("               CUSTOMER RECEIPT\n")
print("Company: ", user_company_name)
print("-------")
print("Amount of fiber optic cable purchased:", amount_of_cable, "(feet)")
print("-------------------------------------")
print("Calculated Cost:", calculated_install_cost)
print("---------------")
print("Total Cost: $", total_install_cost)
print("----------")
print("Thank you for your business!")
print("---------------------------------------------")


