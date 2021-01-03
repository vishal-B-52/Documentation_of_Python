# Functions -
"""It is or It contains  a block of code which only runs when it is called. You ccan give parameters, data, arguments in
 a fucntion."""

# Bulit in functions - This functions are already present in interpreter which do not need to be installed through
# internet."""

import random

# list = ["Vishal", "Faroff", "Atlantis", "Taskmaster"]
# lister = random.choice(list)
# print(lister)

# User defined functions - This functions are defined by user which are different than built-in functions. You have to
# use 'def' keyword before the specific function name. Indentation are needed everytime you use user-define functions.
# You need to call it everytime.


# def getdata():
#    a = random.randint(1, 100)
#    b = random.randint(1, 100)
#    c = a + b
#    print(c)


# getdata()

""" 
Functions call decreases the work load and time consumption. Instead of printing a string again and again, enter the
code in function and call the function to print value.
"""


# Functions with user inputs - In normal functions, when function is called it prints the code inside function without
# asking for input values. For input values, functions should be provided with specific arguments. After arguments are
# provided, you should type in values to obtain input from the code. EX:-


# def gettto(a, b):
#    c = a + b
#    print(c)


# gettto(12, 33)

# Return Keyword - Useful to store value of called function in a variable. When you use a return keyword, the value of
# code shifts to return and then it becomes easy to print called function. You will get "None" if you tried to print
# called value without Return.
# As well as, Another use of Return is that, it prevents any type of code to be written after declaration of it. In following
# example, after writing 'return a+b' code won't allow me to write anything further.
# Another use of it is that it allows user to call function from a separate variable whereas a normal function will print
# 'None' and 'result' one by one. For Ex:-

def Myfunc():
    a = int(input("Enter number for a: "))
    b = int(input("Enter number for b: "))
    # Print(a + b)
    return a + b


# s = Myfunc()
# print(s)


print(Myfunc())

# On going with return, you can see that the result is being printed through 's'. On going with normal conditions, result
# will print but None will assist it too.



# Docstring - Useful to give a summary about a function. Can be used to warn or notice about the respective function.
# funct.__doc__() will print the docstring of the function. The docstrings are a type of comment which are invisible
# when you run any code in it. In order to print it use the above function.
# def gettto():
#
#     """Defineing function here"""
#     print(gettto.__doc__)
#
#
# gettto()









