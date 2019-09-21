# File: week4.py
# Name: Awah Ndingwan
# Date: 09/17/2019
# Desc: Program calculates total cost by multiplying length of feet by cost per feet
# Usage: This program receives input from the user and calculates total cost by multiplying the number of feet
# by the cost per feet. Finally the program returns a summary of the transaction to the user

cost_per_feet_above_100feet = 0.80
cost_per_feet_above_250feet = 0.70
cost_per_feet_above_500feet = 0.50
length_above_100 = 100.0
length_above_250 = 250.0
length_above_500 = 500.0


# calculate and return cost
def calculate_cost(cost, feet):
    return cost * feet


class FiberCostCalculator:

    def __init__(self, company_name="", num_of_feet=0, installation_cost=0, cost_per_feet=0.87):
        self.company_name = company_name
        self.number_of_feet = num_of_feet
        self.installation_cost = installation_cost
        self.cost_per_feet = cost_per_feet

        self.get_input()
        self.compute_total_cost()
        self.show_receipt()

    # Get amd validate input from user
    def get_input(self):
        # printing welcome message
        message = "******** WELCOME ********"
        print(message)

        self.company_name = input("Enter Company name: ")

        while True:
            try:
                self.number_of_feet = float(input("Enter number of feet for fiber optic cable(ft): "))
            except ValueError:
                print("Not Valid! length of feet cannot be a String. Please try again.")
                continue
            else:
                break

    # compute installation cost for user
    def compute_total_cost(self):
        if length_above_100 < self.number_of_feet < length_above_250:
            self.cost_per_feet = cost_per_feet_above_100feet
            self.installation_cost = calculate_cost(self.number_of_feet, self.cost_per_feet)

        elif length_above_250 < self.number_of_feet < length_above_500:
            self.cost_per_feet = cost_per_feet_above_250feet
            self.installation_cost = calculate_cost(self.number_of_feet, self.cost_per_feet)

        elif self.number_of_feet > length_above_500:
            self.cost_per_feet = cost_per_feet_above_500feet
            self.installation_cost = calculate_cost(self.number_of_feet, self.cost_per_feet)

        else:
            self.installation_cost = calculate_cost(self.number_of_feet, self.cost_per_feet)

    # Print receipt details
    def show_receipt(self):
        print('********************')
        print('     Receipt      ')
        print(' ****************** ')
        print(f'Company Name: {self.company_name}')
        print(f'Cost Per Feet: ${float(self.cost_per_feet)}')
        print(f'Length of feet to be installed: {self.number_of_feet} feet')
        print("Total cost: $" + format(round(float(self.installation_cost), 2), ',.2f'))


if __name__ == "__main__":
    fiberCostCalculator = FiberCostCalculator()
