# Multi-level Inheritance :-
"""
Derivation of a class from one class and another from the one is often called as Multi-level inheritance.

Suppose a user has created a class "Dad". Then user inherits a class "Son" from it. Now "Son" can owe anything from "Dad"
being a child class. But again user inherits class "GrandSon" from "Son". This enables "Grandson" to use any attribute/
function from class "Son" and "Father" easily.
"""


# class Father:
#     pass
#
#
# class Son(Father):
#     pass
#
#
# class GrandSon(Son):
#     pass
#
#
# Darry = Father()
# Garry = Son()
# Lorry = GrandSon()

# print(Darry.Cricket)
"""
After the inheritance chain is done, Python interpreter will show a sign of inheritance before the parent classes. Son 
is subclassed by GrandSon whereas "Father" is subclassed by "Son" and indirectly by "GrandSon" too.

You might have known that whenever a child class inherits from parent class, child class is automatically enable to use 
properties and function of it's parent class. The same will happen here. Even though Son can access "Father"'s values, GrandSon 
can use "Son" and "Father"'s values as well.
"""
# Magic of multi-level inheritance :-

"""
Suppose Father has an attribute of "basketball" which is assigned a value "1". In son, the same variable is used,i.e 
Overriden and is provided a value of "2". Meanwhile, In GrandSon, the variable has a value of "3". We are exmining here 
that what will GrandSon do if we erased the variable from it's class.    
"""

# class Father:
#     Basketball = 1
#
# class Son(Father):
#     Basketball = 2

#
# class GrandSon(Son):
#     Basketball = 2

#
# Darry = Father()
# Garry = Son()
# Lorry = GrandSon()
# print(Lorry.Basketball)

"""
In the first attempt of printing Lorry.Basketball, we will get the exact value of variable as declared in class "Grandson".
If we erased the variable from Grandson, then Lorry will find the variable in parent's class. As "Son"is the first parent
to "Grandson", the value displayed will be from class "Son". If we erased Son's value too, then Lorry will recover the 
value from "Father" and will display it as output. 

The reason behind this chain of inheritance is effect of Multi-level inheritance and overriding "Basketball" variable. 
As I have already stated that, whenever a class is asked to print a class variable, it always looks for the value in the 
current class first and then in it's primary parent, i.e first parent to inherit the class.
Overriding variable is because when a declared variable is declared again in a class, it overrides the value of the first 
copy of variable. Because of Overriding, Python disables the override variable from being used by any user and suggests the
user to use the new value everytime. Simply in the above code, we have override "Basketball" two times and hence, we were 
unable to print the previous value of "Basketball". 

The exact mechanism is applied when a inherited class re-declares a function present in it's parent class. Thus, the user 
finds it unable to use function from parent class and will end up providing similar function from child class. 
"""

# Parent class using attributes from Child class-
"""
Though Child class are able to use attribute/functions from parent classes, parent class can't use attribute/functions from
child class. This is because Parent class aren't inherited which makes them unable to access other classes.  
For Ex:- Let's try to print a variable from class "Grandson" through "Father".
"""

class Father:
    Basketball = 1

class Son(Father):
    Basketball = 2
    Cricket = 6

class GrandSon(Son):
    Basketball = 2
    Cricket = 5
    Squash = 5


Darry = Father()
Garry = Son()
Lorry = GrandSon()
print(Darry.Cricket)

"""
As I have stated above, "Darry" won't be accompanied by cricket which is a separate variable in GrandSon. Even if the user 
tried to print Cricket with Father manually, python will give an error for not acknowledging the value in the class. 

The error will be :- AttributeError: 'Father' object has no attribute 'Cricket'.

"""
# Exercise :-

class Electronic_gadgets:
    Electricity = 1

class Pocket_gadget(Electronic_gadgets):
    Electricity = 1
    portability = 2

class Phone(Pocket_gadget):
    Electricity = 1
    portability = 2
    reliability = 3
