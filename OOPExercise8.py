# Single leveled Inhertance -
"""
Single level inheritance means deriving a class from an existing class. The derived class is called as the child class or
inherited class whereas the source class from which child class is derived is called as base class or Parent class.

The inherited class has an advantage of inheriting all the variables, properties and functions of parent class after derivation.
Due to the inheritance, all the codes and functions are shared to the derived class which automatically enables the child
class to use them in their own codes.

The changes made in variables of parent class can change the value of variables of child class but changes made in child
class can't change the value of Parent class.
Ex:- Deriving class"Seniors" from parent class "Officers".
"""


class Officers:
    Pension = 15000

    def printdetails(self):
        return f"Employee name is {self.name}.\nEmployee's post is {self.post}.\nEmployee salary is {self.salary}\n "

    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary

    @ classmethod
    def return_args(cls, string):
        return cls(*string.split("-"))


# Mukesh = Officers.return_args("Mukesh-CEO-15000")
# Ramesh = Officers.return_args("Ramesh-Senior Clerk-14000")


# class Seniors(Officers):
#     @ classmethod
#     def Pension_value_Converter(cls, value):
#         cls.Pension = value


# Mahadev = Seniors("Mahadev", "Senior Manager", 25000)
# print(Officers.Pension)
# print(Seniors.Pension)
# print(Mahadev.Pension)
# Mahadev.Pension_value_Converter(200000)
# print(Officers.Pension)
# print(Seniors.Pension)
# print(Mahadev.Pension)


# class Seniors(Officers):
#      @ classmethod
#      def Pension_value_Converter(cls, value):
#          cls.Pension = value
#      pass


# Mahadev = Seniors("Mahadev", "Senior Manager", 25000)
# Bhojraj = Seniors("Bhoja", "Senior assistant", 25699)

"""
Here, we can clearly see that "Mahadev" and "Bhojraj" being objects of class "Seniors" are able to use init(0 function from 
class "Officers". Along with the functions, Seniors can use the class variable "pension" too.   
Ex:- Printing Pension from Seniors and Objects.
"""

# print(Mahadev.Pension)
# print(Seniors.Pension)

# Override and 'Super' keyword :-
"""
Overriding in OOP means violation of DRY(Don't Repeat Yourself) method. OOP respects and uses the policy of DRY which prevents 
user from overriding one statement multiple times.
Ex:- Using init() function as it is with smaller modification in class "Seniors". ALong with init(), printdetails() function 
has been override. The override methods are defined by a symbol before their declaration.
"""


class Seniors(Officers):
    @ classmethod
    def Pension_value_Converter(cls, value):
        cls.Pension = value

    def printdetails(self):
        return f"Employee name is {self.name}.\nEmployee's post is {self.post}.\nEmployee salary is {self.salary}\nEmployee works at {self.posting} "

    def __init__(self, name, post, salary, posting):
        self.name = name
        self.post = post
        self.salary = salary
        self.posting = posting


Mahadev = Seniors("Mahadev", "Senior Manager", 25000, "Thane")
Bhojraj = Seniors("Bhoja", "Senior assistant", 25699, "Virar")
print(Bhojraj.printdetails())

"""
Overriding may be the simplest way to use parent class features but as it thoroughly violates OOP's DRY policy, Python do 
not wants their users to follow overriding the codes. To avoid overriding, Python has a "Super" keyword which has the ability 
to call the constructors of parent class without copy-pasting anything. We are going to learn "Super" keyword in nearby 
future.  
"""

