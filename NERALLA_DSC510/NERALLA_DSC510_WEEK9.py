'''
File: NERALLA_DSC510_WEEK9.py
Name: Ravindra Neralla
Course:DSC510-T303
Date:02/07/2020
Description: This program will perform the below list of items.
        It will process this .txt file: Gettysburg.txt.
		Calculate the total words, and output the number of occurrences of each word in the file.
        Open the file and process each line.
        Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
        We want to achieve each major goal with a function (one function, one action). We can find four functions that need to be created.
		add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
		Process_line: There is some work to be done to process the line: strip off various characters, split out the words, and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No return value.
		Process_file: Write the output into a separate file with user entered name
		main: We will use a main function as the main program. As usual, it will open the file and call process_line on each line. When finished, it will call pretty_print to print the dictionary.
'''
import string
def add_word (words, dictionary):
    #Function to add words and count
    for word in words:
        if word not in dictionary:
            # for the first time set the count variable to 1, i.e. when the word does not exist
            dictionary[word] = 1
        else:
            # when the word is present, increment the count by 1
            dictionary[word] = dictionary[word] + 1

def process_line (line, dictionary):
    #Function to remove special characters and split the words
    # below line removes all punctuation by changing to blank
    line = line.translate(str.maketrans('','', string.punctuation)) #removes all punctuation by changing to None
    line = line.lower()
    words = line.split()
    add_word(words,dictionary)
#Function to write output into a separate file
def process_file (dictionary,input_file):
    sort_list = list()
    with open("{}.txt".format(input_file),'w') as wf:
        # Opens user input file in write mode
        wf.write("Count \t  Word \n------    -------\n")
        for key in sorted(dictionary, key=dictionary.__getitem__, reverse=True):
            wf.write("\n{}\t{}".format(key, dictionary[key]))

#Define main function, starting point of program, opens file and creates empty dictionary
def main ():
    getty_file = open('C:\\Users\\Ravi\\PycharmProjects\\NERALLA_DSC510\\gettysburg.txt', 'r')
    counts = dict()
    input_file = input('Please Enter Output File Name: ')
    # Process each line in the file by calling process_line function
    for line in getty_file:
        process_line(line, counts)
    process_file(counts,input_file)

if __name__ == '__main__':
    main()

