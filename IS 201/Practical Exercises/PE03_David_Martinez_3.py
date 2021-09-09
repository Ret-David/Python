# David Martinez

# Write a Python program to combine two dictionary adding values for common keys. 

# Sample Dictionary:
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

from collections import Counter # dictionary subclass for counting values

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = Counter(d1) + Counter(d2)  # use Counter object to add common key values and merge dictionaries

print(d3)                       # print the Counter merged dictionary
