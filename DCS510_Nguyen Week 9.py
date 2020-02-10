import os
'''
 File: DSC510-Week 9 Nguyen.py
 Name: Chau Nguyen
 Date: 2/9/2020
 Course: DSC_510 Intro to Programming
 Description: Goals for this week assignment were to read file and write file into your directories and to continue
              apply string formatting. 
 '''
def process_line(line, line_dictionary):
    line = line.split() #split lines in file
    for word in line:
        word = word.strip (',--:.') #remove unwanted characters
        if word != '': #If string not empty
            add_word(word,line_dictionary)
def add_word(word, line_dictionary):
        if word in line_dictionary:
            line_dictionary[word] +=1
        else:
            line_dictionary[word] = 1
def Pretty_print(line_dict):
    sort_list = list()
    print("Lenght of the dictionary: ",(len(line_dict)))
    print('Word      Count')
    print('------------------------')
    for key in sorted(line_dict, key=line_dict.__getitem__, reverse=True):
       print("{}\t\t{}".format(key, line_dict[key]))
def process_file(line_dict, user_input):
    with open('{}.txt'.format(user_input),'w') as user_new:
        length = len(line_dict)
        user_new.write("Length of Dictionary \t {}".format(len(line_dict)))
        user_new.write('\nWord \t\t  Count')
        for key in sorted(line_dict, key=line_dict.__getitem__, reverse=True):
            user_new.write("\n{}\t\t\t {}".format(key, line_dict[key]))
def main():
    gba_file= open('gettysburg.txt','r')
    line_dict = {} #line_dict = line_dictionary
    user_input = input('Name your new file: ')
    for line in gba_file:
        process_line(line,line_dict) #call function
    process_file(line_dict,user_input)
    #Pretty_print(line_dict) #Formate line dictionary
if __name__ == '__main__':
    main()








