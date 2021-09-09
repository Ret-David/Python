# David Martinez

# Write a Python program that takes a text file as input and returns the number of words
#     of a given text file.

with open('PE05_David_Martinez_1.txt') as file_object:       # open file hello.txt
    my_string = file_object.read()                           # read contents of file to variable
    split_words = my_string.split()                          # split string into a word list
    print("No. of words in the string : ", len(split_words)) # out the word count to the screen

file_object.close()                                          # close file hello.txt
