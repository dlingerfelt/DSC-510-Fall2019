#File: Assignment 10
#Name: April Meyer
#Assignment 10
#Date: 11.1.2019
"""This program will receive a JSON response from a Chuck Norris API. It will parse the JSON data to obtain the “value” key which is the joke.
The joke will be displayed as a message box. It will continue to prompt the user if they want another joke.
It will display a error message if the user response is not in the no or yes set.
"""
import requests
import easygui

no_set = ['n','no','go away','stop', 'nope', 'nah', 'no way', 'nay']
yes_set = ['y','yes','sure','why not','aye','i agree','okey dokey','okay','yeah','yup','ya','ok','k','alright','alrighty','sounds good','certainly', 'definitely', 'of course', 'gladly']
full_set = no_set + yes_set
userTemp_input = easygui.enterbox(msg='Hello, Would you like a Chuck Norris Joke?', title='Please Confirm', default='', strip=True) #prompts user input
while True: #continues to loop until user inputs no
    if userTemp_input.lower() in no_set: #check value in no set
        break
    if userTemp_input.lower() in yes_set: #check value in yes set
        response = requests.get("https://api.chucknorris.io/jokes/random") #gets the request
        joke_response = response.json() #assigns the response
        userTemp_input = easygui.enterbox(msg=" {} \n\n\n Would you like another joke? ".format(joke_response['value']), title="Chuck Norris Joke", default='', strip=True)
    if userTemp_input.lower() not in full_set : #all other inputs will receive this message
        userTemp_input = easygui.enterbox(msg="Invalid Input. Please try again using yes/no.", title="Error", default='', strip=True)
easygui.msgbox(msg="All done! Have a good day!", title="End", ok_button="OK") #message once user inputs a no set
