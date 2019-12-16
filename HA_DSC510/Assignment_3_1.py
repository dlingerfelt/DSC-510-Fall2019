#!/usr/bin/env python3

# File: Assignment_3_1.py
# Name: Jubyung Ha
# Date: 12/14/2019
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc: The program will do followings:
# Display a welcome message for your program.
# Get the company name from the user.
# Get the number of feet of fiber optic cable to be installed from the user.
# Calculate the cost of fiber optic cable installation by multiplying the number of feet needed by $0.87.
# Evaluate a bulk discount.
# Using the default value of $0.87 calculate the total expense.
# If the user purchases more than 100 feet they are charged $0.80 per foot.
# If the user purchases more than 250 feet they will be charged $0.70 per foot.
# If they purchase more than 500 feet, they will be charged $0.50 per foot.
# Prompt the user for the number of fiber optic cable they need installed.
# Evaluate the total cost based upon the number of feet requested.
# Display the calculated information including the number of feet requested and company name.

# Usage: InventoryManager class has name, company, and an object of CableInventory class as its member.
# The inventory manager can create, set, and summarize the cable inventory
# CableInventory has members of cables (feet, type, cost per feet, total cost).
# CableInventory class has three methods: set, get, and calculate total cost.
# The user will need to create an instance of InventoryManager class and the program will guide users to process.


class CableInventory:

    def __init__(self, type_of_cable):  # Initialize variables
        self.__type_of_cable = type_of_cable
        self.__feet = None
        self.__cost_per_feet = None
        self.__installation_cost = None
        print("{} inventory has been created.".format(self.__type_of_cable))

    def set_inventory(self):
        while True:
            try:
                print("Please set your inventory.")
                self.__feet = int(input("Enter the number of feet: "))
                break
            except ValueError:
                print("Please enter the number")

        if self.__feet > 500:
            self.__cost_per_feet = 0.50
        elif self.__feet > 250:
            self.__cost_per_feet = 0.70
        elif self.__feet > 100:
            self.__cost_per_feet = 0.80
        else:
            self.__cost_per_feet = 0.87

        self.__installation_cost = self.calculate_install_cost()

        print("After bulk purchase discount is applied, the cost per feet is {}".format(self.__cost_per_feet))

    def calculate_install_cost(self):
        return self.__feet * self.__cost_per_feet

    def get_inventory(self):
        print("Type of cable: ", self.__type_of_cable)
        print("Fiber to be installed: ", self.__feet, " feet")
        print("Cost per feet: $", self.__cost_per_feet)
        print("Installation cost: $", self.__feet * self.__cost_per_feet)


class InventoryManager:

    def __init__(self):  # Initialize sub and super class
        print("Welcome to Inventory Manager.")
        print("Please enter your name and company.")
        self.__name = input("Your Name: ")
        self.__company = input("Company Name: ")
        self.inventory = None

    def create_inventory(self):
        type_of_cable = input("Please enter the type of cable: ")
        self.inventory = CableInventory(type_of_cable)

    def set_inventory(self):
        self.inventory.set_inventory()

    def summarize_inventory(self):  # Override the super class method adding name and company
        print("###################")
        print("######SUMMARY######")
        print("###################")
        print("Name: ", self.__name)
        print("Company: ", self.__company)
        print(self.inventory.get_inventory())  # Call super class summarize_inventory method


def main():
    manager = InventoryManager()
    manager.create_inventory()
    manager.set_inventory()
    manager.summarize_inventory()


if __name__ == '__main__':
    main()