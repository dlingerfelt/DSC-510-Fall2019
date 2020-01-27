'''
File: lists.py
Name: Mohammed A. Frakso
Date: 19/01/2020
Course: DSC_510 - Introduction to Programming
Desc: This program will  work with lists:
The program will contains a list of temperatures, it will populate the list based upon user input.
The program will determine the number of temperatures in the program, determine the largest temperature, and the smallest temperature.
'''
# create an empty list

temperature_list = []
while True:
    print('\n Please enter a temperature:')

#print('Enter "finished" once you are done with all temparatures: \n')

    input_temperature = input('please type "finished" when you have entered all temperatures')
    if input_temperature.lower() == 'finished':
        break
    try:
        temperature_list.append(float(input_temperature))
    except ValueError:
        input_temperature = input('Oops... Please enter a numeric value!')
        temperature_list.append(float(input_temperature))

# printing argest, smallest  temperatures and how many temperatures are in the list.

print('The largest temperature is: ', max(temperature_list), 'degrees')
print('The smallest temperature is: ', min(temperature_list), 'degrees')
print('The total temperatures input is: ', len(temperature_list))