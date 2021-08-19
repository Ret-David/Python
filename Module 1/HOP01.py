# HOP01- David Martinez
# From Kim Nguyen, 4. Python Decision Making Challenge
#  Fix the program so that the user input can be recognized as an integer. 

# Original Code
guess = input("Please guess a integer between 1 and 6: ")
randomNumber = 5

if (guess == randomNumber):
    print("Congrats, you got it!")
else:
    print("Oops, goodluck next time!")

# Corrected code identifying guess and randomNumber as integers.
guess = input("Please guess a integer between 1 and 6: ")
randomNumber = 5

if (int(guess) == int(randomNumber)):
    print("Congrats, you got it!")
else:
    print("Oops, goodluck next time!")


# ------------------------------
# From Kim Nguyen, 5. While loop
#  Fix the program so that the it only allows three guesses.

# Original Code
attempt = 0
randomNumber = 5

while attempts <= 3:
    guess = input("Please guess a integer between 1 and 6: ")

    if (guess == randomNumber):
        print("Congrats, you got it!")
    else:
        print("Oops, goodluck next time!")
    
    attempts += 1

# Corrected code that allows for only three guesses.
#  I found that you could either set the variable attempt to 1
#  or you can change the while attempts to <= 2.
attempts = 1
randomNumber = 5

while attempts <= 3:
    guess = input("Please guess a integer between 1 and 6: ")

    if (guess == randomNumber):
        print("Congrats, you got it!")
    else:
        print("Oops, goodluck next time! Attempt #", attempts)
    
    attempts += 1

#  or you can change the while attempts to <= 2.
attempts = 0
randomNumber = 5

while attempts <= 2:
    guess = input("Please guess a integer between 1 and 6: ")

    if (guess == randomNumber):
        print("Congrats, you got it!")
    else:
        print("Oops, goodluck next time! Attempt #", attempts)
    
    attempts += 1


