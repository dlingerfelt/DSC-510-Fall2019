'''
File: process.py
Name: Mohammed A. Frakso
Date: 02/09/2020
Course: DSC_510 - Introduction to Programming
Desc: This program will  work with a text file to perform the following actions:
Open the file and process each line.
Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
new function called process_file which prints to the file (this method should almost be the
same as the pretty_print function from last week. Keep in mind that we have print statements in main as well.
The program must modify the print statements from main as well.
'''

import string

# Create add_word
def add_word (word, w_count_dict):
    if word not in w_count_dict:
        w_count_dict[word] = 1
    else:
        w_count_dict[word] = w_count_dict[word] +1

# Create process_line function in order to strip off various characters, split out the word

def process_line (line, w_count_dict):
    line = line.translate(str.maketrans('', '', string.punctuation))

    line = line.lower()  #  lines transformation, split  the words
    words = line.split()
    for word in words:
        add_word(word,   w_count_dict)

#Process_file function for processing file

def process_file(file_name, dictionary):
    total = 0
    for word in dictionary:
        total += 1

    output = open(file_name,     'w')

    output.write('Length of dictionary:      %s\n'% total)  # Printing in alphabetical order
    output.write('   Word           Count\n')
    output.write('----------    ----------\n')
    for word in sorted(dictionary.keys()):
        output.write('%s: %d\n' % (word, dictionary[word]))
    output.close()
    return

#define main() function
def main():
    dictionary = {}
    gba_file = open('C:\\Users\\ss\\Desktop\\Gettysburg.txt', 'r')  # store txt in python assignment folder
    for line in gba_file:
        process_line(line, dictionary)

    file_name = input('How do you want to name the output file?\n')
    process_file(file_name, dictionary)
    return
if __name__ == '__main__':
    main()
