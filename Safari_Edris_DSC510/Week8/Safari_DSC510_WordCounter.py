# File : Safari_DSC510_WordCounter.py
# Name:Edris Safari
# Date:10/17/2019
# Course: DSC510 - Introduction To Programming
# Desc:
# This program will populate a list of temperatures from user input.
# This program will display the number of temperatures entered by user,
# This program displays the maximum temperature and minimum temperature from the list entered by the user.
# Usage: Provide input when prompted.

# Some global variables
import string

try:
    fhand = open(".\gettysburg.txt")
except:
    print("File not found")
    exit()

filecontent = dict()

for line in fhand:
    # strip whitespace from the right side
    line = line.rstrip()
    # remove all punctuations in this list '!"# $%&\'()* +,-./:; < = >?@[\\] ^_ `{ |} ~'
    line = line.translate(line.maketrans('', '', string.punctuation))
    # convert all characters to lower case
    line = line.lower()
    # Split the line to words separated by blank characters
    words = line.split()
    # Add each word in the line(stored in 'words') and increment its count
    for word in words:
        # add to dictionary with count value of 1 if word does not exist in dictionary
        # otherwise, get the current count and increment by one.
        filecontent[word] = filecontent.get(word, 0) + 1

print(filecontent)

lst = list()
for key, val in list(filecontent.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    print(val, key)