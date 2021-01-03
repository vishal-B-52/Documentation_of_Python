# Classes and Objects (Object Oriented Programming):-
"""
1. Classes :- Classes are template for creating objects. The objects created in the class are always associated in it
              whenever printed.

2. Objects :- Objects are also called as instances of the class a.k.a templates. They are created using constructor of
              the host class and can be accessed by class names or objects name associated with it using extension.

Note :- Classes are used to depict topic and objects to define the points of topic. OOP uses DRY method which is the
point of creating class.
DRY stands for Do not Repeat Yourself.
"""

# Creating a class and assigning objects and property to it :-


class Vishal:
    pass


age = Vishal()
std = Vishal()

age.x = 18
std.y = "12th"


# print(age)
# print(age.x)

"""
Vishal is the class created here. 'Vishal' has two objects and those two objects have one property each. 'age and std' are 
the two objects stated above. Both are created using constructor of the class. The constructor used in creation marks the
objects that they are associated with the particular function. 

when you print age and std directly, code will display the memory location of that object. It is the same memory location
where further provided results, values are stored. 

X and y are property of both objects which allow the both object to store the values they are provided with. 

The first print statement of the code will return the memory location of the specified object. The second and last statement
will return the value assigned to x property and will be redirected through age object. 

Note1 :- Undefined or declared objects are not authorized in python. if you try to print any object which is not created, 
interpreter will simply give an error because of un-acknowledgement.

Note2 :- Rather than strings, int and float value the object can even accept a list, tuple, set and any other collection 
         of elements. 

for Ex:-     
"""


class sorrow:
    pass


feelings = sorrow()

feelings.a = ["sad", "sadder", "saddest"]
# print(feelings.a)


