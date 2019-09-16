'''
    File: Assignment3-1.py
    Author: Sanjay Jaras
    Assignment: 3.1
    Date:09/10/2019
    Course: DSC 510 - Introduction to programming
    Desc: Program will calculate the installation cost for fiber optic cable.
    Usage: This program will show welcome message to user and ask for company name,
    and take the number of feet fiber optics cable he wants to install.
    Calculate the installation cost as follow
    default rate is $0.87/feet
    >100 feet rate is $0.80/feet
    >250 feet rate is $0.70/feet
    >500 feet rate is $0.50/feet
'''
# print welcome message
print("Welcome !!!")
# get company name from user
company_name = input("Please enter company name:")
# get number of feet
feet = None
while feet is None:
    try:
        feet = int(input("Please enter the cable length in feet:"))
    except:
        print("Please enter valid cable length...", end="\n")
        feet = None

default_rate_feet = 0.87

if feet > 500:
    rate_per_feet = 0.50
elif feet > 250:
    rate_per_feet = 0.70
if feet > 100:
    rate_per_feet = 0.80
else:
    rate_per_feet = 0.87

# Calculate installation cost
installation_cost = default_rate_feet * feet
discounted_price = rate_per_feet * feet
line_length = 100
# Print receipt
print("\n", "*" * line_length, end="\n")
print(" " * ((line_length // 2) - len(company_name)), company_name, end="\n")
print("*" * line_length, end="\n")
print("Cable length:\t", feet, "feet", end="\t" * 10)
print("Installation cost per feet:\t", default_rate_feet, "$", end="\n")
print("Calculated cost:", installation_cost, "$", end="\t" * 11)
print("Total cost:", "\t" * 3, installation_cost, "$", end="\n")

print("Discount :\t", "%2.2f" % (installation_cost - discounted_price), "$", end="\t" * 10)
print("Discounted cost per feet:\t\t", rate_per_feet, "$", end="\n")
print("Discounted  cost:", discounted_price, "$", end="\t" * 11)
print("Discounted Total:", "\t" * 2, discounted_price, "$", end="\n")

print("*" * line_length)
