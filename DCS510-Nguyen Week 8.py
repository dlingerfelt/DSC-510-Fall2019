'''
 File: DSC510-Week 5 Nguyen.py
 Name: Chau Nguyen
 Date: 2/2/2020
 Course: DSC_510 Intro to Programming
 Desc: This program helps implement dictionary functions and it's properties
 The program will open text file, read string, count words, and return word and number of repetition.
 '''
def process_line(line, line_dictionary):
    line = line.split() #split lines in file
    for word in line:
        word = word.strip (',-:.') #remove unwanted characters
        if word != '': #If string not empty
            add_word(word,line_dictionary)
def add_word(word, line_dictionary):
        if word in line_dictionary:
            line_dictionary[word] +=1
        else:
            line_dictionary[word] = 1
def Pretty_print(line_dict):
    print("Lenght of the dictionary: ",len(line_dict))
    print("Word              Count")
    print("------------------------")
    for key, value in line_dict.items():
        print("{:20s} {}".format(key,value))

def main():
    gba_file= open('gettysburg.txt','r')
    line_dict = {} #line_dict = line_dictionary
    for line in gba_file:
        process_line(line,line_dict) #call function
    Pretty_print(line_dict) #Formate line dictionary
if __name__ == '__main__':
    main()


