#May_DSC510_Assignment3.py
#Name: Brandon May
#Date: 9/8/19
#Course: DSC 510 - Introduction to Programming
#Descr: Purpose is to quote pricing for feet of fiber optic cable for the May company using conditional statements and booleans.
print('Welcome to the May Company')
companyname = input('What is your company name?\n')
print('Thank you for quoting your price with us', companyname)

try:
    cablefeet = float((input('How many feet of fiber optic cable are you requesting to be installed?\n')))  #designating we want this as a float
except:
    print('Please provide a numerical value.\n')
    cablefeet = float((input('How many feet of fiber optic cable are you requesting to be installed?\n')))
#exception statement if someone enters in a non-numerical value.

#designating the different formulas for calculation as variables

cablecost1=float((cablefeet)*0.87)   #$0.87 per foot up to 250 feet
cablecost2=float((cablefeet)*0.70)   #$0.70 per foot up to 500 feet
cablecost3=float((cablefeet)*0.50)   #$0.50 per foot greater than 500 feet

if float(cablefeet) <= 0:
    print('Error.  Please try again.') #want the program to end if entering a negative or zero value.

elif float(cablefeet) > 0 and float(cablefeet)<= 250.0:
    print('Attached is an invoice from the May company for', companyname, 'for', cablefeet, 'feet of fiber optic cable which will cost $',cablecost1,'\n')
    print('Thank you for your business!\n')
    #invoice printout for up to 250 feet but >0

elif float(cablefeet) > 250.0 and cablefeet <= 500.0:
    print('Attached is an invoice from the May company for', companyname, 'for', cablefeet, 'feet of fiber optic cable which will cost $',cablecost2,'\n')
    print('Thank you for your business!\n')
    #invoice printout for between 250 and 500 feet

elif float(cablefeet) > 500.0:
    print('Attached is an invoice from the May company for', companyname, 'for', cablefeet, 'feet of fiber optic cable which will cost $',cablecost3,'\n')
    print('Thank you for your business!\n')
    #invoice printout for >500 feet

