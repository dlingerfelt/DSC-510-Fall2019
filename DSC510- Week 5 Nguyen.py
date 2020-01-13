'''
 File: DSC510-Week 5 Nguyen.py
 Name: Chau Nguyen
 Date: 1/12/2020
 Course: DSC_510 Intro to Programming
 Desc: This program helps implement variety of loops and functions.
 The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
 '''
def performCalculation(user_operation):
    # Using list will allow multiple inputs
    user_input = list(map(int, input("Enter multiple values: (no comma, just space) ").split()))
    if user_operation =="*":
          result = user_input[0] * user_input[1]
    elif user_operation =="%":
        try:
            result = user_input[0] / user_input[1]
        except:
            print("Error: Cannot Divide %s/%s" %(user_input[0], user_input[1]))
            return
    elif user_operation =="-":
        result = user_input[0] - user_input[1]
    elif user_operation =="+":
        result = user_input[0] + user_input[1]
    else :
        return float(result,2)
    print("Your calcualtion result is",result)

def calculateAverage():
    user_input2 = int(input('How many numbers they wish to input? '))
    total_sum = 0
    # Define store_input as list
    store_input = []
    for n in range(user_input2):
        x = (int(input("Enter your value ")))
        # Store user input into a list
        store_input.append(x)
    total_sum = sum(store_input)
    average = total_sum / user_input2
    print("The average is ", average)


def main():
    # Welcome statement
    print("Welcome. What program would you like to run today?")
    user_operation =''
    # Asking user to pick the program they want to run
    while user_operation != 'exist':
        user_operation = input("pick one of the choices: -,*,+,%,average, or exist ")
        if user_operation == 'exist':
            break
        elif (user_operation == '-') or (user_operation == '+') or (user_operation == '*') or (user_operation == '%'):
            performCalculation(user_operation)
        elif (user_operation == 'average'):
            calculateAverage()
        else:
            print("invalid choice try again")

if __name__ == '__main__':
    main()
