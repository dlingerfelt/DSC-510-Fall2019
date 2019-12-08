#File: NERALLA_DSC510_WEEK2.py
#Name: Ravindra Neralla
#Course:DSC510-T303
#Date:12/08/2019
#Description: Calculate Total Cost of FiberOptic Cable Installation
#Display Welcome
print("Welcome to FiberOptics Inc");
#User to enter company name
company_name=input("Please enter your company name: \n")
print (company_name);
#Get the length of cable needed from user
quantity=float(input("Please Enter number of feet of fiber optic cable needed: \n" ))
#Assign price per cubic feet
price_per_feet=0.87
#Calculate the total cost
TotalCost=quantity*price_per_feet;
#Print receipt
print('RECEIPT');
print("Company Name: ",company_name);
print("Price Per Cubic feet: ",price_per_feet);
print("Total Number of Feet of FiberOptic Cable to be Installed: ",quantity);
print("Total Cost of Installation: $",TotalCost);

