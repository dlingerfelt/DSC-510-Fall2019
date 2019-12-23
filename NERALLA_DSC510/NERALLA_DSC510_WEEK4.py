# File: NERALLA_DSC510_WEEK4.py
# Name: Ravindra Neralla
# Course:DSC510-T303
# Date:12/21/2019
# Description: Calculate Total Cost of FiberOptic Cable Installation
# *********************************************************************
#		    Display Welcome message with company name
#			Get the Total feet of cable to be installed from the user
#			Validate the user input, i.e. cable length must be positive number
#           Calculate the discount to be applied, based on the cable length
#			Calculate the total cost, based on the above discount
#			Print receipt, with company name and currency formatted
#			Use python functions with arguements
# ***********************************************************************
# Below function calculates the bulk discount to be applied based on total length of fiber
def discount_rate(cable_length: float):
    if 100 < cable_length <= 250:
        price_per_feet = 0.80
    elif 250 < cable_length <= 500:
        price_per_feet = 0.70
    elif cable_length > 500:
        price_per_feet = 0.50
    else:
        price_per_feet = 0.87
    return price_per_feet

# This function is to calculate the total cost
def total_cost(cable_length: float, price_per_feet: float):
    total_price = cable_length * price_per_feet
    return total_price

# main is the function, where the actual program execution starts from
def main():
# Display Welcome message
    print("Welcome to FiberOptics Inc");
# User to enter company name
    company_name = input("Please enter your company name: \n")
    print(company_name)
# Validate user entered cable length
    while True:
        try:
            cable_length = float(input('\nHow many feet of fiber optic cable to be installed?\n'))
            if cable_length <= 0:
                print('Cable Length must be a positive number')
                continue
            else:
                break
        except ValueError:
            print('Cable Length must be a number')
     # Calculate the discount price, based on cable length using the function defined above
    price_per_feet = discount_rate(cable_length)

    # Calculate the total cost of instllation, using discount price feet and total length
    total_price = total_cost(cable_length, price_per_feet)
    # printing receipt
    print('\nRECEIPT')
    print("Company Name: ", company_name)
    print("Total Number of Feet of FiberOptic Cable to be Installed: ", cable_length)
    print("Price Per Cubic feet: ", price_per_feet)
    print("Total Cost of Installation:", '${:,.2f}'.format(total_price))
if __name__ == '__main__':
    main()
