'''
    This program will show welcome message to user and ask for company name,
    and take the number of feet fiber optics cable he wants to install.
    Calculate the installation cost by multiplying by 0.87.

    Author: Sanjay Jaras
    Assignment: 2.1
'''
# print welcome message
print("Welcome !!!")
# get company name from user
company_name = input("Please enter company name:")
# get number of feet
feet = input("Please enter the cable in length in feet:")
rate_per_feet = 0.87
# Calculate installation cost
installation_cost = float(feet) * rate_per_feet
line_length = 100
# Print result
print("\n", "*" * line_length, end="\n\n")
print(" " * ((line_length // 2) - len(company_name)), company_name, end="\n\n")
print("*" * line_length, end="\n\n")
print("Cable length:\t", feet, end="\t" * 12)
print("Installation cost per feet:\t", rate_per_feet, "$", end="\n\n")
print("Calculated cost:", installation_cost, "$", end="\t" * 11)
print("Total cost:", "\t" * 3, installation_cost, "$", end="\n\n")
print("*" * line_length)
