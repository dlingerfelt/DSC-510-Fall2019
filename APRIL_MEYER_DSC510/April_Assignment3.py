#%%

#File: Assignment 3
#Name: April Meyer
#Assignment 3
#Date: 9.12.2019
'''Desc: This program will greet the user, ask for the
amount of fiber optic cable they would like to order.
It will then calculate the total based on the amount ordered. '''

ft_fib_cab = input('Thank you for choosing us! \n '
                   'How many feet of fiber optic cable would you like to order?') #gets amount needed
try:  #calculates the total based on the amount
    if int(ft_fib_cab) > 500:
        print('Your receipt is below: \n\n',
              'Amount of fiber optic cable:', ft_fib_cab, 'feet \n',
              'Order Total: $', int(ft_fib_cab)*.50)
    elif int(ft_fib_cab) > 250:
        print('Your receipt is below: \n\n',
              'Amount of fiber optic cable:', ft_fib_cab, 'feet \n',
              'Order Total: $', int(ft_fib_cab)*.70)
    elif int(ft_fib_cab) > 100:
        print('Your receipt is below: \n\n',
              'Amount of fiber optic cable:', ft_fib_cab, 'feet \n',
              'Order Total: $', int(ft_fib_cab)*.80)
    else:
        print('Your receipt is below: \n\n',
              'Amount of fiber optic cable:', ft_fib_cab, 'feet \n',
              'Order Total: $', int(ft_fib_cab)*.87)
except ValueError: #handles an incorrect value and reprompts the user
    ft_fib_cab = input('Invalid Entry. Please try again. How many feet would you like to order?')
    if int(ft_fib_cab) > 500:
        print('Your receipt is below: \n\n',
              'Amount of fiber optic cable:', ft_fib_cab, 'feet \n',
              'Order Total: $', int(ft_fib_cab)*.50)
    elif int(ft_fib_cab) > 250:
        print('Your receipt is below: \n\n',
              'Amount of fiber optic cable:', ft_fib_cab, 'feet \n',
              'Order Total: $', int(ft_fib_cab)*.70)
    elif int(ft_fib_cab) > 100:
        print('Thank you for you business. Your receipt is below: \n\n',
              'Amount of fiber optic cable:', ft_fib_cab, 'feet \n',
              'Order Total: $', int(ft_fib_cab)*.80)
    else:
        print('Your receipt is below: \n\n',
              'Amount of fiber optic cable:', ft_fib_cab, 'feet \n',
              'Order Total: $', int(ft_fib_cab)*.87)
except: #lets the user know they entered the wrong value
    print('Invalid Entry. Unable to process order.')

