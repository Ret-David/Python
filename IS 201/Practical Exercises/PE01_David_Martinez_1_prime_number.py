# David Martinez
# Test whether the input integer is prime or not.

# Input an integer to test for prime.
user_num = int(input("Input an integer to test as prime: "))

# Test whether the input integer be divided by itself and 1.
#  Modulus will return a remainder of 0 for a True value
for i in range(2, user_num):
    if (user_num % i) == 0:
        # print(i)
        # print(bool())
        print(user_num, "is not a prime number.")
        break

else:
    # print(i)
    # print(bool())
    print(user_num, "is a prime number.")
