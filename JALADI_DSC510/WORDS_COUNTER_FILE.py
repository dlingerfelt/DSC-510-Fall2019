# File :    WORDS_COUNTER.py
# Name :    Pradeep Jaladi
# Date :    01/25/2020
# Course :  DSC-510 - Introduction to Programming
# Assignment :
#           Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name. Use the SIUE Style Guide as a reference.
#           We will create a program which performs three essential operations. It will process this .txt file: Gettysburg.txt. (Click the link to download the text file).  Calculate the total words, and output the number of occurrences of each word in the file.
#           Open the file and process each line.
#           Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
#           Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
#           add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
#           Process_line: There is some work to be done to process the line: strip off various characters, split out the words, and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No return value.
#           Pretty_print: Because formatted printing can be messy and often particular to each situation (meaning that we might need to modify it later), we separated out the printing function. The parameter is a dictionary. No return value.
#           main: We will use a main function as the main program. As usual, it will open the file and call process_line on each line. When finished, it will call pretty_print to print the dictionary.
# Desc :    Program to calculate the words count in a file and print the words count order by most first
import string
import os.path


def process_line(line, word_count_dict):
    # Need to remove the special characters in the line. otherwise, here, and here will be different
    trans_table = line.maketrans('', '', string.punctuation)
    line = line.translate(trans_table)

    # convert the line into lowercase, other wise Here and here will be different
    line = line.lower()

    # loop through each word
    for word in line.split():
        add_word(word_count_dict, word)


def add_word(word_count_dict, word):
    word_count_dict[word] = word_count_dict.get(word, 0) + 1


def process_file(word_count_dict, output_fname):
    with open(output_fname, 'a+') as file_handler:
        print("Word\t\t\tCount", file=file_handler)
        print("----------------------", file=file_handler)

        # dictionary sort is supported either key or value not both, so using lists
        sorted_list = list()
        for word, value in list(word_count_dict.items()):
            sorted_list.append((value, word))  # adding value as key and word as value

        sorted_list.sort(reverse=True)  # List first sorts the keys and then sorts the values

        for count, word in sorted_list:
            space_length = 16  # We are giving len(word) = 4 + 3* 4 (tab) for key
            value = word.ljust(space_length)  # Padding the key to format and print
            print('{0}{1}'.format(value, count), file=file_handler)


def open_output_file():
    try:
        output_file_name: str = input('Enter the file name to write output : ')
        output_file_name = output_file_name.strip()  # striping whitespace characters
        if os.path.isfile(output_file_name):  # checking if file already exists and alerting the user
            print(
                'Already file exists with same name, if you wish to override press any key to continue, to abort press q')
            quit_checker = input()
            if quit_checker == 'q':  # abort the file is input is passed a q
                exit(0)

        return output_file_name
    except:
        print('Aborting the program due to user abort request')


def main():
    try:
        output_file_name = open_output_file()

        word_count_dict = dict()

        # Open the file in read mode only and the file will close automatically
        with open('gettysburg.txt', 'r') as file:
            # Process each line for the word count
            for line in file:
                process_line(line, word_count_dict)

        # Print the output
        with open(output_file_name, 'w+') as file_handler:
            print("Length of the dictionary : {0}".format(len(word_count_dict)), file=file_handler)

        process_file(word_count_dict, output_file_name)
    except:
        print("Something went wrong")

    exit()


if __name__ == '__main__':
    main()
