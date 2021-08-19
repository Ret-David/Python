# David Martinez

filename = 'hello.txt'

with open(filename) as file_object:     # open file hello.txt
    lines = file_object.readlines()     # read lines into variable

for line in lines:                      # step through each line in lines
    print(line.rstrip())                # strip extra after last visible character

file_object.close()                     # close file hello.txt
