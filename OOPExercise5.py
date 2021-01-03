# Using class method for alternative constructor :-

"""
Suppose a user wants to create an object by giving class as input and then passing a string which will get break down to
"name", "Salary" and "post".

The object must gain it's value from just a string statement and should cover all the 3 arguments of __init__() function
one by one through the broken down string. It will be wrong and tricky to change the code of init function for a one line
object and if the user does it, he will create an error for the object "Mukesh" and "Ramesh" which are dependent on init()
function for using and amending the value.

As only a string statement cannot be passed in place of 3 arguments of init() function. we will create a separate function
which takes class as input and string as the argument.



"""

#
# class Officers:
#     Pension = 15000
#
#     def __init__(self, Rename, Repost, Resalary):
#         self.name = Rename
#         self.post = Repost
#         self.salary = Resalary
#
#     @classmethod
#     def string_Converter(cls, string):
#         params = string.split("-")
#         print(params)
#         return cls(params[0], params[1], params[2])


# Mukesh = Officers("Mukesh", "Manager", 29999)
# Ramesh = Officers("Ramesh", "CEO", 50000)

# Umesh = Officers("Umesh-Clerk-15000")
# print(Umesh.name)

"""
As we can see, Python displayed error when we forced init() to break three arguments from a single string. To make such mechanism, 
we need to use classmethod decorator. As we want to modify our results, we will be using it directly. 
Ex:- We will create Prathamesh to test string_converter function.
"""

# Prathamesh = Officers.string_Converter("Prathamesh-peon-10000")
# print(Prathamesh.salary)

"""
So, We successfully created a decorator function which turns a string into arguments and then assigns themselves to the 
correct properties. Here,
cls --> represents a class. Here, it will represent "Officers".
string --> Argument for the string which is passed to be broken down into separate values. here, "Prathamesh-peon-10000"
           is the argument value.
string.split("-") --> This statement will first examine the string and then, split function will remove the place where 
                      '-' symbol were placed and replace it will commas(",").
params --> After string.split() complete their work, params will place the separated arguments one by one and in order into 
           a list.
cls(params[0], params[1], params[2]) --> The statement will be first matched with the statement which called the function,
                                         i.e "Prathamesh = Officers.string_Converter("Prathamesh-peon-10000")". Afterwards,
                                         the values of the object are stored through init function into it's auto-made 
                                         properties. Hence, on printing instance.variable pair, we ge accurate results.                                          

"""

# One-Liner string converter :-

"""
As we know how string_Converter works, we can still compress it's code to make it work more efficiently. This one-line 
statement will work the same as 3 statements worked.

For making the function one-liner, we will use reference operator(*). For Ex:- *args or *string. 
"""


class Officers:
    Pension = 15000

    def __init__(self, Rename, Repost, Resalary):
        self.name = Rename
        self.post = Repost
        self.salary = Resalary

    @classmethod
    def string_Converter(cls, string):
        # params = string.split("-")
        # print(params)
        return cls(*string.split("-"))


Mukesh = Officers("Mukesh", "Manager", 29999)
Ramesh = Officers("Ramesh", "CEO", 50000)

Prathamesh = Officers.string_Converter("Prathamesh-peon-10000")
print(Prathamesh.salary)

"""
The one liner string converter will follow this mechanism -
1. Function is called.
2. String statement is passed to the string_Converter function.
3. split function will break down the statement into three arguments and send them into a list.
4. init() will obtain the list and eventually, will withdraw arguments from it.
5. init() will match them and assign value to the corresponding property if user had provided accurate values.
6. After user requests for a specific instance.variable pair result, init() displays the corresponding value.


Advantage :-
Just by making function call, a user can create and assign lots of objects and properties without spending less time on 
manually creating objects and variables.  
"""

