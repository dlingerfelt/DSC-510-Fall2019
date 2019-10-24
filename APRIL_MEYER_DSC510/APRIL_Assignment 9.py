#File: Assignment 9
#Name: April Meyer
#Assignment 9
#Date: 10.24.2019
"""A program which performs three essential operations.
It will process a .txt file: Gettysburg.txt.
It will calculate the total words, and output the number of occurrences of each word in the file to a new file.
The name of the file will be from the user.
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

def process_file (dictionary,user_file): #prints the results in a cleaner way
    sort_list = list()
    with open("{}.txt".format(user_file),'w') as wf: #opens file as write and names it what the user input
        # wf.write("Length of the dictionary: {} \n".format(len(dictionary))) #writes the length of dictionary
        wf.write("Count \t Word \n-------------------\n") #header
        for key, value in list(dictionary.items()): #changes to list to be able to sort
            sort_list.append((value, key))
            sort_list.sort(reverse=True)
        for key, value in sort_list[:]: #writes each item from list to file
            wf.write("{:4} \t {:10} \t \n".format(key, value))
            # print(key, value)

def main (): #main function that opens the file and creates an empty dictionary
    gba_file = open('gettysburg.txt','r')
    counts = dict()
    user_file = input('Please enter a a name for your report: ')
    for line in gba_file: #for each line in the file run process_line method
        process_line(line, counts)
    process_file(counts,user_file)
    with open("{}.txt".format(user_file),'r+') as wf: #opens the file as read/write and adds count of dictionary at the beginning
        lines = wf.readlines()
        wf.seek(0)
        wf.write("Length of the dictionary: {} \n \n".format(len(counts)))
        wf.writelines(lines)

main()
