'''
 File: DSC510-Week 10 Nguyen.py
 Name: Chau Nguyen
 Date: 2/16/2020
 Course: DSC_510 Intro to Programming
 Description: Learning how to utilize python code to grab data from web API based on number of request from user
 '''
import json
import requests
def grab_jokes():
    try:
        response= requests.get('https://api.chucknorris.io/jokes/random')
#Currently in Json -- need to parse and convert to python object
        jokes_4days = json.loads(response.text)
#check status: 200 show = successful
       # print(response.status_code)
        print("The joke is {}\t".format(jokes_4days['value']))
    except Exception as e:
        print("{}".format(e.status_code))
        print('Please double check API URL')


def main():
    print("This program will print a joke from Chuck Norris.")
    print('Would you like to hear a joke from Chuck Norris?')
    #Define Variables
    possible_no = ['no','n']
    possible_yes = ['yes','y']
    user_input = ''
    program = True
    while True:
        user_input = input("Please respond with a 'yes' or 'no' ")
        user_input= user_input.lower()
        if user_input in possible_no:
            break
        elif user_input in possible_yes:
            grab_jokes()
            print('One more joke?')
        else:
            print('Response not valid. Please enter yea or no')
if __name__ == '__main__':
    main()





