# David Martinez
# Class Challenge 1

# Write a Python class called ReturnInput which has two methods get_Input and
#     print_Input. get_Input accept any input from the user and print_Input
#     print the input.
#
# Then create 2 instances of class ReturnInput.
#     One is called ReturnString, which only accepts inputs of type string, and print
#         the input in all upper case.
#     The other instance is called ReturnNum, which only accepts numeric inputs. All
#         returned values must be integers (if the input is a decimal number, you must
#         return a rounded integer).

class ReturnInput:
    ''' Message user input method '''
    def get_Input(message=''):
        message = input('Type me a message: ')
        return message

    ''' Number user input method '''
    def get_Num():
        num = float(input('Give me a number: '))
        return round(num)

    ''' Format message and print '''
    def print_Input():
        print(f'You typed "' + ReturnInput.get_Input() + '".\n')

ReturnInput.print_Input()       # run the print_Input method

''' Convert the message to all caps. '''
ReturnString = ReturnInput.get_Input().upper()
print(f'We converted your message "{ReturnString}" to all caps.\n')

''' Error trap for number input, then return a rounded output. '''
while True:
    try:
        ReturnNum = ReturnInput.get_Num()
    except ValueError:
        print('That\'s not a number, try again!\n')
    else:
        print(f'Your typed number is "{ReturnNum}", rounded.\n')
        break
