#%%

#File: Assignment 4
#Name: April Meyer
#Assignment 4
#Date: 9.20.2019
'''Desc: This program will greet the user, ask for the
amount of fiber optic cable they would like to order.
It will then calculate the total based on the amount ordered using a New function'''

def bulk_order(fiber, cost): #new function with 2 parameters to calculate a bulk order
    fiber = int(fiber)
    if fiber <= 100:
        cost = cost
    elif fiber > 500:
        cost = fiber*.50
    elif fiber > 250:
        cost = fiber*.70
    elif fiber > 100:
        cost = fiber*.80
    print('Your receipt is below: \n\n',
          'Amount of fiber optic cable:', fiber, 'feet \n',
          'Order Total: $', cost)

company_name = input('Let\'s get started. What company do you work for?') #gets company name

try:  #calculates the total based on the amount
    ft_fib_cab = input('Thank you for choosing us! \n '
                       'How many feet of fiber optic cable would you like to order?') #gets amount needed
    tot_price = int(ft_fib_cab)*.87
    bulk_order(ft_fib_cab, tot_price)
except ValueError: #handles an incorrect value and reprompts the user
    try:
        ft_fib_cab = input('Invalid Entry. Please try again. How many feet would you like to order?')
        tot_price = int(ft_fib_cab)*.87
        bulk_order(ft_fib_cab, tot_price)
    except: #lets the user know they entered the wrong value
        print('Invalid Entry Again. Unable to process order.')