# File: Assignment 6.1 - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 12/17/2019
# Course: DSC510 - Introduction to Programing
# Desc: Program will determine largest and smallest temperature.
# Usage:  The program will get a list of temperatures from user input
#         store them in a list and determine the largest and smallest
#         temperature. It will then print the largest and smallest
#         temperature. It will then print how many temperatures in the list

# create empty list
temperatures = []

loop = True;

print("Welcome to the Temperature program! Enter temps and get the highest and lowest in return.\n")

# while loop to get multiple temperatures
while loop:

    # get temperatures from user
    temperatures.append(input("Please input a temperature.\n"))

    # sentinel input to end or continue loop
    answer = input("Would you like to add another temperature? Please input 'yes' or 'no'.\n")

    # if statement to get more input or display information and end
    if answer == "no":

        # sort list to get highest and lowest temp
        temperatures.sort(key=int)

        print("\nThe highest temperature is ", str(temperatures[-1]), " degrees")
        print("\nThe lowest temperature is ", str(temperatures[0]), " degrees", "\n")
        print("\nYou entered ", len(temperatures), "temperatures")

        loop = False

    elif answer == "yes":
        loop = True
