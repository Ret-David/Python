# David Martinez

# Given a list of tuples, write a Python program to sort the tuples by the
#     second item of each tuple.
# Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
# Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]

tuple_input = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
print(tuple_input)

tuple_input.sort(key=lambda x: x[1])
print(tuple_input)



# 4.7.6. Lambda Expressions
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)
