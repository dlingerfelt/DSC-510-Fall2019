def calculate_total_cost(number_of_feet: object) -> object:
    # method to calculate the total installation cost for the fiber cable
    # 3-1
    # Joy Storm

    # check for feet entered is valid or not
    if (number_of_feet > 0):

        # checks for number of feet greater than 100 and less than 250
        if (number_of_feet > 100 and number_of_feet < 250):
            total_cost = number_of_feet * 0.80

        # checks for number of feet greater than 250 and less than 500
        elif (number_of_feet > 250 and number_of_feet < 500):
            total_cost = number_of_feet * 0.70

        # checks for number of feet greater than 500
        elif (number_of_feet > 500):
            total_cost = number_of_feet * 0.50

        # for all other conditions less than 100
        else:
            total_cost = number_of_feet * 0.87
        return total_cost

    elif (number_of_feet < 0):
        return 0

if __name__ == '__main__':
    print("-----------WELCOME-------------")

    # ask for company name as input from user
    company_name = input(" Enter your company name ")

    # ask the number of feet of fiber cable as input
    number_of_feet = int(input(" Enter the number of feet of fiber cable "))

    # call the method to calculate the total installation cost
    installation_cost = calculate_total_cost(number_of_feet)

    # print the receipt consisting of company name, number of feet and installation cost
    print("--------- Your Receipt----------- ")

    print("Company name :", company_name)

    print("Number of feet of fiber cable : {}".format(number_of_feet))

    print(f"Installation cost : ${installation_cost:,.2f}")
