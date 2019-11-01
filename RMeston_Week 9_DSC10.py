# File: Week 9 Assignment
# Name: Ryan Meston
# Date: 20191027
# Course: DSC510
# Desc: Week 9 Assignment
# Usage: open gettysburg.txt file, create process_file. Print length of dictionary to file and not screen.

def add_word (words, dictionary): # pg. 107 python for everybody, dictionary as a set of counters example.
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dictionary[word] +1

import string

def process_line (line, dictionary): # pg. 111, 112 using examples from book.
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    add_word(words, dictionary)

def process_file (dictionary, fname): #slides and chapter 7
    with open(fname, 'w') as fileHandle:
        fileHandle.write("Dictionary length is: " + str(len(dictionary)))
        for key, value in dictionary.items():
            print(key, value)

def main():
    gba_file = open('gettysburg.txt', 'r')
    word_count = {}
    fname = input('Enter the file name: ')
    for line in gba_file:
       process_line(line, word_count)
    process_file(word_count, fname)
    with open(fname, 'r+') as fileHandle: #special read and write mode
        data = fileHandle.read()
    print(data)

main()
