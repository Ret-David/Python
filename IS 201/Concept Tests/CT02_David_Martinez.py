# David Martinez
#
# Write a pseudo code to write a program that takes one integer number at a time
#  continuously from a user and halts its execution when the sum of input values
#  is greater than 25.

# My Pseudo Code
#  Establish the integer variable.
#  Request user's 1st integer input under 25.
#  Use a while statement to loop through till greater than 25 is reached.
#  Embed an if statement for the while loop to use.
#  Use the if statement for 2nd question input and beyond.
#  Print total sum statement once greater than 25 is reached.


# Establish user_number.
user_number = int(0)
# Request first user input.
user_number = int(input("Provide a number under 25, please: "))
# Using a while statement to loop through till the sum is greater that 25.
while user_number < 26:
        if user_number < 26:
                user_number = user_number + int(input("Provide another number under 25, please: "))
        else:
                print("You're total sum of", user_number, "is greater than 25!")
else:
        print("You're total sum of", user_number, "is greater than 25!")
