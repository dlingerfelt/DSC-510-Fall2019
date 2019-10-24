# File: Week 8 Assignment
# Name: Ryan Meston
# Date: 20191020
# Course: DSC510
# Desc: Week 8 Assignment
# Usage: open gettysburg.txt file and process each line, add each word to dictionary, pretty print output.

def add_word (word, dictionary): # pg. 107 python for everybody, dictionary as a set of counters example.
    for words in word:
        if words not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dictionary[word] +1

import string
def process_line (line, dictionary): # pg. 111, 112 using examples from book.
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in add_word(word, dictionary):
            add_word(word, dictionary)[word] = 1
        else:
            add_word(word, dictionary)[word] += 1

def pretty_print (dictionary): #assignment 8.3 video and reading examples
    print("Dictionary length is: " + str(len(dictionary)))
    print("Word count")
    for key, value in dictionary.items():
        print(key, value)

def main():
    gba_file = open('gettysburg.txt', 'r')
    word_count = {}
    for line in gba_file:
       process_line(line, word_count)
    pretty_print(word_count)

