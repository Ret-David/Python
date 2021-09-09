# David Martinez

# Based on your pseudo code you wrote from the previous module, post your output
#     screen and a complete Python program " including your pseudocode as comment
#     blocks" that finds and prints the first sequence of 3 elements whose sum is
#     5 then exits.
# Feel free to use the following list for testing.
#     inputList = [1, -2, 3, 3, -1, -2, 7, 0, 2]
#     the correct triplet = 3, 3, -1

inputList = [1, -2, 3, 3, -1, -2, 7, 0, 2]

# Establish index variables
# Read and sum() the first index and following two index sequence positions
# Use a while loop statement
#     if the sum() = 5, then print a message, and end the loop
#     if the sum() != 5, then move to the next index and repeat the loop
# Print the sequence of elements whose sum is 5  (( Missing from last week. ))

x = 0       # set variable to 1st index
y = 3       # set variable to 4th index, so it will stop at the 3rd

while sum(inputList[x:y]) != 5:
        x = x + 1
        y = y + 1

else:
    print("Sum of", inputList[x:y], "equals 5.")
