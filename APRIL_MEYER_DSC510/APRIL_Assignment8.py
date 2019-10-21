#File: Assignment 8
#Name: April Meyer
#Assignment 8
#Date: 10.16.2019
"""A program which performs three essential operations.
It will process a .txt file: Gettysburg.txt.
It will calculate the total words, and output the number of occurrences of each word in the file.
"""
import string
def add_word (words, dictionary): #adds the words to the dictionary and get the word counts
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1 #if the word has not occurred yet set count to 1
        else:
            dictionary[word] += 1 #if it has occurred increment by one

def process_line (line, dictionary): #strip off various characters, split out the words, and cleans the file
    line = line.translate(str.maketrans('','', string.punctuation)) #removes all punctuation by changing to None
    line = line.lower() #converts to lower case
    words = line.split() #splits the words out
    add_word(words,dictionary)

def pretty_print (dictionary): #prints the results in a cleaner way
    print("Length of the dictionary: ", len(dictionary))
    print("Word \t \t \t \t Count \n--------------------------")
    for key, value in dictionary.items():
        print("{:15} \t {:4} \t".format(key, value))

def main (): #main function that opens the file and creates an empty dictionary
    gba_file = open('gettysburg.txt','r')
    counts = dict()
    for line in gba_file: #for each line in the file run process_line method
        process_line(line, counts)
    pretty_print(counts)

main()




