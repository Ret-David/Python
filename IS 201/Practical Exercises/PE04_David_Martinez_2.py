# David Martinez

def describe_city(city, country='Iceland'): # default country defined
    ''' States a given city in a given country. '''
    result = print(f'\n{city} is a city in {country}.') # results sentence
    
# city = input("What is the city name? ")       # for user input
# country = input("What is the country name? ") # for user input

city = ''       # empty city variable
country = ''    # empty country variable

describe_city('Reykjavik')      # 1st def call
describe_city('Njardvik')       # 2nd def call
describe_city('Madrid','Spain') # 3rd def call
