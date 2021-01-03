# Decorators of Python :-
"""
Decorators are used to modify the functionality of a function.
Ex:-
"""
# Test examples about user defined functions :-

# def func1():
#     print("This is Vishal")


# func2 = func1
# del func1
# func2()

"""
This code explains that a variable can be used to copy down a whole function. def func1() is a function which prints 
"This is Vishal" after called. func2 is the variable used to assign code of func1 to itself. To check whether the code 
of func1 can still exist, we will delete fuc1 by suing 'del' keyword. func2() is called which prints the same code lying 
in func1(). It was because at the time func1 was assigned to func2 the code of func1 was copied into it and then after 
deleting func1 from the file func2 was still able to print it.  
"""

# returning a function by a function :-


# def funcret(num):
#     if num == 1:
#         print(print)
#     elif num == 0:
#         print(float)


# funcret(1)

"""
In the above code, we are trying to return a function using a user defined function. functret() is a function which will
return function definition when we return an argument to the function. funcret() function has a if-elif condition in which
argument based conditions are given. when function is called with argument '1', funcret() will return definition of "print"
function and if the function is called with argument "0" then funcret() will return definition of "float" as an output.   
"""

# Using function as an argument :-


# def executor(func):
#     func("This is result")


# executor(print)

"""
Above function accepts built-in or user defined functions and co-operating with it, presents the result. executor function
is assigned with "func" which works as a common representative for any type of functions user wants to enter as an argument.
In func("This is result"), after user enters a function as argument, func redirects it to the called place and further the 
function will decide how to react with "This is result" and provide output. 

Suppose a user called executor function and entered "print" as the argument in place of "func", then further it will be 
directed to statement "This is result". The overall sum up of function for code will be print("This is result"). As code 
acknowledges that the respective statement is printable, it will print the statement as an output.

But if the user entered other function than print, which might be not able to co-operate with the statement, then the 
result will be an error.     
"""

# Concept of Decorators :-

# def dec1(func1):
#     def innerwere():
#         print("Executing the code.......")
#         func1()
#         print("Executed!!!!")
#     return innerwere()


# @dec1
# def identify():
#     print("He is Vishal Bawane")


# identify = dec1(identify())
# identify()

"""
This code shows how to use decorators in a function. As I said above, decorators modify the functionality of a function, 
here dec1 is the function which can be used to modify result of other functions. 

you can call dec1 as the current decorator. dec1 is assigned a representative argument "func1'. When a user enters a function 
as an argument, func1 will accept it and then dec1 will modify the following code. innerwere is the function declared inside 
function dec1. innerwere contains the main oode to modify argument function and return output. The mechanism of dec1 work as 
follows-
1. function is called along with dec1.
2. dec1 accepts the function and enters innerwere function for modification.
3. In innerwere function, two print statement and a function call is given. One print statement is before function call 
   and remnant is after the call. That means before the function result will be displayed, "Executing......" will be written
   on top of result. The print statement after function call means when the result will be displayed result will contain 
   ending with "Executed!!!".
4. To save modified code, return innerwere is written after the code. It makes sure that the function innnerwere will
   successfully display the modified code.
5. There are two methods to access the decorators with functions.  
   A :- calling function inside decorator function.
   B :- Writing @dec1 above the host code.    
    
"""


# calling function inside decorator function. :-


def dec1(func1):
    def innerwere():
        print("Executing the code.......\n")
        func1()
        print("Executed!!!!")

    return innerwere()


def identify():
    print("He is Vishal Bawane")


dec1(identify)

"""
This first method is calling the host function inside the decorator function. After the function is given as argument to
dec1, former function will execute itself and ultimately innerwere() function. After innerwere() is executed completely, 
modified result will be displayed.
"""

#  Writing @dec1 above the host code :-


def dec1(func1):
    def innerwere():
        print("Executing the code.......")
        func1()
        print("Executed!!!!")
    return innerwere()


@dec1
def identify():
    print("He is Vishal Bawane")


identify()
"""
In this second step, you should mark dec1 with symbol "@" on top of of the host function. In the above code, identify was
the host function. Before the declaration and definition of the host function, decorator function should be marked with @
on top of it's head. This will ultimately make python interpreter understand that the user wants to modify above function
with the function marked by "@"    
"""