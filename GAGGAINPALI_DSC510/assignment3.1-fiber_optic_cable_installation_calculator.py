# File : assignment3.1-fiber_optic_cable_installation_calculator.py
# Name : Bhargava Gaggainpali
# Date : DEC-15-2019
# Course : Introduction to Programming - python
# Assignment :
#-This week we will implement “if statements” in a program. Your program will calculate the cost of fiber optic cable installation by multiplying the number of feet needed by $0.87. We will also evaluate a bulk discount. You will prompt the user for the number of fiber optic cable they need installed. Using the default value of $0.87 calculate the total expense. If the user purchases more than 100 feet they are charged $0.80 per foot. If the user purchases more than 250 feet they will be charged $0.70 per foot. If they purchase more than 500 feet, they will be charged $0.50 per foot.
#-Your program must have a header. Use the SUI--Edwardsville Programming Style Guide for guidance.
#-Display a welcome message for your program.
#-Get the company name from the user.
#-Get the number of feet of fiber optic cable to be installed from the user.
#-Evaluate the total cost based upon the number of feet requested.
#-Display the calculated information including the number of feet requested and company name.
# Desc : Program to calculate cost of fiber optic cable installation
# Usage :
# -This program is built to take the 'Company Name' & 'required length(in feet)' of cable for installation as input.
# - Calculate the total cost for installation.
# - Print receipt for the total cost for installation to user.
#
#Display a welcome message for your user
print('\nWelcome to the Fiber Optic Cable Cost Calculator..!!')

#Retrieve the company name from the user
company_name=input("\nPlease enter the name of your Company :\n")

#Retrieve the number of feet of fiber optic cable to be installed from the user
print('\n**Fiber Optic Cable Installation Cost is subjected for bulk discount:**')
print('$0.87 per foot for lenght < 100 foot.')
print('$0.80 per foot for lenght > 100 foot.')
print('$0.70 per foot for lenght > 250 foot.')
print('$0.50 per foot for lenght > 500 foot.')

while True:
  try:
      cable_length = float(input('\nPlease enter the length (in feet) of fiber optic cable to be installed : \n'))
  except ValueError:
    print('Value entered is an Invalid value - Fiber Optic Cable Length must be a Positive number. Please try again.')
    continue
  if cable_length<=0:
    print('Fiber Optic Cable Length must be a Positive number. Please try again.')
  else:
    break

#Calculate the installation cost of fiber optic cable by multiplying the number of feet times the discount price.
if (cable_length>100 and cable_length<=250):
    cost = 0.80
elif (cable_length>250 and cable_length<=500):
  cost=0.70
elif cable_length>500:
  cost=0.50
else:
  cost=0.87

total_cost=round(cable_length*cost,2)   # Rounding the cost to 2 decimal points.

'''Print a receipt for the user including the company name, 
number of feet of fiber to be installed, 
the calculated cost, 
and total cost in a legible format'''

print('\nPrinting Receipt for total Cost to install fiber optic cable for Company : ', company_name)
print('Length (in feet) of fiber optic cable to be installed: ' ,cable_length)
print('Cable installation Cost Calculation: ',cable_length,'ft x $',cost)
print('Total Cost for cable installation:','${:,.2f}'.format(total_cost))