# File : assignment2.1-fiber_optic_cable_installation_calculator.py
# Name : Bhargava Gaggainpali
# Date : DEC-08-2019
# Course : Introduction to Programming - python
# Assignment :
# -Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Use the SIUE Style Guide as a reference.
# -Display a welcome message for your user.
# -Retrieve the company name from the user.
# -Retrieve the number of feet of fiber optic cable to be installed from the user.
# -Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# -Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
# -Include appropriate comments throughout the program.
# Desc : Program to calculate cost of fiber optic cable installation
# Usage :
# -This program is built to take the 'Company Name' & 'required length(in feet)' of cable for installation as input.
# - Calculate the total cost for installation.
# - Print receipt for the total cost for installation to user.
#
#Display a welcome message for your user
print('\nWelcome to the Fiber Optic Cable Cost Calculator..!!\n')

#Retrieve the company name from the user
company_name=input("\nPlease enter the name of your Company : \n")

#Retrieve the number of feet of fiber optic cable to be installed from the user
cable_length=float(input('\nPlease enter the length (in feet) of fiber optic cable to be installed : \n'))


#Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87
cost=0.87
total_cost=round(cable_length*cost,2)   # Rounding the cost to 2 decimal points.

'''Print a receipt for the user including the company name, 
number of feet of fiber to be installed, 
the calculated cost, 
and total cost in a legible format'''

print('\nPrinting Receipt for total Cost to install fiber optic cable for Company : ', company_name)
print('Length (in feet) of fiber optic cable to be installed: ' ,cable_length)
print('Cable installation Cost Calculation: ',cable_length,'ft x $',cost)
print('Total Cost for cable installation: $',total_cost)
