import inspect
import time

# Object Introspection :-
"""
To acknowledge an object and obtaining information about that object like it's class, it's source, it's type and how it is stored
into program is called as object introspection.
"""

# How to do Object Introspection :-
"""
A user can do object introspection by using different types of functions on an object. By using this type of different functions,
User can easily do research on objects. To do object introspection, we will create a class and some variables for beta tests.
"""


class Office:

    def __repr__(self):
        return f"Office({self.fname},{self.lname},{self.Email()})"

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"Email of Employee is :-{fname}{lname}@gmail.com"

    def print_details(self):
        return f"Employee's name is {self.fname} {self.lname} and has an email account named - {self.Email}"

    def Email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set. Please reset it through Setter."
        return f"Email of Employee is :-{self.fname}{self.lname}@gmail.com"

    @ property
    def Email(self):
        return f"Email of Employee is :-{self.fname}{self.lname}@gmail.com"

    @ Email.setter
    def Email(self, string):
        Name = string.split("@")[0]
        self.fname = Name.split("-")[0]
        self.lname = Name.split("-")[1]

    @ Email.deleter
    def Email(self):
        self.fname = None
        self.lname = None

    # def time_record(self):
    #     return time.time()


emp1 = Office("Player", "Unknown")

# print(emp1.time_record())

# Useful functions in Object Introspection are :-

# 1. Type :-
"""
Type function is used to identify class of an object , variable or class variable. 
Ex:- Suppose 'X' is a variable with a string value store in it. After 'X'is passed as argument in type(), 'X' will reveal 
it's class.
"""
# x = "This is Vishal"
# print(type(x))
"""
The output shows <class 'str'> which means x has a value whose type is 'string'. The result will differ if the type of value 
inside 'x' differs. 
"""
# a = 30
# b = 2.4456
# c = 3J + 1

# print(type(a))
# print(type(b))
# print(type(c))
"""
As you can see, <class 'int'>, <class 'float'>, <class 'complex'> define the difference value type of a, b and c respectively. 
Like variable's, objects also define their details upon executing with type. Suppose user has created an instance from class
named 'emp1'. The user wants to do object introspection on emp1 and he passes emp1 as an argument in type function. For 
information, 'emp1' contains "player" as fname and "Unknown" as lname.  
"""
# print(type(emp1))
"""
The output will let the user know that the object is derived from main function of it's owner class, i.e. Office. 
"""

# 2. id function :-
"""
id(identity) function reveals an object or variables's 'id', provided by Python on creation. Each variable can't have different 
id until they have different values from each other. In case of variables, the 'id' numbers are decided on the basis of 
value in a variable. Suppose variable 'X' and 'Y' have a similar int value then Python will give them a similar id number.  
"""
# x = 30
# y = 30
# print(id(x))
# print(id(y))
"""
In the output, Both variables have the similar id number, i.e. 1568262736. But if we changed y's value a bit then you can 
notice that the y's id number is changed. Let's change it and then observe both values. 
"""
# x = 30
# y = 40
# print(id(x))
# print(id(y))
"""
After values are changed, x remained with the smae id number as above but y's id number changed to '1568262896'. Other than 
assigning variables to values and then passing variable as an argument, user can enter values directly to obtain id numbers.
"""
# print(id("This is Vishal"))
# print(id(332))

# 3. dir :-
"""
'dir' function, when run with a variable or object, reveals all the possible methods which are executable for the respective 
variable or object. Suppose, User has created a variable named 'a' and assigned a string to it. When 'a' is passed as an argument
to 'dir', Python will return a list as an output. The list would be containing all the possible function which are executable 
with the string in the variable 'a'. 
"""
# a = "I am not here."
# print(a.__class__)
# print(dir(a))
"""
In the output, from '__add__' to 'zfill' , all the function in list are executable with the stated string. For example, 
1. with 'add' function you can add two strings. 
2. with 'class' you can get to know about type of variable 'a',i.e. clas 'str'.
3. with 'contains' you can check whether the string contains particular character or word or letter.

The 'dir' list will differ with change in value. Like 'string', 'int' and other types can contain different function and mutual 
functions as well. 'dir' function works the same with objects. But in the 'dir' list of objects, class variables and 
methods/attributes are also defined with executable functions. Let's pass 'emp1' as argument to dir and observe the list.
"""
# print(dir(emp1))

"""
'dir' list will contain Email, init(), fname, lname and print_details() which are either method or attributes from emp1's
class. Other than methods and attributes, list wil contain all the possible functions which are executable along with the
object.   
"""

# 4. Inspect module :-
"""
Inspect module is used to retrieve information about functions, methods, variables, frameworks, objects, etc. in a class 
or anything which holds certain value. The functions inside inspect can be used for different inspection purpose.

For Ex:- We will run 'getmembers()' function from 'inspect' module on 'emp1'. 
"""

# a = 5.66

# import inspect
# print(inspect.getmembers(emp1))
# print(inspect.getmembers(a))


"""
getmembers() will display a list which will contain all used/unused methods and attributes inside class 'Office'. But for 
a variable, getmembers() will do the same work as 'dir',i.e it will access the executable methods and functions for that 
variable.  

Inspect module's functionality differs with each function as other functions have different mechanisms to work. You can 
learn other functions of inspect through 'Google'
"""

# Exercise :-

import inspect
print(inspect.getsource(emp1))

