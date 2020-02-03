# File : assignment8.1-wordcount.py
# Name : Bhargava Gaggainpali
# Date : FEB-2-2020
# Course : Introduction to Programming - python
# Assignment :
# -We will create a program which performs three essential operations. It will process this .txt file: Gettysburg.txt. (Click the link to download the text file).  Calculate the total words, and output the number of occurrences of each word in the file.
# -Open the file and process each line.
# -Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
# -Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
# -We want to achieve each major goal with a function (one function, one action). We can find four functions that need to be created.
# -add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
# -Process_line: There is some work to be done to process the line: strip off various characters, split out the words, and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No return value.
# -Pretty_print: Because formatted printing can be messy and often particular to each situation (meaning that we might need to modify it later), we separated out the printing function. The parameter is a dictionary. No return value.
# -main: We will use a main function as the main program. As usual, it will open the file and call process_line on each line. When finished, it will call pretty_print to print the dictionary.
# -In the main function, you will need to open the file. We will cover more regarding opening of files next week but I wanted to provide you with the block of code you will utilize to open the file, see below.
# Desc : Program to input the file and count the words and the occurence of each word.
# Usage :
# -Program to input the file and count the words and the occurence of each word.

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
#create pretty_print function to print the output
def pretty_print (wordcount):
  print("\nLength of Dictionary is : {0}".format(len(wordcount)))
  print("Word\t\tCount")
  print("---------------------")
# print in the order of most occurrences to least occurrences
  for key in sorted(wordcount, key=wordcount.__getitem__, reverse=True):
      print("{}\t\t{}".format(key, wordcount[key]))

#main() function
def main():
    wordcount = {}
    file = open('gettysburg.txt', 'r')
    for line in file.readlines():
	    process_line(line, wordcount)
    pretty_print(wordcount)
    file.close()
if __name__ == '__main__':
    main()
