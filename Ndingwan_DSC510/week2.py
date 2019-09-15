# File: week2.py
# Name: Awah Ndingwan
# Date: 09/03/2019
# Desc: Program calculates total cost by multiplying length of feet by cost per feet
# Usage: This program receives input from the user and calculates toal cost by multiplying the number of feet
# by the cost per feet. Finally the program returns a summary of the transaction to the user

cost_per_feet = 0.87


class FiberCostCalculator:

    def __init__(self):
        # printing welcome message
        message = "******** WELCOME ********"
        print(message)

        # Get amd validate input from user
        self.company_name = input("Enter Company name: ")

        # Get amd validate input from user
        while True:
            try:
                self.number_of_feet = float(input("Enter number of feet for fiber optic cable(ft): "))
            except ValueError:
                print("Not Valid! length of feet cannot be a String. Please try again.")
                continue
            else:
                break

        # Calculate installation cost
        self.installation_cost = self.number_of_feet * cost_per_feet

        self.show_receipt()

    # Print receipt details
    def show_receipt(self):
        print('******************')
        print('     Receipt      ')
        print('******************')
        print(f'Company Name: {self.company_name}')
        print(f'Cost Per Feet: ${float(cost_per_feet)}')
        print(f'Length of feet to be installed: {self.number_of_feet} feet')
        print("Total cost: $" + format(round(float(self.installation_cost), 2), ',.2f'))


if __name__ == "__main__":
    cost = FiberCostCalculator()
