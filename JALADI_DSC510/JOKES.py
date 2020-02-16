# File :    JOKES.py
# Name :    Pradeep Jaladi
# Date :    02/10/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#   Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
#   The program will receive a JSON response which includes various pieces of data.
#   You should parse the JSON data to obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
#   Your program should allow the user to request a Chuck Norris joke as many times as they would like.
#    You should make sure that your program does error checking at this point.
#       If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user.
#       There are other ways to handle this. Think about included string functions you might be able to call.
#   Your program must include a header as in previous weeks.
#   Your program must include a welcome message for the user.
#   Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”
# Desc : Fetchs a joke and prints it to the output for user
import requests


def fetch_jokes():
    try:
        url: str = "https://api.chucknorris.io/jokes/random"  # URL to call
        response = requests.get(url, timeout=1)  # fetching the joke, timeout in 1 sec
        json_response = response.json()  # Converting to dictionary for easy access
        print('Joke to read : ' + json_response['value'])
    except:
        print("error in getting the joke")


def main():
    print("*************************Welcome to Chuck Norris Jokes program*************************")

    while True:
        try:
            jokes_input: str = input("Enter Y to read more jokes, or Q to quit the program : ")
            if jokes_input.upper() == 'Q':
                break
            elif jokes_input.upper() == 'Y':
                fetch_jokes()
            else:
                raise

        except:
            print("Please enter y to read jokes or q to exit the program")
    exit()


if __name__ == '__main__':
    main()
