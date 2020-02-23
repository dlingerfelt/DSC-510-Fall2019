'''
 File: DSC510-Week 11 Nguyen.py
 Name: Chau Nguyen
 Date: 2/22/2020
 Course: DSC_510 Intro to Programming
 Description: Learning and implementing class, and it's property -- class methods and instances
 '''
import locale #Currency data
class CashRegister:
    def __init__(self):
        #initiate variable
        self.totalprice = 0
        self.total_Item = 0
        #CashRegister.number_item +=1
    def addItem(self,price):
        self.total_Item +=1
        self.totalprice = self.totalprice + price
    def getTotal(self):
        return 'Total price of items is : {}'.format(locale.currency(self.totalprice, grouping=True))
    def getCount(self):
        return 'Total number of items added to your shopping cart : {}'.format(self.total_Item)
def main():
    print("Welcome,this is a cash register program that help you calculate your total prices.")
    price_listing = CashRegister()
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
    while True:
        try:
            user_input = input("Please enter the item's price, when complete enter 'done' to calculate the total price ")
            if user_input == 'done':
                break
            price = float(user_input)
            price_listing.addItem(price)
        except ValueError:
                print('Response not valid. Please enter correct value')
    print(price_listing.getTotal())
    print(price_listing.getCount())

if __name__ == '__main__':
    main()


