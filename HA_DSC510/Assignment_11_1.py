#!/usr/bin/env python3

# File: Assignment_8_1.py
# Name: Jubyung Ha
# Date: 01/20/2020
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc: This week we’re going to demonstrate our knowledge of Python object oriented programming concepts
# by creating a simple cash register program.
#
# Your program must have a header.
# Your program must have a welcome message for the user.
# Your program must have one class called CashRegister.
# Your program will have an instance method called addItem which takes one parameter for price.
# The method should also keep track of the number of items in your cart.
# Your program should have two getter methods.
# getTotal – returns totalPrice
# getCount – returns the itemCount of the cart
# Your program must create an instance of the CashRegister class.
# Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
# Your program should print the total number of items in the cart.
# Your program should print the total $ amount of the cart.
# The output should be formatted as currency. Be sure to investigate the locale class.
# You will need to call locale.setlocale and locale.currency.

# Usage:


import locale

def welcome_message(self):
    """

    :return:
    """
    pass


class CashRegister(object):
    """

    """

    def __init__(self):
        """

        """
        self.itemCount = 0
        self.totalPrice = 0

    def addItem(self, price):
        """

        :param price:
        :return:
        """
        self.itemCount += 1
        self.totalPrice += price

    def getTotal(self):
        return self.totalPrice

    def getCount(self):
        return self.itemCount


def main():
    pass


if __name__ == '__main__':
    main()