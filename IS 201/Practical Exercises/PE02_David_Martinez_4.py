# David Martinez

# 1) A buffet-style restaurant offers only five basic foods. Think of five simple foods,
#     and store them in a tuple.
basic_foods = 'baked fish', 'steamed rice', 'pot stickers', 'chocolate pudding', 'shrimp'

# 2) Use a for loop to print each food the restaurant offers.
for i in range(len(basic_foods)):
    print(basic_foods[i])

# 3) Try to modify one of the items, and make sure that Python rejects the change.
basic_foods[0] = 'salmon'

# Exception has occurred: TypeError
# 'tuple' object does not support item assignment
#   File "C:\Users\David\Desktop\School\IS201\python_work\PE02_David_Martinez_4.py", 
#            line 12, in <module>
#     basic_foods[0] = 'salmon'

# 4) The restaurant changes its menu, replacing two of the items with different foods.
#     Add a line that rewrites the tuple, and then use a for loop to print each of the
#     items on the revised menu.

basic_foods = 'salmon', 'steamed rice', 'pot stickers', 'cake', 'shrimp'
# temp_list = list(basic_foods)
# temp_list.remove('baked fish')
# temp_list.append('salmon')
# temp_list.remove('chocolate pudding')
# temp_list.append('cake')

# basic_foods = tuple(temp_list)

for i in range(len(basic_foods)):
    print(basic_foods[i])
