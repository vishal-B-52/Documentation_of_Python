# F-Strings
"""
String formatting is just like inserting a variable in a string.
"""
# 1. Very first method of String formatting-
# Me = "Vishal"
# He = "Rohan"
# a = "I am %s and he is %s" %Me #%He
# print(a)

"""
In the above code, '%s' was used to format the strings. Here, '%s' will represent variable value after the original 
variable is declared outside the specific string. For this method, One variable is used to indicate variable value and 
rest '%' symbol is used to substitute the real value. You can't use more than 1 variable in the string. You wil get an 
insufficient arguments error if you try to use two variables at a time.


In new methods, format() function is used for formatting the strings. It is used to gain ease and format with indexing.
"""

# a = "I live in {} and my name is still {}"
# b = a.format("Virar", "Unknown")
# print(b)

"""
# Using Non-variable values :-

In the above code, parenthesis were used to represent the parentheal value. Parantheal value means value inside format()
The parenthesis redirects the variable values according to the index position. The first ever parenthesis in the 
format-able string will represent the value of first ever value in the format() parenthesis. This method can be done by 
using variables and directly using the string values from format() parenthesis. 

# Using Variable value :- 

a.format will check the value and print them in sentence. The sentence will print the values on the basis of index number
In the sentence, there are two brackets having place secured from 0. 

b = a.format ("Vishal", "Unknown")

The two indexes will be then specified  according to positions. You can change positions or specify their index in brackets
for changing sentence.

Note:- In both conditions, a separate variable must be used to represent string's formatting and should not be used within 
the function. If the a.format() is print directly it will show no effect, rather than printing the statement exactly with 
parenthesis. Even after you assign variable 'b' with a.format() , print 'b' instead of 'a' as 'b' will give the wanted 
effects to the strings whereas printing of 'a' will print the exact statement only.  
For Ex:-   
"""
# Using non-variable values:-

# a = "For short {}, I fell from the {}"
# b = a.format("while", "cliff")
# print(b)

# Using variable value :-

# b = "while"
# c = "cliff."
# d = a.format(b, c)
# print(d)

# OR -
"""
You can enter index numbers in the parenthesis of formattable string and that's another way you can format a sentence. You 
can use multiple arguments to format sentence. The arguments should meet the equal number of parenthesis otherwise it 
will throw error for extra arguments. As well as, If you entered any index out of reach from original variables, it will
throw an error again. 
"""

# d = a.format(b, c)
# print(d)

# f-String -
"""
f-string stands for fast-string. In f-strings, 'f' character is stated before a string in which you supposed to insert 
variable values. f-strings does not take direct values but variable values which are indicated through mentioning curvy 
brackets.   
"""
# a1 = "Vishal"
# b1 = "Unknown"
# stringer = f"My name is {a1} but you are {b1}"

# print(stringer)
"""
The following string will automatically redirect the values of variables to the curvy brackets where the each variable 
is decoded.without curvy brackets, you can't add a variable into string. In F-string, you can easily swap variables or 
change values by changing variables.As well as , You cannot add variable values to the brackets so that variables will 
be redirected at the place. 

F-String has a unique advantage that the string can calculate a mathematical expression easily. You need to import a module,
use a function with wanted value and It will give you perfect result without any error. Not only a mathematical expression,
but you can use any module's function inside the curvy brackets.
    
"""
# import time
# neverevr = f"Here is the epoch time :- {time.time()}"
# print(neverevr)

"""
As you have seen in the above code, " Time " module was imported and then using time(), we have printed the epoch time 
since , 1 January 1970. You can try with a mathematical expression as well.
"""

# import math
# nevereeest = f"Here is the result of square root :- {math.sqrt(576)}"
# print(nevereeest)

"""
F-strings brigs additional pace to the variable and String combination. F-Strings is faster than adding each variable to
specific string. It saves much time.
"""
