# File : Safari_DSC510_Cable_Cost.py
# Name:Edris Safari
# Date:9/6/2019
# Course: DSC510 - Introduction To Programming
# Desc: Get name of company and length in feet of fiber cable. compute cost at $.87 per foot. display result in recipt format.
# Usage: Provide input when prompted.

print("Welcome to Fiber Optics One.")
print("Please tell us the name of your company")
Company_Name = input()

print("Thank You.")
print("Now, please tell us the length in feet of cable you need. Enter 'q' to exit.")
Cable_Length = input()
while Cable_Length.lower() != 'q':
    if not Cable_Length.isnumeric():
        print("PLease enter a a valid number.")
    else:
        Installation_Cost = float(Cable_Length) * 0.87
        Tax = Installation_Cost*.083;
        Installation_Cost_PlusTax = Installation_Cost + Tax
        print("Thank You. Here's your receipt.")
        print("Company Name: " + Company_Name)
        print("Cable Length: " + Cable_Length)
        print("Cost for " + Cable_Length + " feet of cable at $.87 per foot is $" + str(format(Installation_Cost, '.2f')) + ".")
        print("Tax at 8.3% is $: " + str(format(Tax, '.2f')) + ".")
        print("Total cost for " + Cable_Length + " feet of cable at $.87 per foot is $" + str(format(Installation_Cost_PlusTax, '.2f')) + ".")

    print("Please enter another length in feet of cable you need. Enter 'q' to exit.")
    Cable_Length = input()
print("Thank You. Please come back.")