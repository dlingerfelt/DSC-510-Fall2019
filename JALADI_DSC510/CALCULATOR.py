# File :    calculator.py
# Name :    Pradeep Jaladi
# Date :    12/02/2019
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#           Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Use the SIUE Style Guide as a reference.
#           Display a welcome message for your user.
#           Retrieve the company name from the user.
#           Retrieve the number of feet of fiber optic cable to be installed from the user.
#           Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
#           Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
#           Include appropriate comments throughout the program.
# Desc :    Program to calculate total cost of fiber cable installation
# Usage :
#           The program prompts the user for company name, required feet of fiber optical cable to be installed
#           The program will calculate the cost of prints the receipt for the user
import datetime

price: float = 0.87


# This function will calculate the total cost
def calculate_total(length_of_fiber_cable: int):
    return length_of_fiber_cable * price  # total cost = length of fiber * 0.85


# This function will print the customer receipt
def print_receipt(company_name: str, length_of_fiber_cable: int, sale_price: float):
    now = datetime.datetime.now()
    print('Receipt Date : ' + now.strftime("%Y-%m-%d %H:%M:%S"))  # printing date & time
    print('Invoice for : {0}'.format(company_name))  # printing company name
    print('Purchased length of feet : {:,}'.format(length_of_fiber_cable))  # printing the fiber length
    print('Total cost is : ', sale_price)  # sale price
    print('Total formatted cost is : ', '{:,.2f}'.format(sale_price))  # sale formatted price


def main():
    print("Welcome to the store")
    company_name: str = input("Enter your company name \n")
    while True:
        try:
            length_of_fiber_cable: int = int(input("Enter the length of fiber cable \n"))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    # calling function which returns the total price
    sale_price = calculate_total(length_of_fiber_cable)

    # printing the receipt to the customer
    print_receipt(company_name, length_of_fiber_cable, sale_price)


if __name__ == '__main__':
    main()
