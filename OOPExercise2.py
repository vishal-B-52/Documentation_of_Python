# Instances and Class Variables:-


class Officers:
    pass


Mukesh = Officers()
Ramesh = Officers()

Mukesh.name = "Mukesh"
Mukesh.post = "Senior manager"
Mukesh.salary = 40000

Ramesh.name = "Ramesh"
Ramesh.post = "Personal Assistant"
Ramesh.salary = 30000

# print(Mukesh.post)
# print(Ramesh.salary)

"""
here, We are talking about instances or objects and their private properties. Here "Salary" and "Post" are both properties 
of both objects and after this properties are created, they have nothing do with the Class. Objects use property to assign 
values, store them and later, display them by fetching from memory location. Same property name can be used again and again 
in different objects without creating conflict or collision in ownership. 
For Ex:- Salary and Post are used in both objects to store respective values.
"""
Mukesh.post = "Senior manager"
Mukesh.salary = 40000

Ramesh.post = "Personal Assistant"
Ramesh.salary = 30000

# Using mutual property:-
"""
To make a property mutual, User must declare the variable inside Class ,so that Objects can simply use it as an extension 
and then use it as per the user wants to. We will first print the value of property using class as prefix.
Ex:- 
"""


class Officers:
    no_of_leaves = 2


# print(Officers.no_of_leaves)

"""
Here, no_of_leaves is a mutual property for the objects constructed through "Officers" class. If a user tries to print with
any different object, the output will be the same. 
"""
Rajesh = Officers()

# print(Rajesh.no_of_leaves)

# Changing value of class variable through an object :-
"""
A user cannot change actual value of class using an instance. Surely, a class value can be changed when class itself, is 
used as the prefix and then class variable as the suffix .
For Ex:-
"""


class YT:
    likes = 777


Carryminati = YT()
BB_ki_vines = YT()
# print(YT.likes)
Carryminati.likes = 1000
# print(YT.likes)

"""
You can see that, when user tried to change the actual value of class variable and then checked value again, class variable's
value remained the same. Instead of value of class variable, this step will change the value of class variable only for  
object "Carryminati". So, whenever class variable uses classname as prefix, the value will be 777 and when object "Carryminati" 
is the prefix, value will be 1000. Other objects will show the same value as class variable until their value is changed too.   
"""

# Using __dict__ :-

"""
If a user wants to get all the sort of information from a particular object and all info. about variables or properties 
used inside an object, then "dict" is best thing for it. After dict is used and print along with an object as prefix, the 
output shows a dictionary in which all the properties and their values will be enlisted. The properties will appear as "Key"
while their assigned values will be the "Value".
EX:-    
"""

# print(Mukesh.__dict__)


# Extras :-
"""
You can print a class with dict as well to know what is inside a class. It will show the class variables declared in it 
as well.
Ex:-
"""

print(Officers.__dict__)