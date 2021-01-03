# Self and __init__() functions:-

"""
Self is used to specify the arguments. Self keeps the ability to automatically access anything without calling the function.
"""


# class Officers:
#     Pension = 15000

#     def printdetails(self):
#         return f"Employee name is {self.name}.\nEmployee's post is {self.post}.\nEmployee salary is {self.salary}\n  "
#
#     def __init__(self, name, post, salary):
#         self.name = name
#         self.post = post
#         self.salary = salary


# Mukesh = Officers()
# Ramesh = Officers()

# Mukesh.name = "Mukesh"
# Mukesh.post = "Senior manager"
# Mukesh.salary = 40000

# Ramesh.name = "Ramesh"
# Ramesh.post = "Personal Assistant"
# Ramesh.salary = 30000


# print(Mukesh.printdetails())
# print(Ramesh.printdetails())

"""
In the above function which is printdetails(self), self stands as a common representative prefix for any object. Whenever 
an object is called with printdetails() function the representative prefix will get replaced by the particular object.
As per the above code, If we call function with object "Mukesh", then the function will return "Mukesh.name" and "Mukesh.salary"
simultaneously.

Note1 :- If the corresponding object or variables do not exist, then python will throw an error. Make sure to check everything
         before making a function call. 
         
Note2 :- As this topic is about self function we used it as a common representative for any object called along with the 
         function. But you can anything else in it's place rather than "self" everytime. For Ex:- element, yourself, etc.         
"""

# Constructor and __init__() function :-

"""
The method of giving arguments to the class is called as a constructor. As you can't directly insert any property into 
an object and you need to present them through constructor, init() function is used.
Ex:-

"""

# Salman = Officers()
# Shahrukh = Officers()

"""
Salman and shahrukh are the objects here which are created using class constructor, i.e Officers(). If we use class constructor 
to enter properties directly into object Salman, then it will give an error. It is because even if Officers has a paranthesis
but still the class isn't addressed by the user to accept any type of arguments and thus, class will give an error after 
failing to find a common representative of that argument. To let the class accept arguments from user, __init__ function 
is used.
"""
# Creating an init function in class Officers :-


class Officers:                              # Class creation without any arguments
    Pension = 15000                          # Class variable

    def __init__(self, Rename, Repost, Resalary):  # This function will take values from an object and assign the values as received.
        self.name = Rename                         # here, name is a instance variable and Rename is the argument received
        self.post = Repost                         # from user whose value is going to assign to the object-variable pair.
        self.salary = Resalary


"""
Here, the init function is declared inside class Officers. We have created the first __init__() function which will work 
as a constructor whenever user will operate it with an object. here,  

self --> self is an argument which will be used by init() to identify the main object of the class to which user wants 
         to assign values. It is a representative of the under-construction object. For Ex:- If Ramesh is the object, then 
         self will represent him and values will be assigned to it afterwards.  

name --> "name" values is assigned to instance property. Whatever values is a assigned to instance's propert or variable, 
          will be the new value of that property. "Self" will represent object and name will represent it's variable or 
          property. Rename will be the argument which will be the messenger of value from user to the object-instance pair.
          
Salary and post --> both properties follow the same mechanism as first property "name".

To apply this function, ou don't need to call it. You just need to declare an object with class constructor and then write 
corresponding arguments similar to the representative arguments user have set in the init() function. 
              
Ex:- We will take sarvesh as object and then will assign value.              
"""

# sarvesh = Officers("Mr.Sarvesh Kumar", "Clerk", 15060)

"""
In the above statement, 
1. Sarvesh is the object we have created using Officers() constructor.

2. "Mr.Sarvesh Kumar", "Clerk", 15060 will stand for the representative arguments Rename, Repost and Resalary in init function 

Now you can easily check the assigned values to the properties of instances.
"""

# print(sarvesh.name)

"""
The above print statement will be acknowledged by the value and will print it. The main question is when we didn't called
init function how did the values were updated or printed accurately? The answer is still constructor's abilities.

When we declared object "Sarvesh" through class constructor and added arguments inside it, Class Officers looked for a 
function who will take the arguments and store them. here, init function was the function which was used to receive arguments 
from user without giving any error like "No arguments in the function but 3 were given".

The advantage of init() function is that you can ultimately assign values to the particular properties whenever a user creates 
an object and creates object-variable in it. 

The init() function saves a lot of time which would have been wasted mercilessly on creating object, creating variables 
and then assigning them values again and again. As all this schedule is fixed into init() function, User needs to just 
declare an object using class constructor and then fill up class constructor's parenthesis.       
"""


