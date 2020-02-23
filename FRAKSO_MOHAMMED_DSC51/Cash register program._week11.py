'''
File: CashRegister.py
Name: Mohammed A. Frakso
Date: 02/16/2020
Course: DSC_510 - Introduction to Programming
Desc: creating a simple cash register program.
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

# Creating class of Cash Register to calculate the total cost
class CashReg:
    def __init__(self):
        self.__itemCount = 0
        self.__totalPrice = 0.0

    def getTotal(self) -> float:      # Creating a method to return total price of the shopping cart
        return self.__totalPrice

    def getCount(self) -> int:        # creating a method to return total price of the shopping cart
        return self.__itemCount

    def addItem(self, price: float):  # Creating a method to add item to the shopping cart while price is a float

        self.__totalPrice += price    # Adding each item price in the shopping cart
        self.__itemCount += 1         # Adding item count in shopping  cart

def main():
    print('Welcome to the cash register. To get your total price please enter t ')

    register = CashReg()               # Starting the Cash Register Object
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

    while True:
        try:
            operation: str = input('Enter the price of your item : ')
            if operation == 't':       # To stop the loop and get total price i use t for total
                break

            price = float(operation)

            register.addItem(price)  # no negative price accepted
        except ValueError:
            print('The price is not valid. Please try again')

    total_price: float = register.getTotal()
    total_count: int = register.getCount()
    print('Total items added to your shopping cart : {}'.format(total_count))
    print('Your total price is : {}'.format(locale.currency(total_price, grouping=True)))

if __name__ == '__main__':
    main()