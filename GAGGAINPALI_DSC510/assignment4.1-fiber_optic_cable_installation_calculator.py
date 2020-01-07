# File : assignment4.1-fiber_optic_cable_installation_calculator.py
# Name : Bhargava Gaggainpali
# Date : DEC-22-2019
# Course : Introduction to Programming - python
# Assignment :
# -This week we will modify our If Statement program to add a function to do the heavy lifting.
# -Modify your IF Statement program to add a function. This function will perform the cost calculation. The function will have two parameters (feet and price). When you call the function, you will pass two arguments to the function; feet of fiber to be installed and the cost (remember that price is dependent on the number of feet being installed). You probably should have the following:
# -Your program must have a header. Use the SIU Edwardsville Programming Guide for guidance.
# -A welcome message
# -A function with two parameters
# -A call to the function
# -The application should calculate the cost based upon the number of feet being ordered
# -A printed message displaying the company name and the total calculated cost
# Desc : Program to calculate cost of fiber optic cable installation
# Usage :
# -This program is built to take the 'Company Name' & 'required length(in feet)' of cable for installation as input.
# - Calculate the total cost for installation.
# - Print receipt for the total cost for installation to user.

# Function to calculate the cost of installation per foot based on the discount price.
def discount_price(cable_length: float):
    if (cable_length > 100 and cable_length <= 250):
        return 0.80
    elif (cable_length > 250 and cable_length <= 500):
        return 0.70
    elif cable_length > 500:
        return 0.50
    else:
        return 0.87

# Function to calculate the total cost of installation
def calculate_total(cable_length: float, cost: float):
    return cable_length * cost

# actual program start - main
def main():
#Display a welcome message for your user
    print('\nWelcome to the Fiber Optic Cable Cost Calculator..!!')
    #Retrieve the company name from the user
company_name: str = input("\nPlease enter the name of your Company :\n")
#Retrieve the number of feet of fiber optic cable to be installed from the user
print('\n**Fiber Optic Cable Installation Cost is subjected for bulk discount:**')
print('$0.87 per foot for lenght < 100 foot.')
print('$0.80 per foot for lenght > 100 foot.')
print('$0.70 per foot for lenght > 250 foot.')
print('$0.50 per foot for lenght > 500 foot.')

while True:  # making sure the entered input is valid number
        try:
            cable_length: float = float(input('\nPlease enter the length (in feet) of fiber optic cable to be installed :\n'))
            if (cable_length < 0):
                print('Value entered is an Invalid value - Fiber Optic Cable Length must be a Positive number. Please try again.')
                continue
            else:
                break
        except ValueError:
            print('Value entered is an Invalid value - Fiber Optic Cable Length must be a Positive number. Please try again.')

# Calculate the installation cost per feet based on the discount price.
cost = float(discount_price(cable_length))
#Calculate the installation cost of fiber optic cable by multiplying the number of feet times the discount price.
total_cost: float = round(calculate_total(cable_length, cost),2)   # Rounding the cost to 2 decimal points.

'''Print a receipt for the user including the company name, 
number of feet of fiber to be installed, 
the calculated cost, 
and total cost in a legible format'''

print('\nPrinting Receipt for total Cost to install fiber optic cable for Company : ', company_name)
print('Length (in feet) of fiber optic cable to be installed: ' ,cable_length)
print('Cable installation Cost Calculation: ',cable_length,'ft x $',cost)
print('Total Cost for cable installation:','${:,.2f}'.format(total_cost))

if __name__ == '__main__':
    main()
