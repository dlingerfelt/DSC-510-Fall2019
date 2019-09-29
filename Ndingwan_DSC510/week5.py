# File: week5.py
# Name: Awah Ndingwan
# Date: 09/23/2019
# Desc: This program computes multiple inputs from the user and
# performs various calculations (addition, subtraction, multiplication, division, and average calculation)

import numpy as np

list_of_num = []


class Calculator:

    def __init__(self, user_input=0):
        self.user_input = user_input

        while True:
            print_message()
            self.get_user_input()
            self.calculate()

            user_input = input("Do you want to perform another operation? ")
            print(user_input)

            if user_input.lower().startswith("y"):
                continue
            elif user_input.lower().startswith("n"):
                print("Exiting Calculator...")
                exit()
            else:
                print("Not Valid! Your response is not valid")
                print("Exiting Calculator...")
                exit()

    # Get amd validate input from user
    def get_user_input(self):

        while True:
            try:
                self.user_input = int(input("Which operation do you want to perform?"))

                if self.user_input not in (0, 1, 2, 3, 4, 5):
                    print("Not Valid! Please select a number corresponding to an operation.")
                    continue

                elif self.user_input == 0:
                    print("Exiting Calculator...")
                    exit()

            except ValueError:
                print("Not Valid! Please select a number corresponding to an operation.")
                continue

            else:
                break

    def calculate(self):
        perform_calculation(self.user_input)


# print header for program
def print_message():
    print('****************************************')
    print('             Calculator                 ')
    print('****************************************')
    print("Please choose from the set of operations")
    print('Addition(+): 1')
    print('Subtraction(-): 2')
    print('Multiplication(*): 3')
    print('Division(/): 4')
    print('Calculate Average: 5')
    print('Exit Calculator: 0')
    print('****************************************')
    print("Please choose the a number to the corresponding operation")
    print('****************************************')


# perform calculation for various operations
def perform_calculation(operation):
    if operation == 1:
        input_validator()
        array_of_num = np.asarray(list_of_num)
        total_sum = np.sum(array_of_num)
        print(f'Sum of {list_of_num} is {round(total_sum, 2)}')

    elif operation == 2:
        subtraction_total = subtraction()
        print(f'Results of your inputs is {round(subtraction_total, 2)}')

    elif operation == 3:
        input_validator()
        array_of_num = np.asarray(list_of_num)
        multiplication_total = np.prod(array_of_num)
        print(f'Result of the multiplication of {list_of_num} is {round(multiplication_total, 2)}')

    elif operation == 4:
        division_total = division()
        print(division_total)

    elif operation == 5:
        input_validator()
        array_of_num = np.asarray(list_of_num)
        calculated_average = np.mean(array_of_num)
        print(f'Average of {list_of_num} is {round(calculated_average, 2)}')


# valid input and get values for add or multiply or calculate average calculations
def input_validator():
    while True:
        try:
            numbers_to_compute = int(input('How many numbers do you want to add or multiply or calculate average:'))

            for i in range(numbers_to_compute):
                num = float(input(f'Enter num {i + 1}: '))

                list_of_num.append(num)

        except ValueError:
            print("Not Valid! input cannot be a String. Please enter a valid number..")
            continue

        else:
            break


# compute values for subtraction
def subtraction():
    print("Subtraction")
    while True:
        try:
            sub1 = float(input('Enter num 1: '))
            sub2 = float(input('Enter num 2: '))

        except ValueError:
            print("Not Valid! input cannot be a String. Please enter a valid number..")
            continue

        else:
            return sub1 - sub2


# divide input from user
def division():
    print("Division")
    while True:
        try:
            dividend = float(input('Enter dividend: '))
            divisor = float(input('Enter divisor: '))

            if divisor == 0:
                print("Not Valid! Cannot divide by zero. Please enter valid divisor..")
                continue

        except ValueError:
            print("Not Valid! input cannot be a String. Please enter a valid number..")
            continue

        else:
            return dividend / divisor


if __name__ == "__main__":
    calculator = Calculator()
