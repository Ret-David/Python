# David Martinez

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 

# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

myDict = dict()             # establish an empty dictionary variable

for key in range(1,6):      # for loop through range 5 times
    myDict[key] = key ** 2  # store key with square value in the dictionary

print(myDict)               # Print myDict
