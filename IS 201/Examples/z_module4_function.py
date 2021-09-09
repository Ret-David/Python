
# -- function definition
#  Function DEFINITION 
# def function_name(parameters):
#     ''' doc string or help(function_name), function_name.__doc__ '''
#     statements
#     return something
#

# -- function definition without args, and return statements
def function1():
    ''' Function Name: function1()
        Argument: None
        Return Value: None
        Summary: Prints a greeting message '''
    name = "Harry"
    print("Hello, ", name, "! Good morning!")

def function2():
    ''' Function Name: function1()
        Argument: None
        Return Value: None        
        Summary: Prints a greeting message '''
    name = "Sally"
    print("Hello, ", name, "! Good morning!")

function1()
function2()

# -- function definition with arguments
# this function prints the name + message inside the function greeting
def greeting (name):
    print("Hello, " + name + "! Good morning!")

print("What is your name? ")
name = input()
greeting(name)

# -- function definition with return value
# this function returns a string that has the name and message,
# then it prints the message
def greeting2 (name):
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
name = input()
print(greeting2(name))


# -- MORE on function arguments
#    how about passing the message and name to be more flexible
def greeting3 (name, msg):
   print("Hello, " + msg + "! " + name)

print("What is your name? ")
name = input()
print("Enter the greeting message ")
msg = input()
greeting3(name, msg) # try without msg and explain the error message

#
# -- can we pass a list to a function?
#    I have a list of people and would like to greet individually with message.
def greeting_my_friends(friends_list, msg):
    for f in friends_list:
        print(msg + " " + f + "!")

friends1 = ("Jason", "Brenna", "Shannon")
friends2 = ["Jason", "Brenna", "Shannon"]

msg = input("Enter the greeting message ")
greeting_my_friends(friends1, msg)
greeting_my_friends(friends2, msg)

#
# passing a list, set, tuple
def addnumbs(x, y):     # a = [3, 4]
# def addnumbs(x, y, _):  a = [3, 4, 6]
# def addnumbs(x, y, *_): a = [3, 4, 5, 6, 7]
    return x+y
a = [3, 5]
# print(addnumbs(a)) --> x[0], x[1] passing a list itself
print(addnumbs(*a)) # list, tuple, set all work the same.

#
# passing a dictionary
def addnumbs(d):     
    s = 0
    print(d)
    for k, v in d.items():
        print(k, " ", v)
        s = s + v
    return s
d = {'a': 1, 'b': 2}
s = addnumbs(d)
print(s)

#
# Python program to find the common elements in two lists 
#
def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
  
    if (a_set & b_set): 
        print(a_set & b_set) 
    else: 
        print("No common elements")  

   
a = [1, 2, 3, 4, 5] 
b = [5, 6, 7, 8, 9] 
common_member(a, b) 

a = [1, 2, 3, 4, 5] 
b = [6, 7, 8, 9] 
common_member(a, b) 



# #
# # -- how about passing a dictionary to a function?
def greeting_my_friends2(friends_dict):
    for key in friends_dict:
        print(friends_dict[key], " " + key + "!") # key 
# d = {key: value} == {'name':'message'}
friends_greeting = {'Jason':'Good morning', 'Brenna':"I miss you", 'Shannon':"How have you been sis!"}

# -- let's look at Scope of Variables
# Do you remember this function?
# What is going on with 'name' variable inside greeting2() and 
# 'name' variable before calling greeting2()?

# Local variable, global variable can have the same name
# Local variables means local to the block (scope).
# Local variables cannot be used in the global scope.

# case #1
v = 1
def add_print_X():
    v = v + 10 # v can be accessed for reading but not writing in a local function
    print(v)

def add_print_O():
    global v # fix: use global keyword to indicate "i am accessing a global variable"
    v = v + 10
    print(v)

add_print_O()
add_print_X()


# This example will throw an error UnboundedError
#----------------------------------------------------
def greeting2 ():
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
# this name is global
name = input()
print(greeting2())
#----------------------------------------------------

#Fix1 (use global)------------------------- (1) remove global or use it as local (2) use global key to modify
def greeting2 ():
    global name
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
name = input()
print(greeting2())
#---------------------------------------------------

#Fix2 (passing the argument)-------------------------
def greeting2 (name):
    name = "Hello, " + name + "! Good morning!"
    return name

print("What is your name? ")
# this name is global
name = input()
print(greeting2(name))
#---------------------------------------------------

#Global v Nonlocal----------------------------------
name = "Harry" # remove when nonlocal
def greeting2(name):
    name = "Hello, " + name + "! Good morning!"
    print("greeting2-A = " + str(hex(id(name))))

    def greeting3():
        global name # this will print the same address as name (global)
        # nonlocal name # this will fix the problem of getting outside of local scope telling that "name is not defined in the local scope and to keep search outwards"
                      # Since the assignment limits the search for x to the local scope, it can't be found and I get the error.
        print(name) # when I do this, I access via Local scope(first) -> Enclosing scope(second) -> Global(third) -> Built-in(last)
        # therefore this 'name' is enclosed name defined in greeting2()
        name = name.upper() # new object at a new address
        print(name)
        print("greeting3 = " + str(hex(id(name))))
        return name
    
    print(greeting3())
    print("greeting2-B = " + str(hex(id(name))))
    return name

print("What is your name? ")
# pdb.set_trace()
name = input()
print("main-A = " + str(hex(id(name))))
print(greeting2(name))
print("main-B = " + str(hex(id(name))))
print(name)


# -- what is wrong with the following code and how would you fix
#   UnboundedLocalError?
# Note that the assignment limits the search for x to the local scope, it can't be found and I get the error.
def foo():
    x = 23
    def bar():
        # the reason why we are getting this error is 
        # self modifying operation such as += which means READ/WRITE operations at the same time
        x = x + 1 # fix via nonlocal. nonlocal / global are exclusive
        return x
    return bar()
print(foo())

#
# -- another example of using variable at a different scope
#
# name = "Harry" # this is a global variable
# def name_change():
    #    global name    accessing the global var
    # name = "Sally"
    # print("inside name_change(): ", name) # Sally (from local)

# name_change()
# print("outside name_change(): ", name) # Harry (from global)
name = "Johnson" # this is a global variable
def function1():
    name = "Harry"
    def function2():
        # nonlocal name #(follow the block)
        name = "Sally"
        print("Function2: ", name)
    function2()
    print("Function1:", name)

print("Outside Before:", name)
function1()
print("Outside After:", name)

'''
#1
c:\CityU\CS160\M1>test.py --> without nonlocal name in function2()
Outside Before: Johnson
Function2:  Sally
Function1: Harry
Outside After: Johnson
'''
'''
#2
c:\CityU\CS160\M1>test.py --> with nonlocal name in function2()
Outside Before: Johnson
Function2:  Sally
Function1: Sally <-- * name modified in function1() ie. Harry is replaced by ="Sally" assignment
Outside After: Johnson
'''

'''-------------------- OPTIONAL (built-in) try to avoid using builtin names ----------------------'''
'''
x = 'global x'
def foo():
    # y = 'local y'
    # global x
    x = 'local x'
    print (x)
foo()
print(x)
'''

'''
def test(z):
    x = 'local x'
    print(z)

test('local z') # try z out of scope
'''
''' built-in (min vs min(list))
# import builtins
# print(dir(builtins))

 def my_min():
    pass

m = min([5, 2, 1, 3])
print (m)
'''
'''
def outer():
    x = 'outer x'
    def inner():
        #nonlocal x # only available in the nest function blocks
        x = 'inner x' 
        print(x)
    inner()
    print(x)
outer()    
'''

''' (summary)
x = 'global x'
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x' 
        print(x)
    inner()
    print(x)
outer()    
print(x)
'''


def greeting3 (name, msg = "Good Morning!"): # default argument
   print("Hello, " + name + "! " + msg)

print("What is your name? ")
name = input()
print("Enter the greeting message ")
msg = input()
if len(msg) == 0:
    greeting3(name)
else:
    greeting3(name, msg) 













''' Exception handling 
def division(divisor):
    return 100/divisor
'''
def division(divisor):
    try:
        return 100/divisor
    except ZeroDivisionError:
        print('Error: Invalid Argument.')
        # return -1

print(division(10))
print(division(0)) 
print(division(50))


# Generator is very close to list comprehension
# Generator expression


