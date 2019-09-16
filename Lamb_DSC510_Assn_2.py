#Lamb_DSC210_Assn_2
#Name: Danielle Lamb
#Date: 09/6/2019
#Course: DSC510 Introduction to Programming
#Desc: Calculating cost of purchasing and installing fiber optic cable
print('Welcome to Outstanding Optics!')
print('Can we help you purchase and install fiber optic cable?')
PurchasingCompany = input('What is your company name?\n')
FeetRequested = float(input('How many feet of cable do you require?\n'))
#float is required in case purchase is not an integer
InstallCost = float(str(round(FeetRequested*0.87,2)))
#rounding to two decimal places provides company with correct monitary format
print('The total for',PurchasingCompany,'for',FeetRequested,'feet of fiber optic cable is $',InstallCost)
print('Thank you for choosing Outstanding Optics for your fiber optic cable needs. Please visit us again!')

