# File : Safari_DSC510_ObjectOrientedCashRegister.py
# Name: Edris Safari
# Date:11/05/2019
# Course: DSC510 - Introduction To Programming
# Desc:
# This program works as a cash register. The user is prompted to enter a dollar amount
# for an item. The program keeps a tally of the total amount as user enters each value.
# Once completed, the program displays the total of values as well as number of values
# entered.
# Usage:
# Execute this program from the command line by entering the program name Safari_DSC510_ObjectOrientedCashRegister

import locale

# sets the locale for all categories to default
locale.setlocale(locale.LC_ALL, '')

# Set valid yes and no replies
yes_replies = ['y', 'yes']
no_replies = ['n', 'no']


class CashRegister:
    # Class CashRegister
    # constructor for cashRegister
    def __init__(self):
        self.totalCount = 0
        self.totalPrice = 0.0

    # method to add items and calculate the cart info
    def additem(self, price):
        self.totalPrice += price  # total = total + price
        self.totalCount += 1

    def gettotal(self):
        return locale.currency(self.totalPrice)

    # method to get current count
    def getCount(self):
        return self.totalCount


def receipt_screen(register):
    # This function prints the receipt screen. It is called by the main
    # function when user creates a new receipt.

    number_of_items_msg = ' Total number of items entered: {} '.format(register.getCount())
    total_price_msg = ' Total Price: {} '.format(register.gettotal())
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the receipt message lines surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * ((max(len(number_of_items_msg), len(total_price_msg))) + 20)
    number_of_items_line = "-" * int((len(decoration_line) - len(number_of_items_msg)) / 2) + \
                           number_of_items_msg + "-" * \
                           int((len(decoration_line) - len(number_of_items_msg)) / 2)
    total_price_line = "-" * int((len(decoration_line) - len(total_price_msg)) / 2) + \
                       total_price_msg + "-" * int((len(decoration_line) - len(total_price_msg)) / 2)

    print(decoration_line)
    print(number_of_items_line)
    print(total_price_line)
    print(decoration_line)


def welcome_screen():
    # This function prints the welcome screen. It is called by the main
    # function upon start of this application.
    welcome_message1 = 'Welcome to Object Oriented Cash Register'
    welcome_message2 = 'Enter items with price and get totals.'
    welcome_message3 = 'Only numbers 0 or greater will be processed. All others will be ignored.'
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the welcome message line surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * ((max(len(welcome_message1), len(welcome_message2), len(welcome_message3))) + 20)
    total_length = len(decoration_line)
    welcome_line1 = "-" * int((total_length - len(welcome_message1)) / 2) + welcome_message1 + "-" * int(
        (total_length - len(welcome_message1)) / 2)
    welcome_line2 = "-" * int((total_length - len(welcome_message2)) / 2) + welcome_message2 + "-" * int(
        (total_length - len(welcome_message2)) / 2)
    welcome_line3 = "-" * int((total_length - len(welcome_message3)) / 2) + welcome_message3 + "-" * int(
       (total_length - len(welcome_message3)) / 2)
    print(decoration_line)
    print(welcome_line1)
    print(welcome_line2)
    print(welcome_line3)
    print(decoration_line)


def goodbye_screen():
    # This function prints the goodbye screen. It is called by the main
    # function upon normal exit from this application.
    goodbye_message = 'Thank you. Please come again.'
    # Calculations below construct a decoration line which is '-' repeated 20 times
    # and the goodbye message line surrounded by '-'. This is followed by another decoration line.
    decoration_line = "-" * (len(goodbye_message) + 20)
    goodbye_line = "-" * 10 + goodbye_message + "-" * 10
    print(decoration_line)
    print(goodbye_line)
    print(decoration_line)


def isfloat(value):
    # This function returns true if the value is float and positive
    try:
        if float(value) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def isint(value):
    # This function returns true if the value is an integer and positive
    try:
        if int(value) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def main():
    # Display Welcome screen
    welcome_screen()
    first_time = True

    # Loop allows the users to create as many receipt as the want
    while True:
        if first_time:
            print('Would you like to create a receipt?')
        else:
            print('Would you like to create another receipt?')

            # Create an instance of the CashRegister class
        user_reply = input('Please \'y\'  or \'yes\' to continue and \'n\'  or \'no\' to quit) >>> ')
        if user_reply.lower() in no_replies:  # Break out of the loop if user enters 'n' or 'no' and exit the program,
            break
        elif not user_reply.lower() in (yes_replies + no_replies):  # keep promoting until valid response is given.
            continue
        else:  # User wants to create a receipt.
            first_time = False
            register = CashRegister()
            # The loop allows the users to enter as many items as they want
            while True:
                # Prompt user reply/
                user_reply = input('Please enter the price of item_' + str(register.getCount() + 1) +
                                   ' or \'s\' to get the totals >>> ')

                # Break out of the loop if user enters 's'
                if user_reply.lower() == 's':
                    break
                elif isfloat(user_reply) or isint(user_reply):
                    register.additem(float(user_reply))
                else:
                    continue
            receipt_screen(register)
    goodbye_screen()


# Execute main function is this file is primary.
if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    main()
else:
    print("This Module's name is :" + __name__)
