#  Program Name: optic_cable_week3.py
#  Purpose : This program asks users for number of feets of optical fiber cable,
#  Calculates total cost and offers bulk discount based on number of feet purchased
#  Assignment Name : 3.1 Programming Assignment
#  Name : Mohit Matta


# Input user/buyer's Name and store in a variable
input_welcome_name = input("What is buyer's name?\n")

# Display welcome message for the buyer
print("Welcome", input_welcome_name, "to the optic cable company!")

#Input Company Name and store in a variable
input_company_name = input("What is your company name?\n")

#Take the input of number of feet from the user
input_cable_length = float(
    input("How many feet of optic fiber cable you need to install?\n"))

# Calculation

if input_cable_length <= 100:
  #Calculate the subtotal amount at .87$ per feet
  subtotal = input_cable_length * 0.87

    #Calculate the tax amount with a standard sales tax of 8%
  tax = subtotal * .08

    #Calculate total cost
  total_cost = subtotal + tax
     #Print Final Receipt/Invoice

  print("                  INVOICE")
  print("Company Name:", input_company_name)
  print("Number of feet of cable to be installed:", input_cable_length)
  print("Price per feet: $0.87")
  print("Subtotal amount:", ' $',format(subtotal, ",.2f"),sep='')
  print('Tax amount@8%:', ' $',format(tax, ",.2f"), sep='')
  print('Total amount is:', ' $',format(total_cost, ",.2f"), sep='')

elif input_cable_length <= 250:

    if float(input_cable_length) > 100:
        #Calculate the subtotal amount at .80$ per feet
       subtotal = input_cable_length * 0.80

       #Calculate the tax amount with a standard sales tax of 8%
       tax = subtotal * .08

       #Calculate total cost
       total_cost = subtotal + tax
       #Print Final Receipt/Invoice

       print("                  INVOICE")
       print("Company Name:", input_company_name)
       print("Number of feet of cable to be installed:", input_cable_length)
       print("Price per feet: $0.80")
       print("Subtotal amount:", ' $',format(subtotal, ",.2f"),sep='')
       print('Tax amount@8%:', ' $',format(tax, ",.2f"), sep='')
       print('Total amount is:', ' $',format(total_cost, ",.2f"), sep='')

elif input_cable_length <= 500:
    if float(input_cable_length) > 250:
      #Calculate the subtotal amount at .70 per feet
       subtotal = input_cable_length * 0.70

      #Calculate the tax amount with a standard sales tax of 8%
    tax = subtotal * .08

      #Calculate total cost
    total_cost = subtotal + tax
       #Print Final Receipt/Invoice

    print("                  INVOICE")
    print("Company Name:", input_company_name)
    print("Number of feet of cable to be installed:", input_cable_length)
    print("Price per feet: $0.70")
    print("Subtotal amount:", ' $',format(subtotal, ",.2f"),sep='')
    print('Tax amount@8%:', ' $',format(tax, ",.2f"), sep='')
    print('Total amount is:', ' $',format(total_cost, ",.2f"), sep='')

else:
  input_cable_length >= 500
     #Calculate the subtotal amount at $.50 per feet
  subtotal = input_cable_length * 0.50
    #Calculate the tax amount with a standard sales tax of 8%
  tax = subtotal * .08

    #Calculate total cost
  total_cost = subtotal + tax
   #Print Final Receipt/Invoice

  print("                  INVOICE")
  print("Company Name:", input_company_name)
  print("Number of feet of cable to be installed:", input_cable_length)
  print("Price per feet: $0.50")
  print("Subtotal amount:", ' $',format(subtotal, ",.2f"),sep='')
  print('Tax amount@8%:', ' $',format(tax, ",.2f"), sep='')
  print('Total amount is:', ' $',format(total_cost, ",.2f"), sep='')
