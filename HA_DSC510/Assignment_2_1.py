# File: program2.py
# Name: Jubyung Ha
# Date: 11/30/2019
# Course: DSC510-T303 Introduction to Programming (2203-1)
# Desc: The program will do followings:
# Display a welcome message for your user.
# Retrieve the company name from the user.
# Retrieve the number of feet of fiber optic cable to be installed from the user.
# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost,
# and total cost in a legible format.
# Usage:


class CableInventory:

    def __init__(self, type_of_cable, feet, cost_per_feet=0.87):
        self.__type_of_cable = type_of_cable
        self.__feet = feet
        self.__cost_per_feet = cost_per_feet

    def summarize_inventory(self):
        print("Fiber to be installed: ", self.__feet, " feet")
        print("Cost per feet: $", self.__cost_per_feet)
        print("Installation cost: $", self.__feet * self.__cost_per_feet)


class InventoryManager(CableInventory):

    def __init__(self, name, company, type_of_cable, feet):
        super().__init__(self, type_of_cable, feet)
        self.__name = name
        self.__company = company

    def summarize_inventory(self):
        print("Name: ", self.__name)
        print("Company: ", self.__company)
        print(super().summarize_inventory())


if __name__ == '__main__':
    manager = InventoryManager("Jubyung Ha", "Verizon", "Fiber Optic", 3566)
    manager.summarize_inventory()
