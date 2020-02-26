# File :    calculator.py
# Name :    Pradeep Jaladi
# Date :    12/09/2019
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#           Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Use the SIUE Style Guide as a reference.
#           Display a welcome message for your user.
#           Retrieve the company name from the user.
#           Retrieve the number of feet of fiber optic cable to be installed from the user.
#           Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times by price by feet purchased.
#               Price is $0.87 if purchased feet is less than are equal to 100
#               Price is $0.80 if purchased feet is between 100 and 251
#               Price is $0.70 if purchased feet is between 250 and 501
#               Price is $0.50 if purchased feet is greater than 500
#               Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
# Desc :    Program to calculate total cost of fiber cable installation
# Usage :
#           The program prompts the user for company name, required feet of fiber optical cable to be installed
#           The program will calculate the cost of prints the receipt for the user
import datetime


# This function will return the cost of fiber cable per foot. It will help to change the price quickly and one place.
def price_per_cable_feet(length_of_fiber_cable: int):
    if 100 < length_of_fiber_cable <= 250:  # Purchased feet between 101 to 250 then price is 0.80
        return 0.80
    elif 250 < length_of_fiber_cable <= 500:  # Purchased feet between 251 to 500 then price is 0.70
        return 0.70
    elif length_of_fiber_cable > 500:  # More than 500 feet then price is 0.50
        return 0.50
    else:
        return 0.87  # default value of $0.87


# This function will calculate the total cost
def calculate_total(length_of_fiber_cable: int, price_per_feet: float):
    return length_of_fiber_cable * price_per_feet


# This function will print the customer receipt
def print_receipt(company_name: str, length_of_fiber_cable: int, total_cost: float):
    now = datetime.datetime.now()
    print('Receipt Date : ' + now.strftime("%Y-%m-%d %H:%M:%S"))  # printing date & time
    print('Invoice for : {0}'.format(company_name))  # printing company name
    print('Purchased length of feet : {:,}'.format(length_of_fiber_cable))  # printing the fiber length
    print('Total cost is : ', total_cost)  # sale price
    print('Total formatted cost is :', '${:,.2f}'.format(total_cost))  # sale formatted price


def main():
    print("Welcome to the store")
    company_name: str = input("Enter your company name \n")
    while True:  # making sure the entered input is valid number
        try:
            length_of_fiber_cable: int = int(input("Enter the length of fiber cable \n"))
            if (length_of_fiber_cable < 0):
                print("Oops!  That was no valid number.  Try again...")
                continue
            else:
                break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    # Getting the price based on length of the feet
    price_per_feet = price_per_cable_feet(length_of_fiber_cable)

    # calling function which returns the total price
    total_cost = calculate_total(length_of_fiber_cable, price_per_feet)

    # printing the receipt to the customer
    print_receipt(company_name, length_of_fiber_cable, total_cost)


if __name__ == '__main__':
    main()
