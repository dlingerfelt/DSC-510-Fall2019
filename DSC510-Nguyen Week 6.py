'''
 File: DSC510-Week 5 Nguyen Week 6.py
 Name: Chau Nguyen
 Date: 1/19/2020
 Course: DSC_510 Intro to Programming
 Desc: This program helps building more knowledge in string and list properties and methods.
 '''
def main():
    #Define Variables
    user_input = ''
    temperature =[]
    print("Please input your temperature. Note temperatures are in Fahrenheit")
    while user_input != 'stop': #sentinel value
        user_input = input("input a value, or stop ")
        if user_input == 'stop':
            break
        try:
            temp_input = int(float(user_input)) #Check if input is numerical
            temperature.append(float(user_input))
        except ValueError:
            user_input = input("enter a nemeric value")
            temperature.append(float(user_input))
    print("This is the list of the temperature inputted",temperature)
    temperature.sort()
    print("Total number of temperature inputted is",(len(temperature)))
    print("The lowest temperature is",temperature[0])
    print("The highest temperature is",max(temperature))
if __name__ == '__main__':
    main()



