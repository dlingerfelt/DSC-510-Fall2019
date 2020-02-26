# File: Assignment 11.1 - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 2/20/20
# Course: DSC510 - Introduction to Programing
# Desc: Program will accept items and price and display total items and total cost
# Usage: Simple Cash Register

import locale

# set locale to user's default setting
locale.setlocale(locale.LC_ALL, '')

def main():

    # class to calculate and total item count and total price
    class CashRegister:

        def __init__(self):
            self.itemCount = 0
            self.totalPrice = 0

        # add items Method
        def addItem(self, price):
            self.totalPrice += price
            self.itemCount += 1

        # getter Method
        def getTotal(self):
            return self.totalPrice
        def getCount(self):
            return self.itemCount

    print('Welcome to the Simple Cash Register Program')

    # CashRegister class instance
    simpleRegister = CashRegister()

    loop = True

    # loop to allow user to input many items
    while loop:

        checkErrors = True

        # 1st user input check
        while checkErrors:

            price = (input('\nPlease input item price:\n'))
            price = price.strip('$').replace(',', '')

            # try statement to check for  valid numeric input after stripping commas and decimals
            try:
                price = float(price)
                checkErrors = False
            except:
                print('\nPlease in valid price!\n')
                checkErrors = True

        # send price to CashRegister class
        simpleRegister.addItem(price)

        checkErrors = True

        # 2nd user input check
        while checkErrors:

            answer = input('\nWould you like to input another item? Please enter yes or no.\n')
            answer.lower()

            if 'yes' == answer:
                checkErrors = False
                loop = True

            elif 'no' == answer:
                checkErrors = False
                loop = False

            else:
                checkErrors = True
                print('\n*Incorrect Input! Please input "yes" or "no" only.*\n')

    print('\nTotal Items: {} '.format(simpleRegister.getCount()))
    print('Total Price: {} '.format(locale.currency(simpleRegister.getTotal())))
    print("\nHave a good day.\n")

main()
