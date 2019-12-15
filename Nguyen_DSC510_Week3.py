# File: .py file
# Course: DSC 510
# Name: Chau Nguyen
# Date: 12/15/2019
# Description: This assignment focus on the application of conditional statements.
print("Welcome to Fiber Optical") #Welcoming statement
user_company = input('What company are you working for?') #Ask user to input company name
print("You work for " + user_company)
#Ask user to input number of feet needed
fiber_needed = input('How many feet of fiber optical cable you are looking to install?')
# This next step convert str to int for conditional statement
try: # Checking error if user input non-numeric value
    fiber_needed = int(fiber_needed)
except:
    print("The number you entered was not an integer. Please re-enter")
    fiber_needed = input('How many feet of fiber optical cable you are looking to install?')
print("Your looking to buy",fiber_needed,"ft of fiber.")
a = 500
b = 250
c = 100
if fiber_needed >= 500:
    print(f'Thank for purchasing more than 500ft of fiber.\n'
          f'Due to your high purchase volume, your cost per foot is .50c \n'
          f'cost = number of feet needed * .50c')
    Cost = fiber_needed * .50
    final_cost = round(Cost,2) #Round number to 2 decimal for dollar value
elif 250 <= fiber_needed <= 500:
    print(f'Thank for purchasing more than 250ft of fiber.\n'
          f'Due to your high purchase volume, your cost per foot is .70c \n'
          f'cost = number of feet needed * .70c')
    Cost = fiber_needed * .70
    final_cost = round(Cost,2) #Round number to 2 decimal for dollar value
elif 100 <= fiber_needed <= 250:
    print(f'Thank for purchasing more than 100 ft of fiber.\n'
          f'Due to your high purchase volume, your cost per foot is .80c \n'
          f'cost = number of feet needed * .80c')
    Cost = fiber_needed * .80
    final_cost = round(Cost,2) #Round number to 2 decimal for dollar value
else:
    print(f'Thank for purchasing',fiber_needed,'feet of fiber\n'
          f'Your cost per foot is .87c \n'
          f'cost = number of feet needed * .87c')
    Cost = fiber_needed * .87
    final_cost = round(Cost,2) #Round number to 2 decimal for dollar value
print("Your purchase final cost is $",final_cost,)
receipt = "t394343fda"
print(f'Receipt\n'
      f'Thank you {user_company} for your inquiry of {fiber_needed} feet of fiber optical cable.\n' #\n is for line break
      f'Your total cost is ${final_cost} \n' #f' is formatted string literals; skip string identification
      f'Your receipt number is {receipt}')
