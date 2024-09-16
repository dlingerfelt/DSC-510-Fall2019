'''
File: welcome.py
Name: Chris Goodwin
Date: 9/5/19
Course: DSC510 - Introduction to Programming
Desc: Program provides a receipt for fiber optic cable
Usage: User inputs company name and number of feet of fiber optic cable
       needed
'''
#printing welcome message with linebreaks for cleaner look
welcome = '*** Welcome to Goodwin\'s Fiber Optic Company! ***'
print('\n\n',welcome,'\n\n')

company = input('Please enter your company name: ') #collecting company name
num_feet_raw = input('Please enter the number of feet of fiber optic cable to be installed: ') #collecting number of feet of fiber optic cable

'''
the following lines verify that the user entered an actual number for the number of feet prompt. If they entered a string, they will be prompted to enter a new value
'''

try:
  num_feet_float = float(num_feet_raw)
except ValueError:
  print('\nThe value you entered is invalid! Please enter an actual number.\n')
  num_feet_raw = input('Please enter the number of feet of fiber optic cable to be installed:')
  num_feet_float = float(num_feet_raw)

cost_raw = num_feet_float * .87 #calculating the cost
cost_round = round(cost_raw,2) #rounds value to 2 decimal points to represent a true monetary value

#The following lines print a receipt for the user
print('\n\n---\nFINAL RECEIPT\n','Company Name: ',company,'\n','Total number of feet of fiber to be installed: ',num_feet_float,'\n','Cost per foot: $0.87\n','Total Cost for this order: $',cost_round,'\n---',sep='')
