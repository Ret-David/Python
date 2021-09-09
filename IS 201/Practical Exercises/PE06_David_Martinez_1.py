# David Martinez

# Make a class called Restaurant. The __init__() method for Restaurant should
#     store two attributes: a restaurant_name and a cuisine_type. Make a method
#     called describe_restaurant() that prints these two pieces of information,
#     and a method called open_restaurant() that prints a message indicating that
#     the restaurant is open.

# Update the above program by creating three different instances from the class,
#     and call describe_restaurant() for each instance.

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name              # instance variable
        self.cuisine_type = cuisine_type                    # instance variable

    restaurant_name = 'Spike\'s Grill'                      # member variable
    cuisine_type = 'Southern BBQ'                           # member variable

    def describe_restaurant():                              # method
        return f'{Restaurant.restaurant_name} is a {Restaurant.cuisine_type} style restaurant.'

    def open_restaurant():                                  # method
        return 'We are OPEN, come join us!\n'

    def closed_restaurant():                                # method
        return 'We are currently CLOSED, come back tomorrow!\n'

print(f'{Restaurant.describe_restaurant()}\n{Restaurant.open_restaurant()}')

''' Jabba's restaurant description '''
Restaurant.restaurant_name = 'Jabba\'s Place'
Restaurant.cuisine_type = 'Pizzeria'
description = Restaurant.describe_restaurant()              # instance
print(f'{description}\n{Restaurant.open_restaurant()}')

''' Yogi's restaurant description '''
Restaurant.restaurant_name = 'Yogi\'s Pitstop'
Restaurant.cuisine_type = 'Chicago Hotdog'
description = Restaurant.describe_restaurant()              # instance
print(f'{description}\n{Restaurant.closed_restaurant()}')

''' Daisy's restaurant description '''
Restaurant.restaurant_name = 'Daisy\'s'
Restaurant.cuisine_type = 'Organic Dog Food'
description = Restaurant.describe_restaurant()              # instance
print(f'{description}\n{Restaurant.open_restaurant()}')
