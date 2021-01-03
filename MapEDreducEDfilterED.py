
# Introduction to functions map(), filter() and reduce() :-

# ======================== map() =================================
"""
map() function is used when the user wants to apply a function on a specific list. Map function takes ony two arguments
:- 1.The Function which you want to apply on the list.
2. The list itself.
Map function can be used in place of For loop to reduce code-work and efforts.
Ex :-
"""

# 1. Using for loop -

# Collect = ["3", "45", "66", "57", "33"]

# for item in range(Collect):
#     Collect[item] = int(Collect[item])

# Collect[1] += 5
# print(Collect)
"""
In above code, Collect is a list with string elements. The task is to convert all the string arguments into integers and
the print the updated and converted list to ensure that the list is converted from type "string" to "int".

for loop is used here top loop through each element present in Collect. "i" in the for loop will represent each element 
of the list. range function is used here because for loop will not accept objects in list for conversion into integers. 

Collect[i] = int(Collect[i}) :- will be an important step where conversion of data-type will take place.

Collect{2} += 5 :- It will address the list to add 5 to the element at second index or third position as the first element
in list represents Collect[0].

print(Collect) :- Data-type converted list will be displayed.   
"""

# Using map() function :-

Collect = ["3", "45", "66", "57", "33"]
Collect_updater = list(map(int, Collect))
print(Collect_updater)

"""
The above code didn't required much work instead of only one important step. In the middle step of second code, map is 
directed to return the output in list collection. Here, "int" is the function and "Collect" is the list on which "int" is
going to be applied and conversion of 'string' to 'int' take place.
 
If we compare the code of for loop with map(), we can see that the code of map() is very simple and logical than for loop.
We don't need to apply intense logic using for loop everytime if the user knows how to use map(). 

As map returns result in an object form,It is mandatory to lace map with either list or tuple so that the result will be 
presented in the respective collection. An example is given below. Print it to see the result.
"""

# tuplingConv = map(getch, tupling)
# print(tuplingConv)

# Using a User defined function in map() :-

# def getch(X):
#     return X**X


# tupling = (0, 1, 2, 3, 4, 10)
# tuplingConv = tuple(map(getch, tupling))
# print(tuplingConv)

"""
In above code, 
def getch(X) :- It is a function which will return square of a number when the specific number is entered. 

tupling :- tupling is a tuple with some integer elements inside it.

tuplingConv :- It is a variable used to update tupling by map() function. map() is given two arguments. First is the getch
function and second one is tupling on which getch will be applied after execution. 

print(tuplingConv) :- tuplingConv is asked to print as it is the variable which has the updated tuple otherwise printing 
                      "tupling" will display the normal and actual tuple.                         
"""
# Using lambda/anonymous/one-liner function :-

# setter = {2, 4, 6, 8, 10}
# setter_Conv = set(map(lambda a: a * a, setter))
# print(setter_Conv)
"""
In the above code, 
setter :- It is a set of some integer values.
setter_Conv :- This variable will assign the lambda function on setter as entered into the map() function. After complete
result is declared, set will be used to encase the result inside a collection to avoid formation of object or memory 
location.
print(setter_Conv) :- It will print the accurate result as the code is entered.

Note :- I,myself do not suggest you to use set as a encasement for results. set is a collection which do not have any fixed
        position of elements. The elements inside a set are random position changer and thus you would be able to get 
        accurate result but not accurate positioning. 
"""

# Using for loop and map together for complex codes :-

# def square(X):
#    return X*X


# def cube(Y):
#     return Y*Y*Y


# combiner = [square, cube]
# for i in range(1, 8):
#     value = list(map(lambda x: x(i), combiner))
#     print(value)

"""
def square() :- square() function will receive arguments from assigned set of elements and display square of the respective
                numbers in the assigned list.
                
def cube() :- cube() will receive arguments from assigned set of elements and display cube of the respective numbers in 
              the assigned list. 

combiner :- combiner is a variable which keeps a list in which square and cube functions are placed without call.

for i in range(1, 11) :- "i" is a common representative of each number iterating from defined range. range is used to fix 
                         a limit of 1 to 10 numbers. 
Value :- This variable is the important nad main step of the for loop and map() function as well. in map() function, two 
         arguments are given. lambda function possesses 'X' which means it can accomodate any functions when provided. Combiner 
         is the second argument given to map which contains both functions given above. When the for loop continues, square
         function represents "X" and it will continue till all the numbers from 1 to 10 are squared and stored in a list.
         After square(), cube function will start representing "X" and it will iterate through the given range ,until all 
         the numbers are cubed. 
         
print(Value) :- This will print the result and list in which squares and cubes of all numbers are present. 

Note :- Don't use set to handle map's result as it will mix-up all the result.                                                                                 
"""

#  ======================== filter() =================================
"""
filter() function is used to filter a collection of elements according to the will of user or a specific condition. After
using filter() with a condition, the set of elements will adjust itself in  that way and will represent result. filter 
function takes 2 arguments which are same as map(). You need to lace filter(0 too with a set, tuple or list to avoid result
in a objective form.
"""
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def number_identify(num):
#     return num > 5


# filterer = list(filter(number_identify, list_1))
# print(filterer)

"""
In the above code,
list_1 is a list with numbers from 1 to 10.
number_identify is a function which will receive arguments from list_1 ,compare them with 5 , put them in list if they 
are greater otherwise remove them if they are smaller than 5.
filterer will assign the function on list_1. after the execution is done, filterer will store the output in a list. 
print(filterer) will print the updated list.  

Note:- I you use map() in place of filter(), the output will display a list full of True and False. The boolean values 
       will address the numbers in the list_1. True means numbers is greater than 5 and False means numbers is smaller 
       than 5. 
"""

#  ======================== reduce() =================================

"""
reduce function is a function of module "functools". It can be only used when it will be functools is imported. reduce()
is useful in complicated mathematical operations like fibonacci series.

Note :- reduce does not needs list or tuple or set to handle the object form. As the result does not needs any list, it do 
not needs to be laced with the ocllection types. 
"""
from _functools import reduce
lister = [2, 1, 5, 7, 34, 5, 77, 100]
lister_Conv = reduce(lambda a, b: a + b, lister)
print(lister_Conv)

"""
In above code,
from functools import reduce - reduce is imported directly from functools to reduce efforts. 
lister = It is a list with some integer values.
lister_cov :- In this variable, reduce is given two arguments, that is function and list. lambda a,b: a+b will add 
              two elements simultaneously till the list ends. For Ex:- "2" and "1' are a and b .After addition means completion
              of main statement, "3" will be "a" and B will be 5. After addition, next a will be 8 and next b will be 7.
              
print(lister_Conv) :- It will print the output. It will display the sum of all elements in the list.                
"""
