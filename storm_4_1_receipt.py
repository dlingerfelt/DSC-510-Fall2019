# method to calculate the total installation cost for the fiber cable using a function
# 4-1
# Joy Storm

def calCost(len_in_feet, price):
    tot_cost = len_in_feet * price
    return tot_cost


def calculate_total_cost(len_in_feet):
    # method to calculate the total installation
    # cost for the fiber cable using a function

    # check for feet entered is valid or not
    if len_in_feet > 0:
        # checks for number of feet greater than 100 and less than 250
        if len_in_feet > 100 and len_in_feet < 250:
            total_cost = calCost(len_in_feet, 0.80)

        # checks for number of feet greater than 250 and less than 500
        elif len_in_feet > 250 and len_in_feet < 500:
            total_cost = calCost(len_in_feet, 0.70)

        # checks for number of feet greater than 500
        elif len_in_feet > 500:
            total_cost = calCost(len_in_feet, 0.50)

        # for all other conditions less than 100
        else:
            total_cost = calCost(len_in_feet, 0.87)
        return total_cost

    elif len_in_feet < 0:
        return 0


if __name__ == '__main__':
    print('-----------WELCOME-------------')

    # ask for company name as input from user
    company_name = input(' Enter your company name ')

    # ask the length per foot of fiber cable as input
    len_in_feet = int(input(' Enter the length of fiber cable per foot '))

    # call the method to calculate the total installation cost
    installation_cost = calculate_total_cost(len_in_feet)

    # print the receipt consisting of company name, length in feet and installation cost
    print('--------- Your Receipt-----------')

    print('Company name:', company_name)

    print('Length of fiber cable per foot: {}'.format(len_in_feet))

    print(f'Installation cost: ${installation_cost:,.2f}')
