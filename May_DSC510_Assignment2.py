#May_DSC510_Assignment2_1.py
#Name: Brandon May
#Date: 8/29/19
#Course: DSC 510 - Introduction to Programming
#Descr: Purpose is to quote pricing for feet of fiber optic cable for the May company.
print('Welcome to the May Company')
companyname = input('What is your company name?\n')
print('Thank you for quoting your price with us', companyname)
(cablefeet)= float(input('How any feet of fiber optic cable are you requesting to be installed?'))
#designating that we want this as a float
cablecost=float((cablefeet)*0.87)
#designating that want this to be in float, not an integer since we're talking about cost
print('Your estimated cost is $', cablecost)
print('Attached is an invoice from the May company for', companyname, 'for', cablefeet, 'feet of fiber optic cable which will cost $', cablecost, 'at $0.87 per foot of cable.\n')
print('Thank you for your business!\n')


