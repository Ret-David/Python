# David Martinez

# Given a list of integers with duplicate elements in it. The task to generate
#     another list, which contains only the duplicate elements. In simple
#     words, the new list should contain the elements which appear more than
#     one.
# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]

list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
output_list = []

for i in set(list):                 # Use set() to elimate duplicates
    if list.count(i) > 1:           # Count() through and identify duplicates
        output_list.append(i)       # Append duplicates to output_list

print(output_list)                  # Print the output_list
