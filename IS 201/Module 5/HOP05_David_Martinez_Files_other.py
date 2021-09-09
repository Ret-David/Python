# David Martinez

with open('hello.txt') as file_object:  # open file hello.txt
    contents = file_object.read()       # read contents of file to variable
print(contents)                         # print variable 'contents' to screen
file_object.close()                     # close file hello.txt
