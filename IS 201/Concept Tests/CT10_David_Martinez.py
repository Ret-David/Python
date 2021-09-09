# David Martinez

# Based on your pseudo code you wrote from the previous module,
#   post your output screen and a complete Python program "including
#   your pseudocode as comment blocks" that returns I-th largest value
#   in a list. For example, with the input list [3, 2, 8, 10, 5, 23]
#   and I = 4, the program prints the value 5 as it is 4 th largest value.

# ========== My Pseudo Code ==========
# >> 5 is in index 4 position but is the 3rd largest value

input_list = [3, 2, 8, 10, 5, 23]  # variable = input list values
i = 4                              # variable = I-th largest value
# output = sorted output for I-th largest value
output = sorted(input_list)[i-1]  # grab value in 4th position (index 3) 
print(f'{i}th largest value is {output}.')  # print I-th value
