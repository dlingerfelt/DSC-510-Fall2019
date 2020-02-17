'''
File: NERALLA_DSC510_WEEK10.py
Name: Ravindra Neralla
Course:DSC510-T303
Date:02/16/2020
Description: This program is to connect to check norris webservice and get jokes from the webservice as response.

'''

import requests


def fetch_jokes():
    try:
        url = "https://api.chucknorris.io/jokes/random"  # URL to call the webservice
        joke_response = requests.get(url, timeout=5)  #  to fetch the joke from webservice, timeout in 5 sec
        joke_response_json = joke_response.json()  # Converting the response to json format
        print('Joke to read : ' + joke_response_json['value'])
    except:
        print("Error Occured while fetching joke from Chuck Norris")


def main():
    print("***************************Welcome to Chuck Norris Jokes ****************************")

    while True:
        try:
            no_input = ['n', 'no', 'stop', 'nope','quit','q']
            yes_input = ['y', 'yes', 'sure', 'yeah', 'yup', 'ya', 'ok','k']


            jokes_input  = input("'Hello, Would you like a Chuck Norris Joke?' : ")

            if jokes_input.lower() in no_input:
                break
            elif jokes_input.lower() in yes_input:
                fetch_jokes()
            else:
                raise

        except:
            print("Please enter y to read jokes or n to exit the program")
    exit()


if __name__ == '__main__':
    main()
