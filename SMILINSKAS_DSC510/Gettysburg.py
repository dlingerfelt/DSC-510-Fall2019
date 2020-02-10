# File: 8.1 Assignment.py
# Name: Vilius Smilinskas
# Date: 2/5/2020
# Course: DSC510: Introduction to Programming
# Desc: Program will read a file dissect its words and display its contents in a dictionary
# Usage: Run the program and the results will be displayed.

import string  # importing string for string.punctuation which contains different punctuation to clear text from formating
counts = dict()  # variable set as a empty dictionary


def main():
    gba_file = open('gettysburg.txt', 'r')   # opens gettysburg.txt
    for line in gba_file:  # loop to take lines from gettysburg.txt
        process_line(line, counts)
    pretty_print(counts)


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


def pretty_print(dict_name):
    work_tuple = list(dict_name.items())  # take the key and value from dict_name to make a tuple
    work_tuple.sort(key=lambda x: x[1], reverse=True)  # sort by the value in 1st spot in reverse order
    length = len(dict_name)  # obtain the number of items in dictionary
    print('The length of the Dictionary: {}'.format(length))
    print('Word              Count')
    print('-----------------------')
    for value in work_tuple:  # for each entry in the tuple
        print('{word:19}{count}'.format(word=value[0], count=value[1]))  # print the word and count with a gap of 19 spaces


main()  # run the main function
