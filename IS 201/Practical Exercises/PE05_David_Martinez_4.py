# David Martinez

# Make two files, cats.txt and dogs.txt.
# Store at least three names of cats in the first file and three names of dogs in
#     the second file.
# Write a program that tries to read these files and print the contents of the file
#     to the screen.
# Wrap your code in a try-except block to catch the FileNotFound error, and print a
#     friendly message if a file is missing.

while True:  # while statement to loop through exception handling till a True value is produced
    try:  # run the following code block, test for errors
        cat_file_open = open("PE05_David_Martinez_4_cats.txt", "r") # variable assigned to file
        cat_file_open.readline()    # read the lines of the file into the variable
        for cats in cat_file_open:  # for each cat name in the file
            print(cats, end='')     # print their name to screen, strip the new line
        print("\n")                 # add a new line at the end of the names
        cat_file_open.close()       # close the open file

        dog_file_open = open("PE05_David_Martinez_4_dogs.txt", "r") # variable assigned to file
        dog_file_open.readline()    # read the lines of the file into the variable
        for dogs in dog_file_open:  # for each dog name in the file
            print(dogs, end='')     # print their name to screen, strip the new line
        print("\n")                 # add a new line at the end of the names
        dog_file_open.close()       # close the open file
        break  # exit this while statement

    except FileNotFoundError:  # if an file name is produced, print the following message
        print("Your code needs a valid file name or path, please.")
        break  # exit this while statement
