# File :    MATH_OPERATIONS.py
# Name :    Pradeep Jaladi
# Date :    01/11/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
# Program :
#    Create an empty list called temperatures.
#    Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
#    Evaluate the temperature list to determine the largest and smallest temperature.
#    Print the largest temperature.
#    Print the smallest temperature.
#    Print a message tells the user how many temperatures are in the list.

def print_values(temperatures):
    length: int = len(temperatures)

    # there are couple of ways to determine the min & max of the list -> using max & min function or sort the list and get 0, max length element
    print('There are total %d temperature values ' % length)
    print('The lowest temperature is %g and the highest temperature is %g' % (min(temperatures), max(temperatures)))


def main():
    print("Welcome to temperature calculator program ....")

    # Declaration of empty temperatures list
    temperatures = [];

    # Getting the temperature values
    while True:
        temperature: str = input("Enter the temperature [%d] : " % len(temperatures))
        if temperature == 'q':
            break
        try:
            temperatures.append(float(temperature))
        except ValueError:
            print("Oops!  Invalid temperature.  Try again...")

    # printing the desired calucations
    print_values(temperatures)


if __name__ == '__main__':
    main()
