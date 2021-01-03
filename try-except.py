# Try - Except condition :-
"""

It is a conditional statement. They are used for error handling. It works like error in first line then it will
continue program with the second statement. It has a very good use that you can continue program further witout any
internal error.

Other than "try" and "except", "except(like elif)", "else", "finally", "Exception with error" and "raise Exception can be used"
in error handling.

"""

# Try and Except :-

"""
The try block is used to detect incoming errors. When try senses any error it passes it to the except block to handle it.
If any error is not detected, try will execute a statement in it.
"""

# num1 = 23
# num2 = "Vihsal"
#
# try:
#     print("The result is ", num1 + num2)
# except:
#     print("The addition failed but the program continues")

"""
In above program, we used two variables of type int and chose them to add together in try block. In try except conditions, 
we have decided to give an exception if both variables failed to sum up and the program will continue to run without obstructing 
its flow. 
Being 'int', Both variables will sum up without raising any type of error. As try block has been successfully executed, 
except block's statement will be ignored and result will be printed.
 
Now let's change type of one variable. We can observe that the result is not displayed because Python does not permit an
"int" and a "string" to be summed up. It wil raise a TypeError due to unsupported operand of '+" between different datatypes. 
This will indirectly obstruct the program from going further(if any further code is remaining to execute). 

Due to Except, The error will be handled by user in one sentence , i.e "The addition failed but the program continues." 
Although the error has occurred, Program wi;ll still be able to progress and run remaining code providing complete results.
"""

# Many Exceptions:-

"""
Python allows you to use as many as "Except" blocks to handle various errors. It proves to be useful to handle 'NameError',
"IndexError', "IndentationError", etc.

Except allows us to choose the type of error like TypeError.
For Ex:-
"""

# num1 = 23
# num2 = "Vihsal"
#
# try:
#     print("The result is ", num1 + num2)
# except TypeError:
#     print("The addition failed but the program continues")

"""
As any TypeError will occur, it will be handled through the "except 'TypeError' block(as it is made for it). Alike TypeError,
other errors can be handled through separate except blocks with proper actions.  
"""
# Else :-

"""
try block proves to be useful for sensing an error while except handles it. here, Additional 'Else' block can be used to 
acknowledge a user to continue program if no error has occurred along with respective result of previous code. The 'Else'
block would not execute if error occurs and is handled by except block.

E.g:-
"""

# num1 = 23
# num2 = 34
#
# try:
#     print("The result is ", num1 + num2)
# except TypeError:
#     print("The addition failed but the program continues")
# else:
#     print("All is Well")


# Finally :-
"""
Finally block is a block which is tend to be executed in any condition whether there is an error or not. The content in finally 
will display along with "try"'s result and 'Except''s exception. 
"""

# num1 = 23
# num2 = 34
#
# try:
#     print("The result is ", num1 + num2)
# except TypeError:
#     print("The addition failed but the program continues")
# finally:
#     print("This string is not limited.")

"""
finally can be used in some cases where safety of the code will be carried first and then other things.
For Ex;- A user must close a file after opening it.
"""


# try:
#     f = open("demofile.txt")
#     f.write("Lorum Ipsum")
# except:
#     print("Something went wrong when writing to the file")
# finally:
#     f.close()

"""
Using finally, User can close the file even if an error occurs. Thus, it provides necessary safety to save done work in 
the file. 
"""

# Raise Exception-
"""
Being a python developer, You can raise exception when a specific condition is reached or entered into the interpreter. 
It is useful to raise objection on specific conditions which you don't want to be tested in the interpreter.
To raise exception, use 'raise' keyword and specify the wanted condition in it.

For Ex:- I don't want any number greater than 10000 to be included in a variable:-
"""

# x = 125567
#
# if x > 10000:
#     raise Exception("Sorry no number greater than 10000 is allowed")

"""
Here, 'X' was the variable to which limit was applied. The limit was that ,the'x' can take a number only upto 10000 else 
the value will not be considered and error will be shown. Here, the erro was as follows :-

Traceback (most recent call last):
  File "C:/Users/admin/PycharmProjects/PythonDay/try-except.py", line 133, in <module>
    raise Exception("Sorry no number greater than 10000 is allowed")
Exception: Sorry no number greater than 10000 is allowed 

with defying limits, You can either set a variable for a specific datatype only. Like X for int, y for float and z for str.
For Ex:- We can set a condition where 'x' is not permitted to accept a string value.
"""

# x = 3 + 2j
#
# if type(x) is str:
#     raise Exception("Error!! You are not allowed to enter a string value.")

# Raise in Error defination:-
"""
As Raise is used to raise error in specific conditions, It can be also used with main Errors in Python. The error could 
be a NameError, SyntaxError, etc.

For Ex:- If 'x' is not defined in code, then NameError will occur. 

"""

# try:
#     print(x)
# except NameError:
#     print("X was not found!!")

"""
In the above example, X didn't exist but still we tried to print x and gained a NameError regarding 'x' is non-existing 
in the code. In except NameError block, NameError was set as the condition in case the variable didn't exist, NameError 
will be displayed. If NameError occurs , except block will execute and display the assigned statement notifying about 
NameError to the user.

Alike NameError, Other error can be used as well along with except condition.
For Ex:- 
"""
# 1. IndexError - raises when interpreter cannot find item with entered amount of index.

# lister = [12, 43, 56, 77]
#
# try:
#     print(lister[4])
# except IndexError:
#     print("The list do not have item of concurrent index.")

# 2. KeyError :- raises when a non-existing key is entered.

# dictator = {"Vishal": "A word with 6 letters", "34": "A number comes after 33 and before 35"}
#
# try:
#     print(dictator['5'])
# except KeyError:
#     print("Such key does not exist.")

# 3. ImportError - raises when a non-function function is imported.

# try:
#     import vishal
# except ImportError:
#     print("The above module does not exist.")



