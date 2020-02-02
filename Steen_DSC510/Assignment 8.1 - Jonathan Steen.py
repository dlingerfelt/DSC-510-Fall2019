# File: Assignment 8.1 - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 1/28/2020
# Course: DSC510 - Introduction to Programing
# Desc: Program will open a file, calculate the total words and output
# and calculate the total occurrences of each word.
# Usage:  The program will count total words and occurrences of each word.

import string

def processLine(line, fileDictionary): #function to process each line of file

        line = line.translate(line.maketrans('', '', string.punctuation)) #strip punctuation
        line = line.lower() #convert to lower
        words = line.split() #split out words

        addWord(words, fileDictionary) #call addWord function

def addWord(words, fileDictionary): #function to add words

    for word in words: #for statement to get the count
        if word in fileDictionary:
            fileDictionary[word] += 1
        else:
            fileDictionary[word] = 1

def prettyPrint(fileDictionary): #function to format and display output

    print('Length of the dictionary: ', len(fileDictionary))

    cols = ['Word', 'Count'] #colum headers

    print("{:>0}\t{:>15}".format(*cols))
    print('------------------------')
    for key, value in sorted(fileDictionary.items(), key=lambda kv: kv[1], reverse=True): #sort by frequency
        print("{:15}\t{:6}".format(key, fileDictionary[key]))

def main():
    gba_file = open('gettysburg.txt', 'r')

    fileDictionary = dict()

    for line in gba_file:
        processLine(line, fileDictionary)
    prettyPrint(fileDictionary)

if __name__ == '__main__': main()






