# David Martinez

def first(n):
    return n[0]

def sort_list_first(tuples):
    return sorted(tuples, key=first)

print(sort_list_first([(5, 2), (2, 1), (4, 4), (3, 2), (1, 2)]))



# Results from code above.
# [(1, 2), (2, 1), (3, 2), (4, 4), (5, 2)]
# PS C:\Users\David\Desktop\IS201\is201-fundamentals-of-computing-spring2021-Ret-David\Module 2>