# File: 9.1 Assignment.py
# Name: Vilius Smilinskas
# Date: 2/9/2020
# Course: DSC510: Introduction to Programming
# Desc: Program will ask for an input file dissect its words and create a file with the desired name with the info.
# Usage: Run the program, input .txt file name, and output name. If input file is not in root with program use full path.

import string  # importing string for string.punctuation which contains different punctuation to clear text from formating
counts = dict()  # variable set as a empty dictionary


def main():
    file_name = input('Enter the name of the file, or its full root path:')
    try:
        file_use = open(file_name, 'r')   # opens inputted file
        output_name = input('Enter the desired file name for the results:')
        if '.txt' not in output_name:   # makes sure of the formatting for the output
            output_final = output_name + '.txt'  # if .txt doesn't exist, add it
        else:
            output_final = output_name
        for line in file_use:  # loop to take lines from input file
            process_line(line, counts)
        process_file(counts, output_final)
    except FileNotFoundError:  # if input file isn't found proceed with exception
        print('Incorrect file name.')
        main()  # will restart the program


def add_word(work_words, dict_name):
    for word in work_words:  # loop to go through each word in parameter
        if word not in dict_name:  # if word doesn't exist already add to dictionary
            dict_name[word] = 1
        else:                      # otherwise add it into the dictionary
            dict_name[word] += 1


def process_line(work_line, dict_name):
    work_line = work_line.rstrip()  # removes extra spacing after a string
    work_line = work_line.translate(work_line.maketrans('', '', string.punctuation))  # deletes punctuation in work_line
    work_line = work_line.lower()  # Makes everything lower case
    words = work_line.split()   # split the words individual single word strings
    add_word(words, dict_name)


def process_file(dict_name, output_name):
    work_tuple = list(dict_name.items())  # take the key and value from dict_name to make a tuple
    work_tuple.sort(key=lambda x: x[1], reverse=True)  # sort by the value in 1st spot in reverse order
    length = len(dict_name)  # obtain the number of items in dictionary
    output_file = open(output_name, 'w')  # Creates a desired name file to write in
    output_file.write('The length of the Dictionary: {}\n'.format(length))
    output_file.write('Word              Count\n')
    output_file.write('-----------------------\n')
    for value in work_tuple:  # for each entry in the tuple
        output_file.write('{word:19}{count}\n'.format(word=value[0], count=value[1]))  # print the word and count with a gap of 19 spaces


main()  # run the main function
