'''
    File: Assignment4-1.py
    Author: Sanjay Jaras
    Assignment: 4.1
    Date:09/15/2019
    Course: DSC 510 - Introduction to programming
    Desc: Program will calculate the installation cost for fiber optic cable, it will use function to calculate the price
    Usage: This program will show welcome message to user and ask for company name,
    and take the number of feet fiber optics cable he wants to install.
    Calculate the installation cost as follow
    default rate is $0.87/feet
    >100 feet rate is $0.80/feet
    >250 feet rate is $0.70/feet
    >500 feet rate is $0.50/feet

    Create a function with 2 parameters cable length in feet and price per foot
'''


# declare the function for calculating the installation cost
def calculate_installation_cost(cable_length: int, price_per_feet: float):
    """
    This function will calculate the installation cost

    :param cable_length: Length of the fiber cable in feet to be installed
    :param price_per_feet: Installation cost per feet
    :return: Returns the installation cost by multiplying length by price per feet
    """
    return cable_length * price_per_feet


# declare function to prepare the quotation for customer
def calculate_quotation(company: str, default_rate: float, applied_rate: float, cable_length: int):
    """
    This function will create the quotation for customer

    :param company: Name of the company
    :param default_rate: default rate
    :param applied_rate: rate to apply after discount
    :param cable_length: length of the cable to install
    :return: None
    """

    # Calculate installation cost by calling calculate_installation_cost function
    installation_cost = calculate_installation_cost(cable_length, default_rate)
    # calculate discounted price by calling calculate_installation_cost function
    discounted_price = calculate_installation_cost(cable_length, applied_rate)

    line_length = 100
    # Print Quotation
    # Print header with company name
    print("\n", "*" * line_length, end="\n")
    print(" " * ((line_length // 2) - len(company)), company, end="\n")
    print("*" * line_length, end="\n")

    # print cable length
    print("Cable length:\t", cable_length, "feet", end="\t" * 10)

    # Print installation cost without discount
    print("Installation cost per feet:\t", default_rate_feet, "$", end="\n")
    print("Calculated cost:", installation_cost, "$", end="\t" * 11)
    print("Total cost:", "\t" * 3, installation_cost, "$", end="\n")

    # print installation cost after discount
    print("Discount :\t", "%2.2f" % (installation_cost - discounted_price), "$", end="\t" * 10)
    print("Discounted cost per feet:\t\t", rate_per_feet, "$", end="\n")
    print("Discounted  cost:", discounted_price, "$", end="\t" * 11)

    # Print final quotation amount
    print("Discounted Total:", "\t" * 2, discounted_price, "$", end="\n")
    print("*" * line_length)


if __name__ == "__main__":

    # print welcome message
    print("Welcome !!!")
    # get company name from user
    company_name = input("Please enter company name:")
    # get length of the fiber cable in feet to be installed

    # Validate if user entered valid length of the cable
    feet = None
    while feet is None:
        try:
            feet = int(input("Please enter the cable length in feet:"))
        except ValueError:
            # if invalid length is entered get length again from user
            print("Please enter valid cable length...", end="\n")
            feet = None

    # Default rate used for calculating discount
    default_rate_feet = 0.87

    # Determine the rate to be applied by considering the cable length
    #   default rate is $0.87/feet
    #   >100 feet rate is $0.80/feet
    #   >250 feet rate is $0.70/feet
    #   >500 feet rate is $0.50/feet
    if feet > 500:
        rate_per_feet = 0.50
    elif feet > 250:
        rate_per_feet = 0.70
    if feet > 100:
        rate_per_feet = 0.80
    else:
        rate_per_feet = 0.87

    # invoke the function to calculate quotation for a customer
    calculate_quotation(company_name, default_rate_feet, rate_per_feet, feet)
