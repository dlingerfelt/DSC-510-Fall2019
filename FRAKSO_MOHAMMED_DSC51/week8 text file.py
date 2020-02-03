'''
File: txt.py
Name: Mohammed A. Frakso
Date: 02/02/2020
Course: DSC_510 - Introduction to Programming
Desc: This program will  work with a text file to perform the following actions:
Open the file and process each line.
Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
Nicely print the output, in this case from high to low frequency using string formatting.
Achieve each major goal with a function (one function, one action), so the program will have 4 functions.
'''

import string

# Create add_word
def add_word (word, w_count_dict):
    if word not in w_count_dict:
        w_count_dict[word] = 1
    else:
        w_count_dict[word] = w_count_dict[word] +1

# Create process_line function in order to strip off various characters, split out the word

def process_line (line, w_count_dict):
    line = line.translate(str.maketrans('', '', string.punctuation))

    line = line.lower()  #  lines transformation, split  the words
    words = line.split()
    for word in words:
        add_word(word, w_count_dict)

#Pretty_print function for strings formatting

def pretty_print (w_count_dict):
  print("\nDictionary Length is : {0}".format(len(w_count_dict)))
  print("Word\t\t\tCount")
  print("---------------")
#Print in order the most occurrences first then least.
  for key in sorted(w_count_dict, key=w_count_dict.__getitem__, reverse=True):
      print("{}\t{}".format(key, w_count_dict[key]))

#define main() function
def main():
  try:
    w_count_dict = {}
    gba_file = open('C:\\Users\\ss\\Desktop\\Gettysburg.txt', 'r')
    for line in gba_file.readlines():
        process_line(line, w_count_dict)
    pretty_print(w_count_dict)
    gba_file.close()
  except:
    print("Error occurred while opening file. Please try again!")
  exit()
if __name__ == '__main__':
    main()