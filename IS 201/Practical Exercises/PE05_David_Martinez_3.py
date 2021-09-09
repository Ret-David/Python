# David Martinez

# Write a program that prompts for two numbers.
# Add them together and print the result.
# Catch the ValueError if either input value is not a number, and print a friendly
#     error message.
# Test your program by entering two numbers and then by entering some text instead
#     of a number.

while True:  # while statement to loop through exception handling till a true value is produced
    try:  # run the following code block, test for errors
        first_num = int(input("\nLet's see what the value of two numbers you provide equal."
                              "\nProvide your first number, please: "))
        break  # exit this while statement
    except ValueError:  # if an invalid value is produced, print the following message
        print("Providing a valid number would be helpful, try again, please.")

while True:  # while statement to loop through exception handling till a true value is produced
    try:  # run the following code block, test for errors
        second_num = int(input("Provide your second number, please: "))
        break  # exit this while statement
    except ValueError:  # if an invalid value is produced, print the following message
        print("Really? And you were doing so good! Try again, please.")

total_sum = first_num + second_num  # total sum variable
print(f'The sum of your first number, {first_num}, plus the second number, {second_num}, '
      f'equals {total_sum}.')  # friendly total sum message for screen output
