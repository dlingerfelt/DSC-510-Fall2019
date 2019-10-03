# File: week6.py
# Name: Awah Ndingwan
# Date: 10/02/2019
# Desc: This program receives different temperatures from the users and displays the max and min temperature

import numpy as np


class TemperatureApp:

    def __init__(self, user_input=0, list_of_temperatures=None):
        if list_of_temperatures is None:
            list_of_temperatures = []

        self.user_input = user_input
        self.list_of_temperatures = list_of_temperatures

        self.print_message()
        self.input_validator()
        self.get_temperature_min_max()

    # valid input and get values for add or multiply or calculate average calculations
    def input_validator(self):
        while True:
            try:
                amt_of_temperatures = int(input('How many temperatures do you want to enter? '))

                for i in range(amt_of_temperatures):
                    temperature = float(input(f'Enter temperature {i + 1}: '))

                    self.list_of_temperatures.append(temperature)

            except ValueError:
                print("Not Valid! input cannot be a String. Please enter a valid number..")
                continue

            else:
                break

    def get_temperature_min_max(self):

        array_of_temperature = np.asarray(self.list_of_temperatures)

        max_temperature = np.max(array_of_temperature)
        min_temperature = np.min(array_of_temperature)

        temperature_count = np.size(array_of_temperature)

        print(f"The max temperature is {max_temperature} °C")
        print(f"The min temperature is {min_temperature} °C")

        print(f"You entered {temperature_count} temperatures to the list")

        print(f"Here's the list of temperatures {self.list_of_temperatures} ")

    # print header for program
    def print_message(self):
        print('****************************************')
        print('             Temperature App            ')
        print('****************************************')
        print("  Enter Temperature to get Min and Max  ")
        print('****************************************')
        print("    Enter Temperature in Celsius(°C)     ")
        print('****************************************')


if __name__ == "__main__":
    temperatureApp = TemperatureApp()
