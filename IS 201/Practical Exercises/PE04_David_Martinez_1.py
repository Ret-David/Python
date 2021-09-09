# David Martinez

def make_shirt(size = 'Large', message = 'I Love Python'):
    ''' Shirt making statement. '''
    result = print(f'\nA {size} shirt will be made with the saying "{message}" on it.')

# size = input("What size shirt would you like? ") # Task 1
# message = input("What message would you like printed on your shirt? ") # Task 1

size = 'Large'
message = 'I Love Python'

make_shirt(size, message)                 # Task 1 & 2
make_shirt(size='Medium')                 # Task 2
make_shirt(size='Small', message='foo')   # Task 2
