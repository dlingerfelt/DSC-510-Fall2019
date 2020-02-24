# File : assignment11.1-Cash_Register.py
# Name : Bhargava Gaggainpali
# Date : FEB-23-2020
# Course : Introduction to Programming - python
# Assignment :
#- This week we’re going to demonstrate our knowledge of Python object oriented programming concepts by creating a simple cash register program.
#- Your program must have a header.
#- Your program must have a welcome message for the user.
#- Your program must have one class called CashRegister.
#- Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
#- Your program should have two getter methods.
#- getTotal – returns totalPrice
#- getCount – returns the itemCount of the cart
#- Your program must create an instance of the CashRegister class.
#- Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
#- Your program should print the total number of items in the cart.
#- Your program should print the total $ amount of the cart.
#- The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.
# Desc : Program is to take input on the list of items and display total values.
# Usage :
# -User is prompted to enter price of each item and program display total count and total prize.

import locale
# setting locale to default setting
locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

# class CashRegister to calculate the total count and total cost
class CashRegister:
    def __init__(self):
        self.__CountofItems = 0
        self.__SumofPrice = 0.0

    # getCount method to return total number of items in the shopping cart
    def getCount(self):
        return self.__CountofItems

    # getTotal method to return total price of the shopping cart
    def getTotal(self):
        return self.__SumofPrice

    # addItem a method to add items to the shopping cart
    def addItem(self, price: float):

        self.__SumofPrice += price    # SUM each item price in the shopping cart
        self.__CountofItems += 1         # Increment the count in shopping  cart

def main():
    print('\n----------------------------------------')
    print('Welcome to the Cash_Register Program..!!')
    print('----------------------------------------\n')

    # creating an Class_instance using CashRegister() class
    Class_Instance1 = CashRegister()

    while True:
        try:
            user_input: str = input('Please Enter the price of the item or Enter "q" to complete the Shopping list : ')
            # Read user input and add to register. q to complete the program
            if user_input == 'q':
                break

            price = float(user_input) # assign the user input value to a variable

            Class_Instance1.addItem(price) # Calling the method addItem
        except ValueError:
            print('The price is not valid. Please try again')

    total_price: float = Class_Instance1.getTotal() # calling the method getTotal
    total_count: int = Class_Instance1.getCount() # calling the method getCount

    print('\nTotal number of items added to the shopping cart : {}'.format(total_count))
    print('Total price of all the items in the shopping cart is : {}'.format(locale.currency(total_price, grouping=True)))
    print('\nThank you for using the Cash_Register program.')
    print('------------------------------------------------------------')
if __name__ == '__main__':
    main()