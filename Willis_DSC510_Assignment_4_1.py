"""
File: Willis_DSC510_Assignment_4_1
Name: Bryan Willis
Date: 9/21/19
Course: DSC510-T303 Introduction to Programming (2201-1)
Assignment Number: 4.1
Description:
This program is a simple estimator. It will ask the user for a company name and the desired feet of fiber.  It will
determine the price based on a the feet of fiber order at a base rate of $ 0.87 per foot and reduce the cost for
large orders; greater than 100 feet will be @ $ 0.80,  greater than 250 feet will be @ $ 0.70, greater than 500 feet
will be @ $ 0.50. All of this data will be used to creates a receipt.

Enhanced Assignment Number 4.1 to include the following requirements:
1) Your program must have a header. Use the SIU Edwardsville Programming Guide for guidance.
2) A welcome message
3) A function with two parameters
4) A call to the function (new)
    This function will perform the cost calculation. The function will have two parameters (feet and price).
5) The application should calculate the cost based upon the number of feet being ordered
6) A printed message displaying the company name and the total calculated cost

Usage:
The program will start by printing a welcome to the estimator message. It then will ask the user for their company name
and reply with a personalized welcome.  Next it will ask the user for the number feet of fiber for the estimate and
reply with a personalized reply.  Finally it will validate the 'feet of fiber' provided, calculate the cost per foot
based on the requested amount and either provide a receipt or an error message.

Below are the references for the items in the code beyond the scope of the examples in the text:
comment block:
Retrieved from https://www.codecademy.com/forum_questions/505ba3cfc6addb000200e33c

"{:0.2f}\n".format():
Retrieved from https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

import time and time.sleep()
Retrieved from https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
"""
import time
fullCostPerFoot = float(.87)   # Variable to store the full cost per foot

def calculateCostPerFoot(x):   # Function used to apply a bulk discount
    global costPerFoot         # Set variable up as global for access outside the function
    if x > 500:
        costPerFoot = float(.50)    # Variable for the cost equation
    elif x > 250:
        costPerFoot = float(.70)
    elif x > 100:
        costPerFoot = float(.80)
    else:
        costPerFoot = float(.87)

def calculateCost(x, y): # Function used calculate the cost using the cost per foot and feet of fiber
     return x * y

def printReceipt():  # Function used to print the receipt
    print("#" * 30)  # Print a sequence of 30 # signs
    print("Receipt:", " " * 14, "#00001")  # Insert 14 spaces between the two items
    print("\r")  # Using a carriage return (\r) to insert a blank line
    print("Company: \n", companyName)
    print("\r")
    print("Feet of Fiber requested: \n", feetOfFiber)
    print("\r")

    if costPerFoot < fullCostPerFoot:    # Create custom receipt
        print("Cost per foot @ full price:\n $", "{:0.2f}".format(fullCostPerFoot))
        print("\r")
        print("Order at full cost:\n $", "{:0.2f}".format(fullPrice))
        print("\r")
        print("Discounted cost per foot:\n $", "{:0.2f}".format(costPerFoot))
        print("\r")
        print("Discount for a bulk order:\n $", "{:0.2f}".format(discountAmount))
    else:
        print("Cost per foot:\n $", "{:0.2f}".format(fullCostPerFoot))

    print("\r")
    print("Total Cost: \n $", "{:0.2f}".format(costOfFiber))  # Convert estimate to two fixed position decimal
    print("#" * 30)

print("Welcome to the Fiber Optic Estimator")  # Welcome message
print("You will be ask for two pieces of information:")
print("   First we will ask for the name of your company")
print("   Followed by a request for number of feet of fiber you would like estimated")

print("\r")
companyName = input("Your Company Name ===> \n")  # Request the feet of fiber from the user

print("\r")
print("Welcome ", companyName, "to our estimator ...")  # Personalize welcome

print("\r")
feetOfFiber = input("Desired Feet of Fiber  ===> \n")  # Request the feet of fiber from the user

print("\r")
print("one moment please while we get your estimate for \"", feetOfFiber,"\" feet of fiber")  # Personalize message
print(" .")

time.sleep(.5)   # Pause 2 Seconds for effect

print("\r")

try:  # Block used to valid the input (int or float)
    fullPrice = calculateCost(float(feetOfFiber), fullCostPerFoot)   # Execute the cost function using the full price
    calculateCostPerFoot(float(feetOfFiber))                         # Executes a function to obtain the discounted price
    costOfFiber = calculateCost(float(feetOfFiber), costPerFoot)     # Execute the cost function using the discounted price
    discountAmount = fullPrice - costOfFiber                         # Calculate the discount amount
    printReceipt()
except ValueError:  # Error message for invalid input
    print("\r")
    print("\r")
    print("We are sorry ", companyName)
    print("We are unable to provide an estimate for \"", feetOfFiber, "\" feet of fiber...")
