# Acces Specifiers :-
"""
There are total 3 class access specifiers in Python language, i.e Public, Private and Protected.

Note :- In Python, The access specifiers are declared by underscores and not by keywords. The user has to provide one underscore
        to declare a variable "protected" and two underscores for a "private " variable.
"""
# 1. Public:-
"""
This specifier is by-default present in Python classes. This specifier do not needs any symbol/sign to declare a variable 
as "public". By keeping a variable as same as it is, you can declare it a "public" variable.

"""
# testing Public variable's reach:-
"""
Here, we will create 3 separate classes, i.e Emperor, War_minister and Commander. Commander is the child of Emperor which 
gives him all access to Emperor's attributes. War_minister is not any associate of Emperor which denies all the possibilities 
of him to access anything from Emperor(not Even public variable)
"""
# class Emperor:
#     name = "Vishal"
#     age = 18
#
#
# class Commander(Emperor):
#     pass
#
#
# class War_minister:
#     pass
#
#
# Henry = Emperor()
# Darius = Commander()
# PTolemy = War_minister()
#
# print(Emperor.name)
# print(Commander.age)
# print(PTolemy.age)

"""
The above print statement will get executed easily and output will be as same as the value of variables were. The presence 
or absence of declaration of this specifier does not matters in Python. The Public variables can be easily accessed by base class, 
inherited class, instances of base & child class and inside & outside both classes as well. 
"""

# 2. Protected :-
"""
To make a variable "Protected", write a variable name and join one "underscore" before the variable name. This access specifier 
do not allows any outside class or outside program to access and use it. This type of variables are accessible through base 
class & it's instances and inherited class & it's instances only. 
 
For Ex:- We will create a variable "money" and declare it as "Protected". Then we will try to access it through all methods
         in order to understand it's properties.
"""
# class Emperor:
#     name = "Vishal"
#     age = 18
#     _money = 1,20,34,66,00,00,000
#
#
# class Commander(Emperor):
#     pass
#
#
# class War_minister:
#     pass
#
#
# Henry = Emperor()
# Darius = Commander()
# PTolemy = War_minister()
#
# print(Emperor._money)
# print(Commander._money)
# print(War_minister._money)
# print(Henry._money)
# print(Darius._money)
# print(PTolemy._money)
"""
As you have seen, Except the class "War_minister" and it's instance, others were available to easily execute the statements 
and print value of "_money". Thus, it proves that no outside class can access Protected variables

Note1 :- Access specifiers like "Protected" and "Private" have an ability to remove the specific variable from suggestions.   
       For Ex:- In above code, when we tried to write "_money", it didn't made any appearance in suggestions of all 3 classes.
       Python intentionally did it for safety purpose to avoid accidental use of this variables in programs. Thus, It makes 
       a protected variable really secure in programs.  

Note2 :- Though you can't make protected variable appear in the suggestions outside class, they can appear in suggestions 
         if the user uses the protected variable inside base ad inherited class.  
"""

# Private :-
"""
This access specifier is used to prevent other classes ,excluding base and inherited class, from using the "private" declared 
variable. To make a variable Private, the user must add two underscores before the variable name. 

For Ex:- We will declare a private variable inside Emperor and then try to print it with all methods.  
"""

class Emperor:
    name = "Vishal"
    age = 18
    _money = 1,20,34,66,00,00,000
    __wife = 3

class Commander(Emperor):
    pass


class War_minister:
    pass


Henry = Emperor()
Darius = Commander()
PTolemy = War_minister()

# print(Emperor.__wife)
# print(Commander.__wife)
# print(War_minister.__wife)
# print(Henry.__wife)
# print(Darius.__wife)
# print(PTolemy.__wife)

"""
Surprisingly, None of the statements will execute and prsesent output. Being a private variable, this type of variables 
also has an ability to be expressed only inside the class and not anywhere else. When you try to print "__wife" inside class
it will be printed successfully whereas outside(base, inherited, non-inherited) class is a prohibition. Actually it is a 
method applied by Python, which restricts any program to use a private variable outside the class. The method is called 
as name mangling method. It was applied in order to avoid conflicts between a normal variable having the same name like 
private variable has.  

There is only one way to print a private variable outside the class. The user must write the base class name of the private 
variable in front of the 'private' variable. In addition, before writing base class name, add an underscore and then type 
the whole class name. Now, You can print it. Except the part after dot extension, you can print the private variable using 
name of base and inherited class as well as instances of both classes.
"""
print(Darius._Emperor__wife)

"""
Python wants the user to print a private variable through such tricky and complex method is to avoid confliction and nothing. 
The method simply prevents mis-handling of private variables outside base class.

Note :- The user must add only one underscore before base class name otherwise Python will give an error regarding absence 
        of private variable in the base class. 
"""