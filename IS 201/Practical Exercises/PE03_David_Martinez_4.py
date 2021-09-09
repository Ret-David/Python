# David Martinez

# Write a Python program to print all unique values in a dictionary. 

# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

sample = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
          {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

output = set()                  # use set() to show unique values
for dict in sample:             # for loop to cycle through the list of dictionaries
    for value in dict.values(): # for loop to cycle through the dictionaries values
        output.add(value)       # add the values to the output set

print(output)                   # print the output set
