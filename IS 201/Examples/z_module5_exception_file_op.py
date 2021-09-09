#
# - Exception Handling
#

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


while True:
    try:
        inChar = input("Please enter \"X\" or \"O\": ").upper()
        if(inChar == 'X' or inChar == 'O'):
            print(f"Your choice is '{inChar}' and let's play!")
            break
        else:
            print("Oops!  That was no valid input.  Try again with \"X\" or \"O\"")
    except:
        print("ValueError: That was no valid input.  Try again with \"X\" or \"O\"")

bGo = True
i = 0
while bGo and i < 3:
    try:
        x = (10/int(input("Enter a denominator : ")))
    except ZeroDivisionError:
        print("Zero Division Error is raised!")
        bGo = False
    except ValueError:
        print("Enter an integer!")
        bGo = False
    i = i + 1
# unexpected operation was executed
# cannot trust x
if bGo == True:
    print(x)
else:
    x = -999
    print("not so trustful value!", x)

L = ['3', '8', '2', '10', '-9', '2', "", 'c']
for i in range(10):
    if(int(L[i])):
        print(L[i])

L = ['3', '8', '2', '10', '-9', '2', "", 'c']
for i in range(10):
    try:
        if(int(L[i])):
            print(L[i])
    # except ValueError:
    #     print("Unexpected input value!")
    #     continue
    # except IndexError:
    #     print("Out of bound!")
    #     continue
    except (ValueError, IndexError):
        print("Fix your darn program!")
        continue


a = [0,1,2]
try:
    b = True
    if b == False:
        if(a[0] == 0):
            raise Exception("Oh My Exceptoin: Divided-by-zero??")
        a[2] = a[1]/a[0]
    else:
        print('fourth element is %d ' % a[3])
except IndexError as error:
    # print("Out of Bound!")
    print("Exception: " + str(error))


L = [2, 3, 4, 2, -3]
for i in range(len(L)):
    print(L[i])
    assert(L[i] > 0), "Cannot have a negative value!" # Assertion error when false

#
# - File operation
#
# 
# --- printing the strings obtained from a user input and write to a file
#
try:
    f = open('test.txt', 'r')
    contents = f.read()
    print(contents)

finally: #This type of construct makes sure the file is closed even if an exception occurs.
    f.close() # <<-- to ensure the file is closed after finished reading.

try:
    f = open('test1.txt', 'w')
    print('What do you want to say?')
    str = input()
    f.write(str)

finally: #This type of construct makes sure the file is closed even if an exception occurs.
    f.close() # <<-- to ensure the file is closed after finished writing.

#
# -- appending to the EOF
#
try:
    f = open('test1.txt', 'a')
    print('What do you want to say again?')
    str = input()
    f.write(str)
    
finally: #This type of construct makes sure the file is closed even if an exception occurs.
    f.close() # <<-- to ensure the file is closed after finished writing.


# 
# -- traditionally, we have been using open -- close a file for any operation
#
f = open('test.txt', 'r')
contents = f.read()
print (contents)
f.close()

#
# -- new way of opening a file with the context manager
#
with open('test.txt', 'r') as f:
    contents = f.read()
    print (contents)
    # no need to close with the context manager!!

try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError:# as fnf_error:
    print("ERROR:", end="")
    # print(fnf_error)


with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

line_number = 1
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(str(line_number) + ") " +line)
            line_number = line_number + 1


#
# for a demo purpose, I'll just simply open for reading
f = open('test.txt', 'r')
f.readlines() # read a line at a time
['This is the first line\n', 'This is the second line\n', 'This is the third line\n', 'This is the forth line\n', '\n']
f.read() # read a whole contents

# file pointer, f.tell(), f.seek(0) // rewind
f.tell()
99
f.seek(0) # back to 0th character, the beginning of the file
0
f.close


''' FILE OPERATION '''
import os

totalsize = 0
num_files = 0

for filename in os.listdir('C:\\Windows'):
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\Windows', filename))
    num_files = num_files + 1
    print(filename)

print(totalsize, "bytes")
print("number of files: ", num_files)
