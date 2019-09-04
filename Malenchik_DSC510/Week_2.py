"""
File:       Week_2.py
Name:       Ali Malenchik
Date:       9/4/2019
Course:     DSC 510 - Introduction to Programming
Assignment: 2.1
Purpose:    This program prompts the user for information about his or her company, along with information
            required for determining cost of fiber optic cable installation. The program uses this information
            to output a receipt with the details of the order and the total cost.
"""

print('Welcome to Fibre-R-Us!\n')

company_name = input('Please enter your company name:\n')

#Prompts user for length of cable installation. If not a positive number, prints an error message.
while True:
      cable_length = input('Please enter the number of feet of fiber optic cable to be installed:\n')
      try:
            float(cable_length)
            if float(cable_length) <0:
                  print("Invalid. Response must be a positive number.")
                  continue
            break
      except ValueError:
            print('Invalid. Response must be a number.')

cost_per_foot = .87

#calculates cost of installation and rounds to two decimal places
total_cost = round(float(cable_length) * cost_per_foot, 2)

# Prints receipt showing total cost of installation
print('=====Receipt=====\n'
      'Company Name:', company_name,'\n'
      'Length of Fiber to be Installed:',cable_length,'feet\n'
      'Cost per Foot: $', cost_per_foot, '\n'
      'Total Cost: $', total_cost)
