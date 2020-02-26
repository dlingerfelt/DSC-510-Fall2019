'''
File: FiberOptic If_Statments.py
Name: Mohammed A. Frakso
Date: 21/12/2019
Course: DSC_510 - Introduction to Programming
Desc: Programe calculates the need of fiber optic cable and  evaluate a bulk discount for a user
Usage : This program uses functions to take the 'Company Name' and 'required length(in feet)' of optic cable for installation as input.
 Then Calculate the total cost that will vary upon the length of optic cable requested for installation and printing receipt for the total cost for installation to user.
'''
# Display Welcome Message
message = "Welcome to the store"
print(message)

# Retrieve the company name
companyName = input('What is your company name? \n')
print('Your company name is', companyName)


# Retrieve the number of fiber optic
prompt = 'What is the number of feet of fiber optic cable to be installed? \n'
numberFeet = float(input(prompt))
int(numberFeet)


# Calculate the installation cost of fiber optic
# Create a variable
cost = 0.87

# Print Number feet
print(' The number of feet of fiber optic is', numberFeet)
print(numberFeet)

# Function for cable cost

if 100 < numberFeet <= 250:  # If Cabal length is between 101 and 250 then price is 0.80
        cost = 0.80
elif 250 < numberFeet <= 500:  # If Cabal length is between 251 and 500 then price is 0.70
        cost = 0.70
elif numberFeet > 500:  # If Cabal length is more than 500 then price is 0.5
        cost = 0.50
else:
        cost = 0.87  # If Cabal length is less than 100 then price is 0.87


# Function with 2 parameters to Calculate the installation cost of fiber optic

def calculateTotalCost(x, y):
    global totalCost
    totalCost = float(x) * float(y)
    return totalCost

# calling the function

calculateTotalCost(numberFeet, cost)
print("The installation cost is", totalCost)

# Printing out the receipt
print('Company name: ', companyName)
print('Length of  Fiber optic Cable in Feet: ', numberFeet)
print('Cable installation Cost Calculation:', numberFeet,'ft x $',cost)
print('Total Cost: $', totalCost )