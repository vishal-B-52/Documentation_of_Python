# Abstract class and Abstract methods :-

"""
Abstract class is actually a blueprint  from which classes and their methods can be created. Abstract base class can be
used to set rules for the inherited classes or child classes. Using abstract base class, user can easily set condition for
it's child classes.

Suppose a user wants the child classes ,inherited from a particular parent class, to compulsorily follow some conditions
depicted in it's parent class. Abstract base class are made for this purpose. As I said, An abstract base class works like
a blueprint for child classes, any declaration of attribute/method/function in the abstract class automatically enforces
the child class to use the same attribute/method/function in their class.

If a child class does not follow the implementations of abstract class, the child class will not be allowed to create any
object as a punishment.

To make a class an abstract class, User must import module 'abc' and then use "ABC, abstractmethod' from it.

1. ABC means abstract base class. You can declare a class as an abstract class just by writing ABC in the class's parenthesis.

2. abstractmethod is the decorator,just like classmethod and static method, which will make an attribute/method/function
   abstract and compulsorily implementable for all those classes which are derived from parent class.

Let's create an abstract class and set a method inside it using abstractmethod decorator.

Note :- You can use either ABC or ABCMeta or Metaclass to declare a class as an abstract base class.
"""

from abc import ABC, abstractclassmethod


class Office(ABC):
    @ abstractclassmethod
    def attendance(cls):
        pass


class Junior(Office):

    name = "Dharmesh"

    def __init__(self):
        self.post = "CEO"
        self.salary = 35000

    def attendance(cls):
        return "Total attendance :- 22 days work/8 days leave"


emp1 = Junior()
empstar = Office()

"""
In the example, abstract class and it's method implementation is defined. 'Office' is the ABC(abstract base class) while 
'Juniors' is the child class of it. Being a child class of 'Office', 'Juniors" will be enforced to implement the abstract 
method of parent class. attendance() is the abstract method here which class 'Juniors' must write into them. 

Not only 'Juniors' but ABC can enforce it's methods on all of the classes which are inherited from 'Office'. It will be 
'must' for the child class to use the method attendance() in their class even if they do not need it.

In the above code, the derived class are allowed to enter whatever the content they want to enter in the attendance() as 
the original abstract method contains only 'pass' and not any proper syntax. Thus, 'Juniors' have decided to return a string
which contains info. about Employees's days of work and leaves.

If the child class does not follow abstract class, i.e if the child class does not implements attendance() in their own 
class, then ABC will not allow child class to create any object and will throw error as a sort of warning. The error will 
clearly address user that child class has not obeyed ABC's conditions and implementations.  

Note :- One cannot create object/instances of an abstract base class. 
"""

