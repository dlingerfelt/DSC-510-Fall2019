#!/usr/bin/env python3

# File: Assignment_9_1.py
# Name: Jubyung Ha
# Date: 02/09/2020
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc: Last week we got a taste of working with files.
# This week we’ll really dive into files by opening and closing files properly.
#
# For this week we will modify our Gettysburg processing program from week 8
# in order to generate a text file from the output rather than printing to the screen.
# Your program should have a new function called process_file which prints to the file
# (this method should almost be the same as the pretty_print function from last week.)
# Keep in mind that we have print statements in main as well.
# Your program must modify the print statements from main as well.
#
# Your program must have a header. Use the programming style guide for guidance.
# Create a new function called process_fie.
# This function will perform the same operations as pretty_print from week 8
# however it will print to a file instead of to the screen.
# Modify your main method to print the length of the dictionary to the file as opposed to the screen.
# This will require that you open the file twice. Once in main and once in process_file.
# Prompt the user for the filename they wish to use to generate the report.
# Use the filename specified by the user to write the file.
# This will require you to pass the file as an additional parameter to your new process_file function.
#
# Your program must have a header. Use the programming style guide for guidance.
# Create a new function called process_fie.
# This function will perform the same operations as pretty_print from week 8,
# however it will print to a file instead of to the screen.
# Modify your main method to print the length of the dictionary to the file as opposed to the screen.
# This will require that you open the file twice. Once in main and once in process_file.
# Prompt the user for the filename they wish to use to generate the report.
# Use the filename specified by the user to write the file.
# This will require you to pass the file as an additional parameter to your new process_file function.

# Usage:


import string


def add_word(words, summary):
    """Add each word to the dictionary. If exist, increment the count by 1.

    Args:
        Parameters are the word and a dictionary.
    Returns:
        No return value.
    """
    for word in words:
        if word not in summary:
            summary[word] = 1  # If not a word exists, add the word and set value as 1
        else:
            summary[word] += 1  # If a word exists, just increase value by 1


def Process_line(line, summary):
    """Strip off various characters, split out the words, and so on
    Args:
        Parameters are a line and the dictionary.
    Returns:
        No return value.
    """
    line = line.lower()  # lower all words in the line
    line = line.translate(str.maketrans('', '', string.punctuation))  # Remove all punctuation
    words = line.split()  # Split word from the line
    add_word(words, summary)  # Add word to dictionary


def Pretty_print(summary):
    """Print the total count of words and the count for each word.
    Args:
        The parameter is a dictionary
    Returns:
         No return value.
    """
    print('Word', '              ', 'Count')
    print('-------------------------')
    # Sort the dictionary by value
    for word, count in sorted(summary.items(), key=lambda kv: kv[1], reverse=True):
        print("{:17} {:5}".format(word, count))


def process_file(summary, txt_file):
    """Print to the file
    Args:
        summary: dictionary
        txt_file: file object
    :return:
        None
    """
    txt_file.write('Word', '              ', 'Count')
    txt_file.write('-------------------------')
    # Sort the dictionary by value
    for word, count in sorted(summary.items(), key=lambda kv: kv[1], reverse=True):
        txt_file.write("{:17} {:5}".format(word, count))

def main():
    """it will open the file and call process_line on each line.
     When finished, it will call pretty_print to print the dictionary
    """
    summary = dict()
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        Process_line(line, summary)
    file_name = input('Please enter file name: ')
    file_path = "{}.txt".format(file_name)

    txt_file = open(file_path, 'w')
    txt_file.write('Length of the dictionary: {}'.format(len(summary)))

    process_file(summary, txt_file)


if __name__ == '__main__':
    main()
