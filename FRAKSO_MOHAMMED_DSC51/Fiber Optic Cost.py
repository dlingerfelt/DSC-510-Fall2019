'''
File: Fiber optic Cost.py
Name: Mohammed A. Frakso
Date: 08/12/2019
Course: DSC_510 - Introduction to Programming
Desc: Programe calculates the need of fiber optic cable for a user
Usage : This program is built to take the 'Company Name' and 'required length(in feet)' of optic cable for installation as input.
 Then Calculate the total cost for installation and printing receipt for the total cost for installation to user.
'''
# Display Welcome Message
message = "Welcome to the store"
print(message)

# Retrieve the company name
companyName = input('What is your company name? \n')
print('Your company name is', companyName)


# Retrieve the number of fiber optic
prompt = 'What is the number of feet of fiber optic cable to be installed from the user? \n'
numberFeet = float(input(prompt))
int(numberFeet)


# Calculate the installation cost of fiber optic
# Create a variable
cost = 0.87

# Print Number feet
print(' The number of feet of fiber optic is', numberFeet)
print(numberFeet)

# Calculate the installation cost of fiber optic
totalCost = (numberFeet * cost)
print("The installation cost is", totalCost)

# Printing out the receipt
print('Printing Receipt for Company: ', companyName)
print('Length of  Fiber optic Cable in Feet: ', numberFeet)
print('Cable installation Cost Calculation:', numberFeet,'ft x $',cost)
print('Total Cost: $', totalCost )