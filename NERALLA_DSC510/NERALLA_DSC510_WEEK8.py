'''
File: NERALLA_DSC510_WEEK8.py
Name: Ravindra Neralla
Course:DSC510-T303
Date:02/01/2020
Description: This program will perform the below list of items.
        It will process this .txt file: Gettysburg.txt. 
		Calculate the total words, and output the number of occurrences of each word in the file.
        Open the file and process each line.
        Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
        We want to achieve each major goal with a function (one function, one action). We can find four functions that need to be created.
		add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
		Process_line: There is some work to be done to process the line: strip off various characters, split out the words, and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No return value.
		Pretty_print: Because formatted printing can be messy and often particular to each situation (meaning that we might need to modify it later), we separated out the printing function. The parameter is a dictionary. No return value.
		main: We will use a main function as the main program. As usual, it will open the file and call process_line on each line. When finished, it will call pretty_print to print the dictionary.
'''
import string

# Create add_word function, with parameters are word and word_count_dict
def add_word (word, word_count_dict):
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] = word_count_dict[word] +1

# Create process_line function to remove special characters and covert to lower case

def process_line (line, word_count_dict):
	#below line removes special characters

    line = line.translate(str.maketrans('', '', string.punctuation))
	#below lines removes converts to lower case 
    line = line.lower()
    words = line.split()
    for word in words:
        add_word(word, word_count_dict)
#create pretty_print function to format the out in a desired format
def pretty_print (word_count_dict): 
  print("\nDictionary Length is : {0}".format(len(word_count_dict)))
  print("Word\t\tCount")
  print("-------   --------")
# We need to print the most occurrences first then least, in order
  for key in sorted(word_count_dict, key=word_count_dict.__getitem__, reverse=True):
      print("{}\t{}".format(key, word_count_dict[key]))

#define main() function, from where program execution starts
def main():
  try:
    word_count_dict = {}
    file = open('C:\\Users\\Ravi\\PycharmProjects\\NERALLA_DSC510\\gettysburg.txt', 'r')
    for line in file.readlines():
	    process_line(line, word_count_dict)
    pretty_print(word_count_dict)
    file.close()
  except:
    print("Error occured while opening file")
  exit()
if __name__ == '__main__':
    main()	
