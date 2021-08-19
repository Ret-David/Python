# David Martinez

file = open('hello.txt', 'a')           # open file hello.txt in append mode
file.write('\nThis is new content I just appended.')    # append new content
file.close()                            # close file hello.txt

new_file = open('world.txt', 'w')       # open file world.txt in (over)write mode
new_file.write('This is new file')      # write new content
new_file.close()                        # close file world.txt

file = open('hello.txt')                # open file hello.txt
content = file.read()                   # read contents of file to variable
file.close()                            # close file hello.txt
print(content)                          # print contents to screen
