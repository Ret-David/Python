# David Martinez

# Write a Python program to match key values in two dictionaries. 

# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

sample_dictionary = {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}

x = sample_dictionary[0]                   # set index 0 as dict{x}
y = sample_dictionary[1]                   # set index 1 as dict{y}

present_in_both = dict()                   # make an empty dictionary for output
for key in x:                              # for loop through dict{x}
    if (key in y and x[key] == y[key]):    # compare dictionary key/value
        present_in_both[key] = x[key]      # store common key/value found between dictionaries

for key, value in present_in_both.items(): # use dict.items to cycle through key/value
    print("{}: {}".format(key, value) + " is present in both x and y")
                                           # use str.format to achieve Expected Output
