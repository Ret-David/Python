# David Martinez

# Write a Python script to concatenate following dictionaries to create a new one. 
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

myDict = {}         # Establich an empty dictionary
myDict.update(dic1) # Put contents of dic1 into myDict
myDict.update(dic2) # Put contents of dic2 into myDict
myDict.update(dic3) # Put contents of dic3 into myDict
print(myDict)       # Print contents of myDict
