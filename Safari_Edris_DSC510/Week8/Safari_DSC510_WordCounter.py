# File : Safari_DSC510_WordCounter.py
# Name:Edris Safari
# Date:10/17/2019
# Course: DSC510 - Introduction To Programming
# Desc:
# This program performs three essential operations.
# 1. It opens the file Gettysburg.txt and reads it line-by-line.
# 2. It calculates and displays the total number of words in the file.
# 3. It calculates and displays the number of occurrences of each word in a tabular form.
# Assumptions:
# punctuation marks will not be considered as prt of a word.
# For example "Results:" and "Results:" are considered the same word and will be counted as repeating twice.
# words with different cases will also be considered the same. The words "SaMe" and " "SAme" are the same
# and will be counted as repeating twice.
# Usage: Provide file in the sme folder as this program. Program exists with an error message if fine not found.


import string

# Globals
# max_table_size controls the width of the output table in pretty_print()
max_table_size = 30

def add_word(word, filecontent):
    # This function adds the word to the dictionary.

    # Add word to dictionary and update the key value which is the number of occurrences of the word.
    # The statement filecontent.get(word, 0) results in 0 if the word is not in the dictionary and
    # its current value otherwise.
    filecontent[word] = filecontent.get(word, 0) + 1


def process_line(line, filecontent):
    # This function take a line of characters as input.
    # it will extract words from the line by first removing punctuation characters from the line,
    # and changing all characters to lowercase, it then calls the add_word function to add it the
    # dictionary filecontent.

    # Strip the end of line from this line
    line = line.rstrip()
    # remove all punctuations in this list '!"# $%&\'()* +,-./:; < = >?@[\\] ^_ `{ |} ~'
    line = line.translate(line.maketrans('', '', string.punctuation))
    # convert all characters to lower case
    line = line.lower()
    # Split the line to words separated by blank characters
    words = line.split()
    # Add each word in the line(stored in 'words') and increment its count
    for word in words:
        # add to dictionary with count value of 1 if word does not exist in dictionary
        # otherwise, get the current count and increment by one.
        add_word(word, filecontent)


def pretty_print(filecontent):
    # This function prints the output result.
    # It displays the value and key of the dictionary in a tabular format.

    lst = list()
    for key, val in list(filecontent.items()):
        lst.append((val, key))
    # List is reversed to show words in ascending order and word count in descending order
    lst.sort(reverse=True)
    print("Length of the dictionary: " + str(len(filecontent)))
    # Calculations to place blanks between column headers are based on max_table_size.
    print("Word" + " " * (max_table_size - (len("word") + len("Count"))) + "Count")
    # Print header separator
    print("-" * max_table_size)
    for key, val in lst:
        # Number pf spaces between values in calculated based on max_table_size as above
        print(str(val) + " " * (max_table_size - (len(str(val)) + len(str(key)))) + str(key))


def main():
    # The main function of this program will open the file,
    # processes the file line-by-line,
    # then prints the number of words in the file
    # followed by each word and the number of repetitions in a tabular format.
    filecontent = dict()
    # Open the file in a try and except to handle error condition better
    try:
        input_file = open("gettysburg.txt")
        # For each line in the file
        for line in input_file:
            # The function below processed the line and updates the filecontent dictionary
            process_line(line, filecontent)

        pretty_print(filecontent)
        input_file.close()
    except:
        print("File not found")
        exit()




if __name__ == '__main__':
    main()
else:
    print("This Module's name is :" + __name__)
