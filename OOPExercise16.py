# Operator Overloading & Dunder methods :-

# 1. Dunder methods :-
"""
The methods which start from double underscore are called as Dunder methods. In many examples of OOP, the __init__() function
was dunder method too, commonly can be called as dunder __init__()

dunder methods are called a special methods because like init(), this methods run the arguments and break them into separate
variable-values without actually running or calling the function. We are going to use this dunder methods in Operator Overloading.
"""

# Operator Overloading :-
"""
Operator overloading means giving an extended meaning to operators beyond their defined operational meaning. 

For Ex:- We all know that '+' sign is used to add two integers which gives output in 'sum'. But along with that the same operator
         same operator can be used to combine two strings as well as to combine two lists into one. Here, '+' operator's 
         different rules can be called as Operator Overloading.
         
In further topics, we will use dunder methods to overload an operator.         
"""

# Overloading an operator via Dunder methods :-
"""
suppose we have one class, class 'Juniors' with two instances, emp1 & emp2. 'Juniors' has a init() constructor which will 
be the help the user to break down provided arguments into variable-values.

If we try to add emp1 and emp2 together, the program obviously will throw an error. The erro will be like this , "TypeError: 
unsupported operand type(s) for +: 'Juniors' and 'Juniors'". It is because 'emp1' and 'emp2' are not integers, strings or
list which could be summed up or combined to form a result.As both are objects, '+' operator will fail to initialize their 
values and will throw an error due to un-acknowledgement of the type of values. As '+' can't do the job, User will overload 
the operator to make it able to add the two objects.

For Ex :-  User will create a dunder method which will overload the operator according to his will. 
"""


# class Juniors:
#
#     def __init__(self, Rename, Repost, Resalary):
#         self.name = Rename
#         self.post = Repost
#         self.salary = Resalary
#
#     @classmethod
#     def string_Converter(cls, string):
#         return cls(*string.split("-"))
#
#     def printdetails(self):
#         return f"Employee name is {self.name}.\nEmployee's post is {self.post}.\nEmployee salary is {self.salary}\n  "
#
#     def __add__(self, other):
#         return self.salary + other.salary
#
#
# emp1 = Juniors("Vishal Bawane", "Senior Manager", 45000)
# emp2 = Juniors("Amish Patil", "Clerk", 15000)
#
# print(emp1 + emp2)

"""
Here, __add__() is the dunder method which will help the operator to be overloaded. The __add__() is actually an in-built 
dunder method which comes up with 2 common arguments, self and other. Self means first object and other means second object.
Then, 'salary' was the common attribute provided to both objects so that the '+' operator will add the values of salaries 
of both objects and present result which shows their 'sum'. Other than 'salary' you can select another properties as well 
but both should have the same type otherwise '+' operator will give an error as two different types of variables cannot 
be added. Here, the type of salary's value was 'int' and hence, the result will display '60000'(45000 + 15000) as result. 
Due to the combination of instance.variable, __add__() method will easily come to know what to add after User asks to
print 'emp1' and 'emp2'.

As I said, Dunder methods quickly acknowledge the program written inot them and without running or calling, they can execute 
the code. After "emp1 + emp2" was asked to print, __add__() sensed the syntax and according to it processed the code further.

To get to know about more dunder methods which help in operator overloading, visit the "mapping operator to function" page of 
python documentation. It has many tables which will let you know about the dunder methods, their syntax and how to execute them.   
"""

# Repr and __str__ method :-
"""
__Repr__() is used to represent an object in a better form . Let's learn it through an example.

For Ex:- 

If we print object 'emp1' only, then python will reveal memory location of the object and other unknown things in an encrypted form 
than printing it's name, salary and post, etc. 

Suppose, The user wants to change emp1's complex format into a readable format. To achieve it we will user __repr__() method.
In the method, 'self' will be the argument which is 'emp1' here. Let's assign the printdetails() to it and observe what 
will happen.
"""


# class Juniors:
#
#     def __init__(self, Rename, Repost, Resalary):
#         self.name = Rename
#         self.post = Repost
#         self.salary = Resalary
#
#     @classmethod
#     def string_Converter(cls, string):
#         return cls(*string.split("-"))
#
#     def printdetails(self):
#         return f"Employee name is {self.name}.\nEmployee's post is {self.post}.\nEmployee salary is {self.salary}\n  "
#
#     def __repr__(self):
#         # return self.printdetails()
#         return f"Juniors ('{self.name}','{self.post}',{self.salary})"
#     def __add__(self, other):
#         return self.salary + other.salary
#
#
# emp1 = Juniors("Vishal Bawane", "Senior Manager", 45000)
# emp2 = Juniors("Amish Patil", "Clerk", 15000)

# print(emp1 + emp2)
# print(emp1)

"""
As you can see, after printdetails() was assigned to __repr__(), repr() accessed the printable object through printdetails() 
code. After printdetails() decoded emp1's encrypted format, it presented the values of properties in the object through
printdetails() format. 

The __repr__() function means "To Represent". repr() function needs a separate function to represent the object. After repr()
is execute indirectly, the output will be based on the code of "separate function" while repr() will do the job of host 
only. Other than guest functions, User can itself arrange the syntax of repr() to get desired output.
 
For Ex:- If the user wants repr() to display the exact form of emp1, just as user declared 'emp1' with class constructor 
and "arguments' above, You can either remove or modify function to create your own code for displaying the wanted result.  
"""

# print(emp1)

"""
After 'emp1' is print, program will reach repr() for representing object. repr() will execute the code and then the output 
will be displayed as "Juniors ('Vishal Bawane','Senior Manager',45000)". The output is as same as the syntax we declared 
in repr(). 

A user can even manipulate the type of an argument in the repr().
For Ex:- In the manual syntax of repr(), (self.name) and (self.post) are quoted into a single quote which after execution 
of repr() will give the values a look of "string". You can try it on other values for practice. 
"""

# __str__() method :-
"""
__str__() method is used to return string representation of objects while repr() is used to return presentation of object
in desirable expression.You can consider the "printdetails" and "manual syntax" example from __repr__() topic.

Like repr(), str() also requires code or function as an associate to represent the object.    
"""

class Juniors:

    def __init__(self, Rename, Repost, Resalary):
        self.name = Rename
        self.post = Repost
        self.salary = Resalary

    @classmethod
    def string_Converter(cls, string):
        return cls(*string.split("-"))

    def printdetails(self):
        return f"Employee name is {self.name}.\nEmployee's post is {self.post}.\nEmployee salary is {self.salary}\n  "

    # def __repr__(self):
    #     # return self.printdetails()
    #     return f"Juniors ('{self.name}','{self.post}',{self.salary})"

    # def __str__(self):
    #     return self.printdetails()

    def __add__(self, other):
        return self.salary + other.salary


emp1 = Juniors("Vishal Bawane", "Senior Manager", 45000)
emp2 = Juniors("Amish Patil", "Clerk", 15000)

# print(emp2)
"""
Here, Str() was provided with printdetails() function and then after execution, str() displayed the output exactly similar 
as it should be from printdetails(). 

Another noticeable fact is, after user asked to print 'emp1' str() executed and displayed output but repr() didn't execute.
It is because, Python has more interest in executing str() than repr(). If a program contains str() and repr() both, then 
the program will execute str() only and will ignore repr(). You can see the live example in the above program.

To use repr in a program where str() is present too, the user should do typecasting. When emp1 is asked to print, the user 
can add repr in front of it and thne python will execute the object from repr() only and will ignore str() this time.  
"""

# print(str(emp2))

"""
Hence, the result can be successfully handled by typecasting. To do typecasting, existence of program/method is more important.
If user tries to typecast an object through a method which is not declared or does not exist in the program, the statement 
will execute the statement through repr() method.
 
"""
# print(str(emp1))

"""
As a result, repr() will be executed and in the output we can see that the result is in syntax of repr(). Again if user 
removes repr() and tries to print through str() or repr() this time, user will get to see object's encrypted form which 
is the original form of any object before being decoded and processed into any method. 
"""
# print(repr(emp1))
# print(str(emp1))


# Exercise :-
# class BETA:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __eq__(self, other):
#         return self.salary == other.salary
#
#     def __and__(self, other):
#         return self.salary & self.salary

#     def __lt__(self, other):
#         return self.salary < other.salary
#
#
# emp1 = BETA("Naman", 23)
# emp2 = BETA("Chaman", 30)
# print(emp1 < emp2)