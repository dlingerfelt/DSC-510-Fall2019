#File: Assignment 11
#Name: April Meyer
#Assignment 11
#Date: 11.7.2019
"""This program will greet the user and ask them if they want to start a cart.
It will then allow the user to continue to add items to the cart until they request to quit (by typing done or clicking cancel).
The output print the total number of items in the cart and print the total $ amount of the cart.
"""
import easygui
import locale
locale.setlocale(locale.LC_ALL, '') #sets the locale for all categories to default
class CashRegister:

    def __init__(self, name): #constructer for cashRegister
        self.name = name
        CashRegister.itemCount = 0
        CashRegister.totalPrice = 0.0

    def addItem(self, price): #method to add items and calcuate the cart info
        CashRegister.totalPrice += price #total = total + price
        CashRegister.itemCount += 1

    def getTotal(self): #getter method
        return self.totalPrice

    def getCount(self): #getter method
        return self.itemCount

user_greeting = easygui.ynbox(msg="Would you like to create a cart?", title="Welcome") #welcome message
if user_greeting == False:
    easygui.msgbox(msg="Have a good Day" , title="End", ok_button="OK") #message if user says no
else:
    register1 = CashRegister('Register 1')
    while True: #continues to loop until user inputs done
        user_input = easygui.enterbox(msg='What is the price of the item? \n\n Press cancel when done.', title='Cash Register Cart', default='', strip=True) #prompts user input
        # print(user_input)
        if user_input == None: #Checks if user clicks cancel
            break
        if user_input.lower() == 'done': #Checks if user enters done to end
            break
        try:
            register1.addItem(float(user_input)) #verifies float number and adds to cashregister
        except ValueError:
            user_input = easygui.enterbox(msg='Invalid input. Please enter a numeric number.', title='Cash Register Cart', default='', strip=True) #prompts user input
            # print(user_input)
            if user_input == None: #Checks if user clicks cancel
                break
            if user_input.lower() == 'done': #Checks if user enters done to end
                break
            register1.addItem(float(user_input)) #verifies float number and adds to list
    easygui.msgbox(msg="All done! \n Total Number of Items: {} \n Total Amount: {}".format(register1.getCount(),locale.currency(register1.getTotal())), title="Cart Totals", ok_button="OK") #message once user inputs exits the loop

