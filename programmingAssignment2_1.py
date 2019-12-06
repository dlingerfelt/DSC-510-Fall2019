"""
File: programmingAssignment2_1
Name: Kim Gonzalez
Date: 12/4/2019
Course: DSC510-T303 Introduction to Programming
Desc: Program calculates quantity and costs of fiber optic cable needed by customer
        and prints receipt.
In: Company name from user, number of feet of fiber optic cable needed
Out: Receipt for user to include:
        company name
        number of feet of fiber to be installed
        calculated cost (num of feet  * $0.87) in legible format
Include appropriate comments throughout program
"""


welcome = "Welcome to Fiber Optic Express!"
print(welcome)
companyName = input("Please provide your company name.\n")
customizedGreeting = "Thank you " + companyName + "!"
fibreOpticNeeded = input("Please provide the number of ft of fiber optic cable to be installed.")
print("Thank you! Please wait while we calculate costs.")
cost = float(fibreOpticNeeded) * 0.89
receipt = f"""

Invoice #23456:
        Thank you {companyName}!
        Num. of ft of Fiber Optic Cable to be installed is {fibreOpticNeeded}.
        Total for installation is ${cost}
        Thank you!
        """
print(receipt)

