# David Martinez

# 1) Think of at least seven different animals. Store the names of these
#     animals in a list, and then use a for loop to print out the name of each
#     animal.
# 2) Print the message The first three items in the list are:. Then use a
#     slice to print the first three items from that program's list.
# 3) Print the message Three items from the middle of the list are:. Use a
#     slice to print three items from the middle of the list.
# 4) Print the message The last three items in the list are:. Use a slice to
#     print the last three items in the list.

animals = ["dog", "cat", "quail", "turkey", "deer", "hawk", "duck"]    # 1

for i in animals:
    print(i)

print("The first three items in the list are:", animals[:3])           # 2

print("Three items from the middle of the list are:", animals[2:5])    # 3

print("The last three items in the list are:", animals[-3:])           # 4
