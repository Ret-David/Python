# David Martinez

def string_count(my_string):
    ''' Count lower and upper case characters in a string. '''
    lower = 0                           # Init variable
    upper = 0                           # Init variable
    for i in my_string:                 # Step through string
        if (i >= 'a' and i <= 'z'):     # Evaluate if index character is lower case a-z
            lower = lower + 1           # If true, add 1 to lower variable
        elif (i >= 'A' and i <= 'Z'):   # Evaluate if index character is lower case A-Z
            upper = upper + 1           # If true, add 1 to upper variable
    
    print('No. of Upper case characters : ', upper) # Number of upper case characters
    print('No. of Lower case characters : ', lower) # Number of lower case characters
    
my_string = "The quick Brown Fox jumped over the Lazy Dog."
split_words = my_string.split()

print("No. of words in the string : ", len(split_words))
string_count(my_string)

# Feedback from Instructor
# check out isupper() or islower().
