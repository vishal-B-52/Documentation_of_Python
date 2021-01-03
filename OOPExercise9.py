# Multiple Inheritance -
"""
Multiple Inheritance means inheriting a class from two classes . The inherited class contains an ability which allows it
to gain a direct access to the attributes of it's parent classes.
For Ex:- I have inherited 'Expert' class from 'Seniors' and 'Juniors'.
"""

class Seniors:
    Pension = 20000

    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary

    def printdetails(self):
        return f"Employee name is {self.name}.\nEmployee is on the post of {self.post}.\nEmployee gets {self.salary}per month."

    @ classmethod
    def String_to_Args_Converter(cls, string):
        return cls(*string.split("-"))
#
#
class Juniors:
    no_of_leaves = 4
    Pension = 25000
    def __init__(self, aname, apost, attendance, projects_given):
        self.name = aname
        self.post = apost
        self.attendance = attendance
        self.projects_given = projects_given

    def detailprinter(self):
        return f"Employee name is {self.name}.\nEmployee is on the post of {self.post}.\nEmployee has registered a {self.attendance} days" \
               f" attendance this month.\nEmployee is currently handling {self.projects_given} projects.\n"
#
#
class Expert(Seniors, Juniors):

    Pension = 15000


# Bheem = Seniors("Bheemsen", "Manager", 22000)
# Suyodhan = Seniors("Duryodhan", "Secondary Manager", 21599)
#
# Duhshasana = Juniors("Dushasana", "Personal Assistant", 29, 4)
#
Arjun = Expert()


"""
We have created 3 classes above here. First class is "Seniors", Second class is "Juniors" and the product,i.e Child class 
of both class is "Expert".According to the simple theory of inheritance, Expert is allowed to use attributes/Functions of both
parent class. 
"""

# Importance of Inheritance order:-
"""
In OOP language, when a user inherits a class through "multiple inheritance" the order of inheritance of parent classes 
matters the most. In above code, Expert is inherited first by "Seniors" and then by "Juniors". The advantage of declaring 
a class first in multiple inheritance is that the child class will always look for the available attribute/function in that 
class if it is not present in itself. 

Let's resolve it again through simple examples. Here, Arjun is an object of "Expert". Expert does not have any function or
constructor to give arguments and assign them to the automade properties of Arjun. Even though Expert didn't have had any 
constructor, Arjun managed easily to pass arguments and assign values. You might have known that both parent classes have 
one constructor each. From two constructors, Arjun used the init() constructor of "Seniors". 

"Arjun" reached Seniors first because Seniors was the class which was declared first during making inheritance. You can 
assume this statement as the reason to the question "Why Arjun didn't chose Juniors to get a constructor ?". Just because 
"Seniors" was the first parent, "Arjun" used init() constructor of of "Seniors" to break down his arguments and assign to 
different properties.    

The inheritance order of parent classes is free choice for a user that whether the user wants "Arjun" to go through "Seniors" 
constructor or "Juniors" constructor.

You can chech what type of constructor(Seniors or Juniors) you have set just by creating an object with the class constructor 
and then executing the unprintable object. 
For Ex:- I will create an object and then print it. Python will give an error as the required arguments are not filled which
the interpreter will show. Then you can compare those arguments with respective constructors to see the main constructor. 
"""
# Veerendra = Expert()

# Selecting Class variable:-
"""
Suppose we have written a class variable 'var' in "Expert". To create a confusion for object "Arjun" on selecting 'var''s 
value we will override the same variable in it's parent classes.
"""

# class Seniors:
#     Pension = 20000

    # def __init__(self, name, post, salary):
    #     self.name = name
    #     self.post = post
    #     self.salary = salary
    #
    # def printdetails(self):
    #     return f"Employee name is {self.name}.\nEmployee is on the post of {self.post}.\nEmployee gets {self.salary}per month."
    #
    # @ classmethod
    # def String_to_Args_Converter(cls, string):
    #     return cls(*string.split("-"))


# class Juniors:
#     # no_of_leaves = 4
#     Pension = 25000
#     # def __init__(self, aname, apost, attendance, projects_given):
    #     self.name = aname
    #     self.post = apost
    #     self.attendance = attendance
    #     self.projects_given = projects_given
    #
    # def detailprinter(self):
    #     return f"Employee name is {self.name}.\nEmployee is on the post of {self.post}.\nEmployee has registered a {self.attendance} days" \
    #            f" attendance this month.\nEmployee is currently handling {self.projects_given} projects.\n"

#
# class Expert(Seniors, Juniors):
#
#     pass


# Arjuna = Expert()
# print(Arjuna.Pension)

"""
To see what Arjuna selects after same variable is declared in all 3 classes, we will write a "Pension" variable with different 
values. When Arjun prints variable for the fisrt time, surely he will check for the value in it's class first. If the value 
is not present in it's class, then Arjun will look for the value in "Seniors" raher than "Juniors". After Arjun finds value, 
it will be displayed as Output.

The question remains that "Why didn't Arjuna look for the value in Juniors than Seniors ?"

The answer is again class declaration order. As "Seniors" sttod first in inheritance parenthesis of Expert, any other object 
of Expert class will always give a priority to "Seniors" and then "Juniors"(if the required thing is not present in "Seniors").

Note :- If you want "Arjuna" to provide priority to "Juniors" first then the user must revert the order we have set in Expert.
        The new order must be Expert(Juniors, Seniors) which will help you get the desirable things. 
        
Note :- Reverting down the inheritance order after writing a code, may affect your code, constructor, attributes and selected 
        methods. 
        For Ex:- As you have changed the priority of parent class, "Arjuna" will go through constructor of "Juniors" to 
                 settle down it's property values according to the needs of "Juniors" of constructor. If there is any difference 
                 between constructor of "Seniors" and "Juniors", then "Arjuna" may throw an error for not filling required 
                 arguments.               
        Proof :- Just like this 
        
        Traceback (most recent call last):
  File "C:/Users/admin/PycharmProjects/PythonDay/OOPExercise9.py", line 48, in <module>
    Arjun = Expert()
TypeError: __init__() missing 3 required positional arguments: 'name', 'post', and 'salary'


"""
