# Desc: File describes the need of fiber optic cable, including math operations.
# Name: Aritzi Piedras Silva
# Assignment number: 2.1

# Display Welcome Message
print('welcome to my program')
# Company Name will be prompted
company = input('what is your company name:')
print(company)
feet = input('how many feet in length for' + company)  # receive the ft at company
# Now, let's find out the cost of fiber optic cable times feet
# rate per ft will represent to cost per feet
rate_per_feet = 0.87
# I will now calculate cost of installation cost
installation_cost = float(feet) * rate_per_feet
print(installation_cost)

# i will now print out the receipt
print("FINAL RECEIPT")
print("Company name:", company)
print("Installation rate:$", rate_per_feet)
print("length in feet:", feet)
print("Total cost:$", installation_cost)

















