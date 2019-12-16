#File: NERALLA_DSC510_WEEK2.py
#Name: Ravindra Neralla
#Course:DSC510-T303
#Date:12/15/2019
#Description: Calculate Total Cost of FiberOptic Cable Installation
#Display Welcome
print("Welcome to FiberOptics Inc");
#User to enter company name
company_name=input("Please enter your company name: \n")
print (company_name)
#Validate user entered cable length
while True:
  try:
    cable_length=float(input('\nHow many feet of fiber optic cable to be installed?\n'))
  except ValueError:
    print('Cable Length must be a number')
    continue
  if cable_length<=0:
    print('Cable Length must be a positive number')
  else:
    break
#cable cost aplied with bulk discount, based on length
if 100<cable_length<=250:
  price_per_feet=0.80
elif 250<cable_length<=500:
  price_per_feet=0.70
elif cable_length>500:
  price_per_feet=0.50
else:
  price_per_feet=0.87
#calculate total installation cost
TotalCost=round(cable_length*price_per_feet,2)

#printing receipt

print('\nRECEIPT');
print("Company Name: ",company_name);
print("Total Number of Feet of FiberOptic Cable to be Installed: ",cable_length);
print("Price Per Cubic feet: ",price_per_feet);
print("Total Cost of Installation: $",TotalCost);


