#!/usr/bin/env python3

# File: Assignment_8_1.py
# Name: Jubyung Ha
# Date: 01/20/2020
# Course: DSC510-T303 Introduction to Programming (2203-1)

# Desc: We will create a program which performs three essential operations.
# It will process this .txt file: Gettysburg.txt. (Click the link to download the text file).
# Calculate the total words, and output the number of occurrences of each word in the file.
#
# Open the file and process each line.
# Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
# Nicely print the output, in this case from high to low frequency.
# You should use string formatting for this. (See discussion 8.3).
# We want to achieve each major goal with a function (one function, one action).
# We can find four functions that need to be created.
#
# add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
#
# Process_line: There is some work to be done to process the line:
# strip off various characters, split out the words, and so on.
# Parameters are a line and the dictionary.
# It calls the function add word with each processed word. No return value.
#
# Pretty_print: Because formatted printing can be messy and often particular to each situation
# (meaning that we might need to modify it later),
# we separated out the printing function.
# The parameter is a dictionary. No return value.
#
# main: We will use a main function as the main program.
# As usual, it will open the file and call process_line on each line.
# When finished, it will call pretty_print to print the dictionary.
#
# In the main function, you will need to open the file.
# We will cover more regarding opening of files next week, but
# I wanted to provide you with the block of code you will utilize to open the file, see below.

# Usage: Call main function which will call Process_line function and Pretty_print.

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
    line = line.translate(str.maketrans('','', string.punctuation))  # Remove all punctuation
    words = line.split()  # Split word from the line
    add_word(words, summary)  # Add word to dictionary


def Pretty_print(summary):
    """Print the total count of words and the count for each word.
    Args:
        The parameter is a dictionary
    Returns:
         No return value.
    """
    print('Length of the dictionary: {}'.format(len(summary)))
    print('Word', '              ', 'Count')
    print('-------------------------')
    # Sort the dictionary by value
    for word, count in sorted(summary.items(), key=lambda kv: kv[1], reverse=True):
        print("{:17} {:5}".format(word, count))


def main():
    """it will open the file and call process_line on each line.
     When finished, it will call pretty_print to print the dictionary
    """
    summary = dict()
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        Process_line(line, summary)
    Pretty_print(summary)


if __name__ == '__main__':
    main()
