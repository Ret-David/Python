# David Martinez
# Edit the program to replace any negative numbers in the list
#  with positive ones. Expected result: [8,20,10,55,777]

# Establish original variable with list values
original = [8,20,-10,55,-777]

# Step through each value in original list and print
for i in range(len(original)):
    print(original[i])

# Establish new variable with and empty list for new values
new_original = []     # Took me about 5hrs to realize it belonged here and not nested.

# Step through each value in original list and turn to an absolute value
# Append the new value to the new list
for i in range(len(original)):
    x = abs(original[i])
    new_original.append(x)

# Print the new values from the new list
print("New list is", new_original)

# Insert a 0 before index 3 of the new list
new_original.insert(3, 0)
print("New new list is", new_original)