# David Martinez

# Based on your pseudo code you wrote from the previous module, post your output screen
#     and a complete Python program "including your pseudocode as comment blocks" that
#     removes the duplicate numbers in a list and prints the unique numbers only. For 
#     example, with the input list [1, 2, -2, 1, 0, 2, 4, 0], the program prints
#     1, 2, -2, 0, 4.

input_list = [1, 2, -2, 1, 0, 2, 4, 0] # start with provided list

output_list = []                       # create an empty output_list

for i in input_list:                   # for step through input_list (revised)
    if i not in output_list:           # check if value is already in the output_list (forgot line)
        output_list.append(i)          # append to the output_list if it doesn't exist

print(*output_list, sep = ", ")        # print the list values for screen output (revised)

# ======= My Original Pseudo Code =======
# start with provided list
# create an empty output_list

# if step through input_list
#     and append to the output_list if it doesn't exist

# print format by stepping through the list values for screen output
