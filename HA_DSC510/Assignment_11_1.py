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

# Set LC_ALL default
locale.setlocale(locale.LC_ALL, '')


def isAnswer(answer):
    """ Test if an answer is in Y or N and return True or False
    """
    if answer.upper() in ('Y', 'N'):
        return True


class CashRegister(object):
    """Maintains number of items and total cash amounts
    Fields:
        itemCount: total number of item
        totalPrice: total amount of cash
    Methods:
        addItem: uses to add an item to cash register
        getTotal: gets total price in currency format
        getCount: gets total count
        prettify_register: prints total price and count
    """

    def __init__(self):
        """Initiate cash register object and send welcome message
        """
        self.itemCount = 0
        self.totalPrice = 0
        print('------------------------------------------------')
        print('------------Welcome to Cash Register------------')
        print('------------------------------------------------')
        print('Current number of item is {} and total price is ${:,.2f}'.format(self.itemCount, self.totalPrice))

    def addItem(self, price):
        """Adds an item to the register and increase count by 1 and by amount
        :param
            itemCount: count the number of item
            price: keep the total price
        :return:
        """
        self.itemCount += 1
        self.totalPrice += price

    def getTotal(self):
        """Returns total amount and format it as currency"""
        return locale.currency(self.totalPrice)

    def getCount(self):
        """Returns item count"""
        return self.itemCount

    def prettify_register(self):
        """ Prettify the cash register
        :param:
        :return:
            NONE
        """
        print('------------------------------------------------')
        print('::::::::::::::::::Cash Register:::::::::::::::::')
        print('Total number of item: {}'.format(self.getCount()))
        print('Total price: {}'.format(self.getTotal()))
        print('------------------------------------------------')


def main():
    cash_register = CashRegister()  # Instantiate cash register object
    # Receive inputs from the user until they want to quit
    while True:
        print('Do you want to add a new item?')
        answer = input('Y for yes, N for quit the program: ')
        # If the answer is not in Y or N, then send a warning and continue
        if not isAnswer(answer):
            print('Only enter Y or N for your answer!')
            continue
        # If the answer is N, then quit the program
        elif answer.upper() == 'N':
            break
        else:
            # Test a user input if it is numeric
            while True:
                item = input('Enter the amount into your cash register: ')
                if not item.isnumeric():
                    print('Only enter numbers!')
                    continue
                else:
                    item = int(item)
                    cash_register.addItem(item)
                    break
    print(cash_register.prettify_register())  # Print prettified results


if __name__ == '__main__':
    main()