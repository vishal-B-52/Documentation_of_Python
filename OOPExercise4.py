# Class Method:-

"""
Suppose a user wants to change the value of class variable, i.e pension through a function without overwriting it manually.
As we know, User can't change value of class variable through any instance. The variables's value can be only and only changed
by using class as the prefix and not any object. Even if object is used in attempt to change value of variable, the changed value
will be limited to the object only and not actual class variable.

To avoid such complexity, we are going to establish a class method or decorator which will easily allow us to use and change
the value of class variable.
"""


class Officers:
    dutytime = 15000

    @ classmethod
    def change_pension(cls, reduty):
        cls.dutytime = reduty


rajesh = Officers()
mahesh = Officers()

print(Officers.dutytime)
print(mahesh.dutytime)
mahesh.change_pension(20000)
# print(Officers.dutytime)
print(mahesh.dutytime)
print(Officers.dutytime)

"""
The function made with decorator classmethod easily allows us to change value of the class variable everytime. The only 
thing you need to do is just hit the class or object as suffix , then call function "change_pension", add paranthsis and 
then add wanted value inside those brackets. As a decorator, classmethods makes it easy for a user to modify the functions 
by it's will. In the above code,

def change_pension --> It is the host function which will be modified through classmethod.

cls --> cls is a common representative for a class whose variable is going to be modified by the user. here, cls represents 
        "Officers" class.  

Redutytime --> It is the argument which will take input value from user and will assign it to the actual class variable 
               and thus, value will be modified.        
 
cls.dutytime --> represents class.variable pair. Class and variable will take there places and then they are assigned the 
                 value of Redutytime 

This mechanism is applied when function is called with "Class" as prefix. The advantage of using this decorator is that 
along with Class you can change value of class variable by an object too which is already written up above in codes. The 
decorator recognises corresponding object as the associate to the class and then indirectly allows object to change the 
value.  
"""

