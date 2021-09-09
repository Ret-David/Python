# David Martinez

def duplicateZeros(arr) -> None:    # None is used to define a null value, or no value at all.
    i = 0                           # assign index variable to zero
    # while i < len(arr)-1:         # loop until index == array end
    for i in range(len(arr)-1):     # step through index range, 0 thru 7
        if arr[i] == 0:             
            arr.pop()               # pop() the last item in the array
            arr.insert(i+1,0)       # insert 0 at current index
            i += 1                  
        i += 1                      # index mover, shorthand for i = i + 1
    print(arr)                      # print array

arr1 =[9,0,2,3,0,4,5,0]
duplicateZeros(arr1)

# The while statement allows the walking of the index till it hit the ending index number.
# Also, index 2 and 6 are skipped to allow for the inserted zeros.

# The for statement does not allow for any index to be skipped. This causes the zero in
# index 1 # to be pushed to the right by inserted zeros.
