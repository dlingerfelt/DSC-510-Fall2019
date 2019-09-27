# File: Week 4 Assignment
# Name: Ryan Meston
# Date: 20190920
# Course: DSC510
# Desc: Week 3 assignment
# Usage: Retrieve name from user, get number of feet of fiber from user, evaluate cost based on feet of fiber, display calculated info including feet requested and company name.

def bulk_discount(fiber_length):

    if fiber_length <= 100:
        cost = 0.87
    elif fiber_length <= 250:
        if fiber_length > 100:
            cost = 0.80
    elif fiber_length <= 500:
        if fiber_length > 250:
            cost = 0.70
    else:
        if fiber_length > 500:
            cost = 0.50
    return cost


def overall_price(cost):
    return fiberLength * cost


print('Welcome to your one stop fiber shop!')
print('What is your companies name?')
companyName = input()
print('How many feet of fiber optic cable do you need?')
fiberLength = float(input())
d_cost = bulk_discount(fiberLength)
totalPrice = overall_price(d_cost)
print("Company: " + companyName)
print('Total Cost: $', totalPrice)
print("Total length of fiber optic cable to be installed: "
               + str(fiberLength) + " feet")
