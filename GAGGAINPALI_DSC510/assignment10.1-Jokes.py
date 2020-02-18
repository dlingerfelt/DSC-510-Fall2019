# File : assignment10.1-Jokes.py
# Name : Bhargava Gaggainpali
# Date : FEB-16-2020
# Course : Introduction to Programming - python
# Assignment :
#- Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
#- The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
#- Your program should allow the user to request a Chuck Norris joke as many times as they would like. You should make sure that your program does error checking at this point. If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user. There are other ways to handle this. Think about included string functions you might be able to call.
#- Your program must include a header as in previous weeks.
#- Your program must include a welcome message for the user.
#- Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty."
# Desc : Program to fetch a joke from the website based on the user input.
# Usage :
# -User is requested to choose to read or quit the program which is used to fetch a joke from a website.

import requests

def Get_Chuck_Norris_Joke():
    try:
        url = "https://api.chucknorris.io/jokes/random"  # URL to call the webservice
        Chuck_Norris_response = requests.get(url, timeout=5)  #  to fetch the joke from webservice, timeout in 5 sec
        Chuck_Norris_response_json = Chuck_Norris_response.json()  # Converting the response to json format
        print('\nHere is Joke from Chuck Norris : ' + Chuck_Norris_response_json['value'])
    except:
        print("Error Occured while fetching joke from Chuck Norris")


#main() function
def main():
    print("\n---------------------------------------------")
    print("\Welcome to 'Chuck Norris Jokes Program'..!!")
    print("---------------------------------------------")
    while True:
        try:
            no_list = ['n', 'N']
            yes_list = ['y', 'Y']
            user_input  = input("\nPlease Enter 'Y' to read a Chuck Norris Joke or Enter 'N' to exit the Program : ")

            if user_input.lower() in no_list:
                break
            elif user_input.lower() in yes_list:
                Get_Chuck_Norris_Joke()
            else:
                raise

        except:
            print("Please enter y to read a joke or n to exit the program")
    print("\nThank you for using 'Chuck Norris Jokes Program'.")
    print("-------------------------------------------------")
if __name__ == '__main__':
    main()
