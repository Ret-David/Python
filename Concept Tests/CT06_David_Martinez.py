# David Martinez

# Write a pseudo code to design a program that returns the # of occurrences of 
#     unique values but sorted from the list. For example, with the input list
#     [1, 2, -2, 1, 0, 2, 4, 0], the program should provide the output as follows:
#     unique value (# of occurrences)
#      -2(1) 
#       0(2)
#       1(2)
#       2(2)
#       4(1)

input_list = [1, 2, -2, 1, 0, 2, 4, 0]
output_dict = {}                             # create an empty output dictionary

for i in set(input_list):                    # for step through input_list, use set for dupes
    if input_list.count(i) >= 1:             # count through values and identify dupes
        output_dict[i] = input_list.count(i) # append key and count value to output_dict (revised)

for key in sorted(output_dict.items()):      # for step through keys of sorted dictionary
    print(f'{key[0]}({key[1]})')             # print format for screen output
