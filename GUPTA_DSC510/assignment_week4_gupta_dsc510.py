# File: RGupta_wk4.py
# Instructor: David Lingerfelt
# Date: 09/18/2019
# Course: DSC510-T304 Introduction to Programming
# Assignment#: 4.1
# Description: This program perform the cost calculation of fiber optic cable with taxes
# User gets a discount on purchase of 100 feet or more 	cable
# Usage: This program requires total length of the optic fiber as the input

import datetime

# Changes the color of the text to green
print("\033[1;32;48m")
print('Welcome to DukeNet Optic Fiber - A destination to buy optic fiber ')
print("\033[1;30;48m")
# actual price per foot = 0.93 cents and tax= 7%
act_price = 0.93
tax = 0.07

# Defining a function
# act_cst = original cost of the cable
# cst_after_disc = cost after deducting the discount
# cst_plus_tax   = tax added to the cost after discount

def caltotcost(ft, prc):
    act_cst = ft * act_price
    cst_after_disc = ft * prc
    cal_tax = cst_after_disc * tax
    cst_plus_tax = round(cst_after_disc + cal_tax, 2)
    print("\033[1;33;48m")
    print("The Original Cost of the Cable :  " + '%.2f' % act_cst + "$")
    if ft > 100:
        print("Total Cost of Your Purchase with Discount:  " + '%.2f' % cst_after_disc + "$")
        print("Final Cost of Your Purchase with 7% tax: " + '%.2f' % cst_plus_tax + "$")
    inp_enter = input('Enter Y to print Receipt : \n')

# Print receipt with Company name, total cost and time
    if inp_enter in ('y', 'Y'):
        print("\033[1;32;48m")
        print("DukeNet Optic Fiber \n\t\t RECEIPT\n\t")
        print("\033[1;33;48m")
        print("\t  Buyer : " + inp_comp)                            ## 'inp_comp' takes input from the user
        print("Total Optic Fiber Purchased:", + no_of_feet, "ft")
        print("\t   Sub Total : " + "$" + '%.2f' % cst_after_disc)
        print("\tSales tax(7%): " + "$" + '%.2f' % cal_tax)
        print("\t  Total Cost : " + "$" + '%.2f' % cst_plus_tax)
        print("\033[1;32;48m")
        print("\nThank you for shopping at DukeNet..!!")
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M"), "\n")
    else:
        print("Thank you. Bye..!!")
    return cst_plus_tax

# Takes input from the user for company name and feet
inp_comp = input('Please Enter Your Company Name: \n')
while True:
    try:
        print("\033[1;30;48m")
        no_of_feet = float(input('Enter total length of optic fiber you want to purchase (In Feet) : \n'))
        break
    except ValueError:
        print("\033[1;31;48m")
        print(''"Please enter a valid number..!!"'')

# Calculate discount
if no_of_feet <= 100:
    disc_val = 0                                    # No discount for <= 100 feet
else:
    if (no_of_feet > 100) and (no_of_feet <= 250):
        disc_val = 0.07                             # 7 cents discount when total feet <= 250 and > 100
    else:
        if (no_of_feet > 250) and (no_of_feet <= 500):
            disc_val = 0.17                         # 17 cents discount when total feet <= 500 and > 250
        else:
            disc_val = 0.37                         # 37 cents discount when total feet > 500

# cost per foot = actual price minus discount value
aft_dis_prc = act_price - disc_val
# call function to calculate the costs
caltotcost(no_of_feet, aft_dis_prc)


Output:

Welcome to DukeNet Optic Fiber - A destination to buy optic fiber                                                               
                                                                                                                                
Please Enter Your Company Name:                                                                                                 
Duke                                                                                                                            
                                                                                                                                
Enter total length of optic fiber you want to purchase (In Feet) :                                                              
2~                                                                                                                       
                                                                                                                                
Please enter a valid number..!!                                                                                                 
                                                                                                                                
Enter total length of optic fiber you want to purchase (In Feet) :                                                              
10                                                                                                                              
                                                                                                                                
The Original Cost of the Cable :  9.30$                                                                                         
Enter Y to print Receipt :                                                                                                      
y                                                                                                                               
                                                                                                                                
DukeNet Optic Fiber                                                                                                             
                 RECEIPT                                                                                                        
                                                                                                                                
                                                                                                                                
          Buyer : Duke                                                                                                          
Total Optic Fiber Purchased: 10.0 ft                                                                                            
           Sub Total : $9.30                                                                                                    
        Sales tax(7%): $0.65                                                                                                    
          Total Cost : $9.95 
                                                                                                                                
                                                                                                                                
Thank you for shopping at DukeNet..!!                                                                                           
2019-09-18 15:21                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
...Program finished with exit code 0                                                                                            
Press ENTER to exit console.     
