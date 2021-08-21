# David Martinez

# Write a pseudo code to design a program that finds the first sequence of 3 elements
#     whose sum is 5.
# You can assume that the list is already defined. For example, when
#     inputList = [1 -6, 4, 1, -2, 6, 0, 5, 0] is defined, your program will start
#     reading 1,-6,4, then -6,4,1, then 4, 1, -2 and so on.
# And the program stops when you read 1, -2, 6 since the sum of triplets is 5.

inputList = [1, -6, 4, 1, -2, 6, 0, 5, 0]

# Establish index variables
# Read and sum() the first index and following two index sequence positions
# Use a while loop statement
#     if the sum() = 5, then print a message, and end the loop
#     if the sum() != 5, then move to the next index and repeat the loop

x = 0       # set variable to 1st index
y = 3       # set variable to 4th index, so it will stop at the 3rd

while sum(inputList[x:y]) != 5:
        x = x + 1
        y = y + 1

else:
    print("Sum of", inputList[x:y], "equals 5.")
