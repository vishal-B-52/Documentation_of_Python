# Using *args -


# def myargs(*args):
#    print(*args)
#
#
# lister = {"Vishal", "Rohan", "Aakash", "Suresh"}
# myargs(lister)

"""
Here, myargs() function has *args as a reference to the arguments of any variable, variable value or user-defined function.
Here, print(args) means the function will read the arguments of specified object one by one. The '*' symbol in front of 
args defines that anything entered after it will redirect the object to this myargs() function and the function will
display the arguments in the object.

In the above example, lister is a list with some arguments or variable value in the list. Then, myargs() function is called
in which lister is assigned. Absence of '*' symbol will not create any havoc but it will change the view of displaying 
the arguments of lister. With '*' symbol, the any collection of elements will appear in a tuple. All the elements will 
be displayed inside a tuple. Without a '*' symbol, The result will show the arguments present inside a list in a tuple and 
a ',' outside the end of the pre-defined list.

Note:- The elements are not stationary and will keep changing positions even if they are in a non-mobile collection. For Example,
If you print result of above code, the list will keep changing like "Rohan Suresh Vishal Aakash", "Suresh Aakash Rohan Vishal"
and etc.

You can change the layout of the arguments by different methods:-
"""
# Make the arguments appear in a list or pre-defined collection-


# def myway(*args):
#     print(args)
#
#
# lister1 = {23, 44, 55, 66, 77}
# myway(lister1)

"""
After the code executes, the arguments will appear in the same type of collection in which they were earlier before defined.
If the collection is dictionary, set, tuple or list it will appear as the same. The difference of '*' symbol here is the
reason behind change. With '*' value in both function and function call, the by default set becomes tuple and erases the
pre-defined collection.  
"""
# Removing the pre-defined and by-default collections and symbols:-


def mytime(args):
    print(*args)


lister2 = (34, "Vishal", 54, "Rohan", 122, "Droper", "Chandu")
mytime(lister2)

"""
In above code, the variable is laced with tuple type collection and commas to separate arguments from each other. When 
the code is executed, the collection type will vanish along with other symbols inside it like commas, full-stop, quotes,
etc.
"""
# Using slicing in the function-
"""
You can slice or negatively-slice the arguments to get desired number of arguments.
"""


# def mynew(*args):
#    print(args[-4:])


# nowhere = (34, "Vishal", 54, "Rohan", 122, "Droper", "Chandu")
# mynew(*nowhere)
"""
When you slice it from positive direction ,that is [0 : 4] or anything you want, the slicing will print only 3 elements 
from the respective collection as it is common in slicing to ignore last element. In negative slicing, last element is always 
indexed as 1 and so, [-4:-1] will present you the last 4 characters.
"""
"""
This type of function can accept as much as arguments you have entered in it. It is more beneficial than a normal function
which allows the user to enter limited number of arguments.
"""


# def myold(a, b, c, d):
#     return a, b, c, d


# print(myold(12, 33, 44, 52))

"""
In above function, function allows the user to enter specific amount of arguments when called. Hence, this type of 
function will not allow you to update the limit of arguments automatically and will throw an error if the limit exceeds 
"""

# Use of for loop to read arguments inside the function -


# def mywork(*args):
#    for i in args:
#        print(i)


# listress = ["Vijay", "Abhishek", "Ketan", "Chetan", "manish", "Visram"]
# mywork(*listress)

"""
You can use a variable along with args and kwargs(in later part).
"""


# def mymoment(Var, *args):
#    print(Var)


# Jian = "Mai hu jian, Mai hu bada takatwar"
# mymoment(Jian)

"""
A user defined function always allow you to use three types of things in it's paranthesis. That is (var, *args, **kwargs).
Var means variable. Value of a existing variable can be redirected through it by entering the specific name of that variable.
Remember that you can't put var behind args as it will be un-suitable and a direct disturbance to the normal chain as given above.  
The chain always works like(var, *args, **kwargs) and you cannot change it. 

Args and Kwargs both are optional things which are dependent on user whether to use it or not.
"""

# KWARGS -
"""
Kwargs need dictionary to access values or arguments. Where as args can pick up any collection it is not all the same 
with Kwargs. Kwargs are assigned with 2 stars while args are only assigned with 1 star. You cannot print values of 
kwargs by simply using print() function. You will need two separate word to define the key and value present inside dictionary.
You can take words like "Key and value" or "a and b" or "egg and omlet" etc. to represent the key and values of a dictionary.
As well as, Kwargs.items() is a very useful function which will help you update the dictionary faster and without any. 
It is necessary for the code     
"""
# dictionary = {"Vishal": 30003, "Aakash": 5000, "Rohan": 20000, "Prajyot": 25}
# list = ["Vishal", "Me", 54, 1, 'd', 3.44, "\n"]
# Meme = "School trip fees -"


# def myfunct(Var, *args, **kwargs):
#    print(Meme)
#    for i in list:
#       print(i)
#    for g, d in kwargs.items():
#        print(g, d)


# myfunct(Meme, *list, **dictionary)

"""
You can use anything instead of actual word "args" and "Kwargs". But you must keep the number of stars the same on each
representative's head. It is must to keep 1 star on args's head and two stars on kwargs's head for reference purpose. 
"""

# my = "I my name is Vishal not bawane"
# formatter = ["I", "do", "not", "format!"]
# Dicter = {"Friend": "Known", "Virus": "Corona", "Pateli": "Prajyot", "Show": "Shatayupathy"}
#
#
# def mytime(Var, *nort, **norton):
#
#     for x in formatter:
#         print(x)
#     for a, z in norton.items():
#         print(a, z)
#
#
# mytime(my, *formatter, **Dicter)
