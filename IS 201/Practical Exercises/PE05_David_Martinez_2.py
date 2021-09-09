# David Martinez

# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a line recording
#     their visit in a file called guest_book.txt. 
# Make sure each entry appears on a new line in the file.

guest_name = ''                                           # start with an empty string variable

while guest_name != 'exit':                               # set 'exit' for the while escape
    guest_name = input("Please provide your name for the guest registry or 'exit': ")
    file = open('PE05_David_Martinez_2_guest_book.txt', 'a') # open file in append mode
    if guest_name == 'exit':                              # check if input equals 'exit'
        guest_name = ''                                   # if true, remove 'exit'
        file.close()                                      # close the file
        break                                             # end
    file.write(f'\n{guest_name}')                         # write the gurst name to the file
    file.close()                                          # close the file
