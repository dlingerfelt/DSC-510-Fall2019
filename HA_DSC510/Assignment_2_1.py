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
# Usage: InventoryManager class has name, company, type_of_cable, feet,  and cost_per_feet as its member.
# The user will need to throw arguments for those 5 attributes while cost_per_feet is defaulted to be 0.87.
# InventoryManager class has CableInventory class as a parent class where the cable inventory is managed
# CableInventory class has one method called summarize_inventory which shows the current status of the inventory
# and calculate the total installation cost as well.
# InventoryManager overrides the summarize_inventory method by adding a user name and company.


class CableInventory:

    def __init__(self, type_of_cable, feet, cost_per_feet=0.87):  # Initialize variables
        self.__type_of_cable = type_of_cable
        self.__feet = feet
        self.__cost_per_feet = cost_per_feet

    def summarize_inventory(self):  # Print a summary of inventory and calculate the total installation cost
        print("Fiber to be installed: ", self.__feet, " feet")
        print("Cost per feet: $", self.__cost_per_feet)
        print("Installation cost: $", self.__feet * self.__cost_per_feet)


class InventoryManager(CableInventory):

    def __init__(self, name, company, type_of_cable, feet, cost_per_feet):  # Initialize sub and super class
        super().__init__(type_of_cable, feet, cost_per_feet)
        self.__name = name
        self.__company = company

    def summarize_inventory(self):  # Override the super class method adding name and company
        print("Name: ", self.__name)
        print("Company: ", self.__company)
        print(super().summarize_inventory())  # Call super class summarize_inventory method


if __name__ == '__main__':
    manager = InventoryManager("Jubyung Ha", "Verizon", "Fiber Optic", 3566, 0.87)
    manager.summarize_inventory()
