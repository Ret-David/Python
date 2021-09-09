# David Martinez

list1 = ['physics', 'chemestry', 1997, 2000]    # Add 4 value to list1
list2 = [1, 2, 3, 4, 5, 6, 7]                   # Add 7 value to list2

#accessing
print ("list1[0]: ", list1[0])                  # Print the value stored at position 0 in list1
print ("list2[1:5]: ", list2[1:5])              # Print a slice of positions 1 thru 5 in list2

#updating
print ("Value available at index 2 : ")         # Print string
print (list1[2])                                # Print the value stored at position 2 in list1
list1[2] = 2001                                 # Assign a new value to position 2 in list1
print ("New value available at index 2 : ")     # Print string
print (list1[2])                                # Print the value stored at position 2 in list1

#Adding
list1.append(2020)                              # Append a new value to end of list1
print("New List:", list1)                       # Print string, list1
