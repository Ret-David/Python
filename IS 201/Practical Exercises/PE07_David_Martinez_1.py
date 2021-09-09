# David Martinez

# Make a class called User.
# Create two attributes called first_name and last_name, and then create
#     several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that prints a summary of the user's
#     information. Make another method called greet_user() that prints a
#     personalized greeting to the user.

class User:
    def __init__(self, first_name, last_name, user_id, user_level):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.user_level = user_level
        self.user_email = first_name + '.' + last_name + '@company.com'

    def describe_user(self):
        return "{} {} is assigned User ID: {}, with {} access.".format(self.first_name, self.last_name, self.user_id, self.user_level)

    def greet_user(self):
        return "Welcome, {} {}".format(self.first_name, self.last_name)

    def userEmail(self):
        return "Your user eMail will be {}.".format(self.user_email)

david = User("David", "Martinez", "DM001", "limited")
jay = User("Jay", "Johnson", "JJ001", "limited")
sierra = User("Sierra", "Honeycutt", "SH001", "limited")

print(david.greet_user())
print(david.describe_user())
print(f'{david.userEmail()}\n')
print(jay.greet_user())
print(jay.describe_user())
print(f'{jay.userEmail()}\n')
print(sierra.greet_user())
print(sierra.describe_user())
print(f'{sierra.userEmail()}\n')
