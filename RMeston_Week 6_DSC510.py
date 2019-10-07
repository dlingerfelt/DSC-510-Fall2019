# File: Week 6 Assignment
# Name: Ryan Meston
# Date: 20191006
# Course: DSC510
# Desc: Week 6 Assignment
# Usage: Create empty temperature list. Allow user to add inputs, print large and smallest temp.

temperature_list = []
# this will ask the user how many temps they would like to list.
num = int(input('How many temperatures would you like to list?: '))
# this will ask the user to list each number.
for n in range(num):
    numbers = int(input('Enter number '))
    temperature_list.append(numbers)
print('Max temperature in the list is: ', max(temperature_list))
print('Min temperature in the list is: ', min(temperature_list))


