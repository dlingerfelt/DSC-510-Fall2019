# File: Assignment 9.1 - Jonathan Steen.py
# Name: Jonathan Steen
# Date: 2/7/2020
# Course: DSC510 - Introduction to Programing
# Desc: Program will open a file, calculate the total words,
# the total occurrences of each word and print to screen and file
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

def process_file(newFile, fileDictionary):

    total = 0
    for word in fileDictionary:
        total += 1

    output=open(newFile,'a')
    output.write('Length of the dictionary:\n\n' + str(len(fileDictionary)) + '\n')

    cols = ['\nWord', 'Count\n'] #colum headers

    output.write("{:>0}\t{:>15}".format(*cols))
    output.write('------------------------')
    for key, value in sorted(fileDictionary.items(), key=lambda kv: kv[1], reverse=True): #sort by frequency
        output.write("\n{:15}\t{:6}".format(key, fileDictionary[key]))

    print("\n\nText file has been created.")

    output.close()

def main():
    try:
        try:
            gba_file = open('gettysburg.txt', 'r')

            fileDictionary = dict()

            try:

                fileName = input('Please input a filename. \n')
                fileName = fileName.lower()

                fileExtentsion = fileName[-4:]
                correctExtentsion = '.txt'

                if fileExtentsion not in correctExtentsion:
                    raise Exception()

                if fileName[+4] in {''} == True:
                    raise Exception()

                newFile = open(fileName, 'w')

                for line in gba_file:
                    processLine(line, fileDictionary)

                prettyPrint(fileDictionary)
                process_file(fileName, fileDictionary)
            except:
                print('Invalid filename. Please enter "filename".txt next time')
        except:
            print('Error opening file.')

    except:
        print('Something went wrong.')
if __name__ == '__main__': main()
