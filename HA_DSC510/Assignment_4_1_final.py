#!/usr/bin/env python3

# File: Assignment_4_1.py
# Name: Jubyung Ha
# Date: 12/16/2019
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc: The program will do followings:
# Modify your IF Statement program to add a function. This function will perform the cost calculation.
# The function will have two parameters (feet and price).
# When you call the function, you will pass two arguments to the function;
# feet of fiber to be installed and the cost (remember that price is dependent on the number of feet being installed).
# You probably should have the following:
# Display a welcome message for your program.
# A function with two parameters
# A call to the function
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
        self.__cost_per_feet = 0.87
        self.__installation_cost = None
        print("{} inventory has been created.".format(self.__type_of_cable))

    def set_inventory(self):
        """Get inputs from users and set cost and total cost"""
        while True:
            try:
                print("Please set your inventory.")
                self.__feet = int(input("Enter the number of feet: "))  # Set feet
                break
            except ValueError:
                print("Please enter the number")

        self.__cost_per_feet = self.calculate_discounted_price(self.__feet, self.__cost_per_feet)  # Set cost

        self.__installation_cost = self.calculate_install_cost()  # Set total cost

        print("After bulk purchase discount is applied, the cost per feet is ${:,.2f}".format(self.__cost_per_feet))

    def calculate_discounted_price(self, feet, price=0.87):
        """Calculate price based on volume of purchase"""
        if self.__feet > 500:
            return 0.50
        elif self.__feet > 250:
            return 0.70
        elif self.__feet > 100:
            return 0.80
        else:
            return 0.87

    def calculate_install_cost(self):
        """Calculate the total cost and return"""
        return self.__feet * self.__cost_per_feet

    def get_inventory(self):
        """It prints a summary of inventory"""
        print("Type of cable: ", self.__type_of_cable)
        print("Fiber to be installed: ", self.__feet, " feet")
        print("Cost per feet: ${:,.2f}".format(self.__cost_per_feet))
        print("Installation cost: ${:,.2f}".format(self.__feet * self.__cost_per_feet))


class InventoryManager:

    def __init__(self):  # Initialize sub and super class
        print("Welcome to Inventory Manager.")
        print("Please enter your name and company.")
        self.__name = input("Your Name: ")
        self.__company = input("Company Name: ")
        self.inventory = None  # This object will have an instance of inventory class

    def create_inventory(self):
        """This will create an instance of Cable Inventory and assign to inventory var"""
        type_of_cable = input("Please enter the type of cable: ")
        self.inventory = CableInventory(type_of_cable)

    def set_inventory(self):
        """Calls set_inventory method of CableInventory class object"""
        self.inventory.set_inventory()

    def summarize_inventory(self):  # Override the super class method adding name and company
        """class get_inventory method of CableInventory in addition to name and company print"""
        print("###################")
        print("######SUMMARY######")
        print("###################")
        print("Name: ", self.__name)
        print("Company: ", self.__company)
        print(self.inventory.get_inventory())  # Call super class summarize_inventory method


def main():
    manager = InventoryManager()  # Create an instance of InventoryManager
    manager.create_inventory()  # Create inventory
    manager.set_inventory()  # Set inventory
    manager.summarize_inventory()  # Print inventory


if __name__ == '__main__':
    main()