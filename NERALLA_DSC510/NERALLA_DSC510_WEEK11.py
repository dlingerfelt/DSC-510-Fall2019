'''
File: NERALLA_DSC510_WEEK10.py
Name: Ravindra Neralla
Course:DSC510-T303
Date:02/23/2020
Description: This program is to create a simple cash register program.
The program will have one class called CashRegister.
The program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
The program should have two getter methods.
getTotal – returns totalPrice
getCount – returns the itemCount of the cart
The program must create an instance of the CashRegister class.
The program should have a loop which allows the user to continue to add items to the cart until they request to quit.
The program should print the total number of items in the cart.
The program should print the total $ amount of the cart.
The output should be formatted as currency.
'''

import locale

# Creating class of CashRegister to calculate the total cost
class CashRegister:
    def __init__(self):
        self.__totalItems = 0
        self.__totalPrice = 0.0

    # Creating a method to return total price of the shopping cart
    def getTotal(self) -> float:
        return self.__totalPrice

    # creating a method to return total number of items in the shopping cart
    def getCount(self) -> int:
        return self.__totalItems

    # Create a method to add items to the shopping cart
    def addItem(self, price: float):

        self.__totalPrice += price    # Adding each item price in the shopping cart
        self.__totalItems += 1         # Adding item count in shopping  cart

def main():
    print('Welcome to the cash register. To know your total purchase price please enter q ')
    # creating an object using CashRegister() class
    register = CashRegister()
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

    while True:
        try:
            operation: str = input('Enter the price of your item : ')
            # At the end of shopping, enter q to calcualte total price and total items in cart
            if operation == 'q':
                break

            price = float(operation)

            register.addItem(price)
        except ValueError:
            print('The price is not valid. Please try again')

    total_price: float = register.getTotal()
    total_count: int = register.getCount()
    print('Total number of items added to your shopping cart : {}'.format(total_count))
    print('Total price of items is : {}'.format(locale.currency(total_price, grouping=True)))

if __name__ == '__main__':
    main()