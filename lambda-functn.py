# lambda-function :-
"""
Lambda function is also called as one-liner function. It is as same as user defined function. It does not need multiple
lines to initialize. It could be called as a shortcut to initiate lengthy functions quickly rather than creating user defined
functions every-time.
"""

# lamder = lambda a, b: a - b

# print(lamder(1, -1))
"""
The above expression is the normal syntax for lambda function. For lambda function, you must have a variable to assign 
lambda function and desired number of arguments in the actual function. 
After declaring arguments, you must provide a condition after the "colon( : )" symbol. You can give a condition like a + b,
a - b, a /b or anything else.

For Ex:-   
"""

# def getlamder(a, b):
#    c = a + b
#    return c

#           OR


# def getlamdder():
#    c = int(input("Enter first number:-"))
#    d = int(input("Enter second number:-"))
#    F = c / d
#    print(F)


# print(getlamder(23, 45))
# getlamdder()

"""
while a user defined function required 2 or more lines, lambda function used only a single line to explain the condition
to respective function. Both produce same result but lambda function acquires very much small space compared to normal 
user defined functions.

Lambda function is useful when the user wants to perform small tasks like addition, subtraction, Multiplication, squaring,
cubing much quickly. Lambda function do not appear more functional when it comes to huge code and complexity. 
"""

# Sort-function in lambda expressions:-
"""
Sort function takes a function as an input with a "key" as an argument. 'key' is a part of sort function which takes user 
defined functions as an input.

note:- Sort function only works for lists and not for other collections.
"""

# a = [[1, 4], [32, 2], [5, 34]]
#
#
# def adder(a):
#     return a[int(input("Enter the index:-"))]
#
#
# a.sort(key=adder)
# print(a)

"""
Here, first of all, list 'a' was created in which group of two numbers were stored in three lists respectively. Later, A
function named adder is created with 'a' as an argument and then a statement is added into it regarding to present the numbers 
in ascending order. It is ordered to be in ascending order because of the sort function. In function, return [1] or [0] 
means the list will display the character present at index 1 or 0. In list 'a', there are 3 lists inside the list. So, 
the function will present each character present on position 1 or 0 from each list and arrange the lists in ascending 
order according to the lower to greater order.

In above example, a = [[1, 4], [32, 2], [5, 34]]. After execution of program, the list will call the function. As the 
statement asks list to return [0] means 0th position element of all lists, the list will compare the 0th position of 
each list with each other and will represent the result like this:- [[1, 4], [5, 34], [32, 2]].

As you can see, the list with lower 0'th element is brought forward while greater elements than the previous one has 
appeared later.

But when it comes to lambda functions, user do not need lengthy text . In lambda-functions, you just need to enter the 
whole lambda equation as an argument to the "key". 
For Ex :- 
"""

b = [[1, 5], [5, 61], [66, 23], [22, 34]]
# b.sort(key=lambda x: x[0])
# print(b)


"""
In the above example, We tested lambda function with sort() to observe the conclusion. To proceed with a lambda equation 
we must define a variable and then the index which we want to sort. Thus the final equation is "lambda x: x[1]".

The reason for inserting a lambda equation at a time is that , the sort function's key needs a function as an input. As 
we were using lambda function which was not callable, we directly assigned the complete equation to key. In the equation, 
we also assigned wanted index as variable 'a' was separately assigned with the value and then was executed into sort(). 

Besides entering the whole equation into 'key', You can try assigning the equation to a variable and then assigning the 
variable to 'key'.
For Ex:-         
"""

Equator = lambda x: x[1]
b.sort(key=Equator)
print(b)
