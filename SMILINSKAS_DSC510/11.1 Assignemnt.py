# File: 11.1 Assignment.py
# Name: Vilius Smilinskas
# Date: 2/23/2020
# Course: DSC510: Introduction to Programming
# Desc: Program will ask for an input of product prices and number of items recorded.
# Usage: Run the program, input numbers for a total, 'total' to see the total cost,
# 'count' to see the number of items on the list,'quit' to exit the program
import locale  # to utilize the module for currency


class CashRegister:  # creating class and establishing variable
    total = 0
    count = 0
    print_total = 0

    def additem(self, amount):  # defining function
        self.total = self.total + amount  # add amount for total
        self.count = self.count + 1  # counter

    def getTotal(self):
        self.print_total = locale.currency(self.total, '$')  # formats the new format for printing.
        print('the total is : ' + str(self.print_total))

    def getCount(self):
        print('the number of items is : ' + str(self.count))


walmart = CashRegister()  # establishing variable


def main():  # main program segment
    price = input('Price of the item:')
    if price == "total":  # test for specific input
        walmart.getTotal()
        main()
    if price == "count":  # test for specific input
        walmart.getCount()
        main()
    if price == "quit":   # test for specific input
        walmart.getTotal()
        walmart.getCount()
        exit()
    try:
        price = float(price)
    except ValueError:
        print('Enter a number:')
        main()
    walmart.additem(price)
    main()


locale.setlocale(locale.LC_ALL, '')
print('Welcome to the Cash Register Program')
main()
