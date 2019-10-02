#%%
#File: Assignment 6
#Name: April Meyer
#Assignment 6
#Date: 10.02.2019
"""A program which creates a list of temperatures based upon user input.
It will determine the number of temperatures in the program, the largest temperature,
and the smallest temperature.
"""

temp_list = []
userTemp_input = input('Please enter a temperature: \n' + 'Type "Done" when you have entered all temperatures')
while userTemp_input:
    userTemp_input = input('Please enter a temperature: \n' + 'Type "Done" when you have entered all temperatures')
    if userTemp_input.lower() == 'done': #check for sentinel value
        break
    try:
        t2 = temp_list.append(float(userTemp_input)) #verifies float number
    except ValueError:
        userTemp_input = input('Invalid input. Please enter a numeric number.')#reprompts user
    #print(temp_list) #used for testing
print(temp_list)
print('The maximum temperature is: ', max(temp_list), 'degrees') #returns max temperature
print('The minimum temperature is: ', min(temp_list), 'degrees') #returns min temperature
print('The total number of temperatures entered are ', len(temp_list)) #returns count of numbers