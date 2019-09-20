# File: week2.py
# Name: Awah Ndingwan
# Date: 09/03/2019
# Desc: Program calculates total cost by multiplying length of feet by cost per feet
# Usage: This program receives input from the user and calculates toal cost by multiplying the number of feet
# by the cost per feet. Finally the program returns a summary of the transaction to the user

cost_per_feet_above_100feet = 0.80
cost_per_feet_above_250feet = 0.70
cost_per_feet_above_500feet = 0.50
length_above_100 = 100.0
length_above_250 = 250.0
length_above_500 = 500.0


class FiberCostCalculator:
    cost_per_feet = 0.87

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
        if length_above_100 < self.number_of_feet < length_above_250:
            self.installation_cost = self.number_of_feet * cost_per_feet_above_100feet
            self.cost_per_feet = cost_per_feet_above_100feet

        elif length_above_250 < self.number_of_feet < length_above_500:
            self.installation_cost = self.number_of_feet * cost_per_feet_above_250feet
            self.cost_per_feet = cost_per_feet_above_250feet

        elif self.number_of_feet > length_above_500:
            self.installation_cost = self.number_of_feet * cost_per_feet_above_500feet
            self.cost_per_feet = cost_per_feet_above_500feet

        else:
            self.installation_cost = self.number_of_feet * self.cost_per_feet

        self.show_receipt()

    # Print receipt details
    def show_receipt(self):
        print('******************')
        print('     Receipt      ')
        print('******************')
        print(f'Company Name: {self.company_name}')
        print(f'Cost Per Feet: ${float(self.cost_per_feet)}')
        print(f'Length of feet to be installed: {self.number_of_feet} feet')
        print("Total cost: $" + format(round(float(self.installation_cost), 2), ',.2f'))


if __name__ == "__main__":
    fiberCostCalculator = FiberCostCalculator()
