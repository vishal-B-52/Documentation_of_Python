# Overriding and Super() :-
"""
1. Overriding variables -
We are now now learning about override. we will try to understand it through some examples.
Suppose a user has created two classes, i.e A and B and has allotted them some attributes and one method each..
"""
# This is just an example which states how a program finds instance.variable or variable from multiple similar variable names.

# class A:
#     var1 = "This is the area of class A"
#     def __init__(self):
#         self.name = "Vishal"
#         self.age = "18"
#         self.var1 = "This is definitely class A"
#
#
# class B(A):
#     var2 = "This is the area of class B"
#
#
# a = A()
# b = B()
#
# print(b.var1)

"""
If the statement is executed, you can actually see the effect of overriding. When you print the statement, It is obvious 
that class "B" will look for the variable in itself first. After the variable is not found, B will look for the variable 
into it's parent class. But rather than going for the 'var1' variable, program will pick the value of 'self.var1'(from init) 
and will display the output.

This happened due to the format and the way 'var1' was asked to print. The main format is 'self.var1' in init() constructor. 
As B is inherited from A, B is allowed to access the constructor of A and assign values to it's instance-variable pair. 
After b.var1 was asked to print, program considered the requested pair as an instance.variable pair. Later, program searched 
for the respective pair in class B and after it was not found, program got a perfect match in the init() constructor of 
class A. Thus, In the end, "self.var1"'s value was considered and other similar values(var1 of class A) were ignored.

The above theory does not explains overriding but still is an essential part of OOP language which needs to be studied 
briefly.    
"""

# Overriding's mechanism -
"""
Overriding is stated many time in the previous topics of OOP exercises(mainly in inheritance) .

Overriding means redeclaring an attribute or function in a separate or inherited class which is already present in the parent 
class. Overriding is subsequently done by child class to overwrite attributes and functions of parent class for changing values which are 
suitable for them. With the redeclaration of same elements again in another class, Overriding prevents the user form using 
those respective redeclared values in program.

Let's try to understand it through some examples.
"""

# Overriding Functions -
"""
Whenever a method in OOP is override, it becomes useless bu the view of Python and everytime the interpreter will suggest
the overriden value of method. 

Let's try to learn it through an example on how overriding affects method using. We will create 2 classes. First class will 
have a init() constructor. The second class will be an inherited class from the first one.  
"""

# class something:
#     var1 = "Something's value"
#
#     def __init__(self):
#         self.name = "Vishal"
#         self.stringvalue = "This variable keeps the stringvalue"
#
#
# class someone(something):
#     var2 = "Someone's value"
#
#     def __init__(self):
#         self.name = "Mayank"
#         self.stringvalue = "This variable has a private value"
#
#
# a = something()
# b = someone()
#
# print(b.name)

"""
After user executes the above statement, the values gained from output will be the values returned by constructor of 'someone'
and not from the construtor of class 'something'. It is partially versatile effect of Override.

Overriding permanently made program forget about the coverage of init() of class 'something' and values inside it. Instead of 
class 'something''s constructor, Program chose class 'someone''s constructor as the main constructor and returned values from 
'something' as per asked by user.

class 'something''s constructor can't be accessed until unless the overriden method is removed.
"""

# Super() :-
"""
super keyword is used to access an overiden method and it's attributes. 

Considering the above example, let's assume that the overiden method had a different variable than that of class 'someone' 
and user wants to acess it without uplifting the overide on 'something'. Indirectly the user wants to access overriding 
method and overriden method at the same time. To fetch this variable, User can use super() keyword.

To access an overiden value and function, user must type the following statement in the override controller class.

super().__init__()
"""

# What is super and how to use it :-
"""
Super means superclass. In the above program, 'someone' is the base class of 'something' which means something is the parent
class whereas someone is the child class. In simple words or OOP language, this classes can be called as Superclass and 
Subclass. So by this relation, 'something' becomes the superclass and 'someone' becomes the subclass. 

The above statement means 'from superclass call init() function'. You can call any function rather than init() if the corresponding
function is overriden.

super temporarily uplifts the limitations of override from the overiding method and allows user to access the data from 
class 'something' and 'someone' simultaneously. But Super is sensitive-case keyword when it comes to giving position.  

In the video, super was declared above initialization of init() constructor's attributes. After then , when the values were 
printed, the values from init() of 'someone''s attributes were displayed. 'something''s values were not printed just because 
super was not placed on a right position.

The mechanism behind it is, super was called which called the values of something's values as well. Then, initialization of someone's 
attributes took place. Because the initialization was in a later phase, the previous values of variables got overwrite as 
they had same variable names and hence, super had no effect on the result.
Ex:-
"""


# class something:
#     var1 = "Something's value"
#
#     def __init__(self):
#         self.name = "Vishal"
#         self.stringvalue = "This variable keeps the stringvalue"
#         self.somevalue = "haha!! JOKE"
#
# class someone(something):
#     var2 = "Someone's value"
#
#     def __init__(self):
#         super().__init__()    # Note:- Dont's forget to provide parenthesis to super or you will face error.
#         self.name = "Mayank"
#         self.stringvalue = "This variable has a private value"
#
#
# a = something()
# b = someone()
#
# print(b.name, b.stringvalue)

"""
You may have noticed it now after the result. To correct this, The user should put the super() statement after initialization 
and then print values.
Ex:- 
"""

class something:
    var1 = "Something's value"

    def __init__(self):
        self.name = "Vishal"
        self.stringvalue = "This variable keeps the stringvalue"
        self.somevalue = "haha!! JOKE"

class someone(something):
    var2 = "Someone's value"

    def __init__(self):

        self.name = "Mayank"
        self.stringvalue = "This variable has a private value"
        super().__init__()


a = something()
b = someone()

print(b.name, b.stringvalue)

"""
This time due to the correct mechanism, Program will print values of attributes returned by 'something''s constructor. This 
was all about accessing the attributes from overriden method. Suppose a variable is only present in class 'something' and 
not in 'someone', then to access it user do not have to care about position of super(). User can easily access a different 
variable easily after wherever a super() statement is declared. 
For Ex:- In above two codes of positioning super(), try to print "somevalue"(different variable) and you will succeed. 
"""

