# File :    CASH_REGISTER.py
# Name :    Pradeep Jaladi
# Date :    02/18/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#     Your program must have a header.
#     Your program must have a welcome message for the user.
#     Your program must have one class called CashRegister.
#         Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
#         Your program should have two getter methods.
#             getTotal – returns totalPrice
#             getCount – returns the itemCount of the cart
#     Your program must create an instance of the CashRegister class.
#     Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
#     Your program should print the total number of items in the cart.
#     Your program should print the total $ amount of the cart.
#     The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.
# Desc : Program to calculate total cost in the cart.
import locale


# Class of Cash Register to calculate total cost
class CashRegister:

    def __init__(self):
        self.__itemCount = 0
        self.__totalPrice = 0.0

    # Method to return total price of the cart
    def getTotal(self) -> float:
        return self.__totalPrice

    # Method to return count of items in the cart
    def getCount(self) -> int:
        return self.__itemCount

    # Method to add item to the cart
    def addItem(self, price: float):
        """
        Parameters
        ----------
        price : float
        """
        self.__totalPrice += price  # Adding the price to total price
        self.__itemCount += 1  # Increasing the item count in cart


def main():
    print("----------------------------------------------------------------------------------------")
    print("Welcome to the cash register. To see final calculation enter q ")
    print("----------------------------------------------------------------------------------------")
    register = CashRegister()  # Initialization of the Cash Register Object
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

    while True:
        try:
            operation: str = input("Enter the price of the item : ")
            if operation == 'q':  # we cannot use any number to quit so using q
                break

            price = float(operation)

            register.addItem(
                price)  # the specifications did not mention anything about the negative price so leaving like that

        except ValueError:
            print("Oops! That was not a valid price. Try again...")

    total_price: float = register.getTotal()
    total_count: int = register.getCount()
    print("Total Items added to the cart are : {}".format(total_count))
    print("Total Price of the items added to cart : {}".format(locale.currency(total_price, grouping=True)))


if __name__ == '__main__':
    main()
