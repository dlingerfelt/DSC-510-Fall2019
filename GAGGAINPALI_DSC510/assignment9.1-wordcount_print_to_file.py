# File : assignment9.1-wordcount_print_to_file.py
# Name : Bhargava Gaggainpali
# Date : FEB-9-2020
# Course : Introduction to Programming - python
# Assignment :
# -Last week we got a taste of working with files. This week we’ll really dive into files by opening and closing files properly.
# -For this week we will modify our Gettysburg processing program from week 8 in order to generate a text file from the output rather than printing to the screen. Your program should have a new function called process_file which prints to the file (this method should almost be the same as the pretty_print function from last week. Keep in mind that we have print statements in main as well. Your program must modify the print statements from main as well.
# -Your program must have a header. Use the programming style guide for guidance.
# -Create a new function called process_fie. This function will perform the same operations as pretty_print from week 8 however it will print to a file instead of to the screen.
# -Modify your main method to print the length of the dictionary to the file as opposed to the screen.
# -This will require that you open the file twice. Once in main and once in process_file.
# -Prompt the user for the filename they wish to use to generate the report.
# -Use the filename specified by the user to write the file.
# -This will require you to pass the file as an additional parameter to your new process_file function
# Desc : Program to input the file and count the words and the occurence of each word and print to file.
# Usage :
# -Program to input the file and count the words and the occurence of each word and print to file.

import string

# Create add_word function to count number of words.
def add_word (words, wordcount):
    if words not in wordcount: wordcount[words] = 1
    else: wordcount[words] = wordcount[words] +1

# Create process_line function to strip off various characters and split words in line
def process_line (eachline, wordcount):
    eachline = eachline.translate(str.maketrans('', '', string.punctuation))
    eachlinewords = eachline.split()
    for word in eachlinewords:
        add_word(word, wordcount)
#create process_file function to print the output to the file
def process_file (wordcount,print_to_file):
    with open("{}.txt".format(print_to_file),'w') as new_file:
        # Opens user input file in write mode
        new_file.write("\nLength of Dictionary is : {0}\n".format(len(wordcount)))
        new_file.write("\nWord\t\tCount")
        new_file.write("\n--------------------")
        for key in sorted(wordcount, key=wordcount.__getitem__, reverse=True):
            new_file.write("\n{}\t{}".format(key.ljust(10,' '), wordcount[key]))
    new_file.close()
#main() function
def main():
    wordcount = {}
    file = open('gettysburg.txt', 'r')
    print("\nWelcome to the 'WordCount_print_to_file Program'..!!")
    print_to_file = input('\nPlease Enter the Output File to be created and print work count: ')
    for line in file.readlines():
	    process_line(line, wordcount)
    process_file(wordcount,print_to_file)
    file.close()
    print("\nFile with a name '",print_to_file,"' created and the Word-Count is printed in the file Successfully.")
    print("Thank you for using 'WordCount_print_to_file Program'.")

if __name__ == '__main__':
    main()
