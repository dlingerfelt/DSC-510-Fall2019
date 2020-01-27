'''
File: NERALLA_DSC510_WEEK6.py
Name: Ravindra Neralla
Course:DSC510-T303
Date:01/14/2020
Description: This program will perform the below list of items.
        Create an empty list called temperatures.
		Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
		Evaluate the temperature list to determine the largest and smallest temperature.
		Print the largest temperature.
		Print the smallest temperature.
		Print a message tells the user how many temperatures are in the list.

'''
# create an empty list and name it as temp_list

temp_list = []
while True:
    print('\n Plese enter a temparature:')
    #print('Enter "Done" when you are done with all temparatures: \n')
    input_temp = input('Type "Done" when you have entered all temperatures')
    if input_temp.lower() == 'done':  # check for sentinel value
        break
    try:
        temp_list.append(float(input_temp))  # verifies float number and adds to list
    except ValueError:
        input_temp = input('Invalid input. Please enter a numeric number.')
        temp_list.append(float(input_temp))
# print(temp_list) #for testing what is in the list
print('The maximum temperature is: ', max(temp_list), 'degrees')  # returns max temperature
print('The minimum temperature is: ', min(temp_list), 'degrees')  # returns min temperature
print('The total number of temperatures entered are ', len(temp_list))  # returns count of numbers