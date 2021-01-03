# Types of Variables -
# Global variable -
"""
This type of variables can be used inside and outside of a function. There value will be always same bu it can be
changed by assigning new value to the same variable.
"""

# x = 7


# def getadd():
#     print(x)


# print(x)
# getadd()

"""
In the above code, x was assigned with value '7'. As x is declared outside the function, it becomes a global function 
which can be used inside and outside a function.
"""
# Local variable -

# y = 23


# def getadd():
#     y = 24
#     print(y)

# print(y)
# getadd()
# print(y)

"""
In the above code, Local variable is explained. Local or personal variable can be only used within a function, it cannot
change a value of global variable. The value of a local variable is only limited within a function while a global variable can be
used anywhere. That's why printing y gave value of 24 and calling getadd() printed value of local variable.
"""

# x = 56


# def getrrr():
#     x = 34
#     print(x)


# print(x)

"""
In above code, when code was asked to print x, the code will start looking for the variable in scopes.
scope means limit. Limit is decided by te type of variable. 

Global variable has an infinite limit so that it can be used after declaring once.
Local variable has a limit within the function so that it can be used only within a function.

When above code is executed, the code looks for the 'x' variable in both scopes. If it is fond in global variable, then 
local variable with same name is denied from any type of permission to change it or replace it.

If the code finds it in local scope, then there will be no matter it will be treated as global variable. It means it can
be used only within the function in which it is declared.

That's how availability of variables is decided.
"""

# def geterror():
#    x = 14
#    print(x)


#  print(x)

"""
In above code, use of scope defining is done. Here, X is local variable inside a function. In the end, again x is asked 
to print. The code will start searching for the scopes. There is only one x present which is present inside the function.
As the print function will look for global scope version of x, it will end up giving error. The error is occurred due to
absence of global version of x. If the code was asked to print the x inside function, then ther will be no error.
"""

# Converting a local variable into global -
"""
A Local variable can be converted to Global variable through Global function. The wanted variable should be declared 
along with global function inside the defined function. After declaration, feel free to increase, decrease or change the
value of variable. After you are done, call the function first and then print(a) outside function. The value of local 
variable will be changed to global scope. Then, no matter how many times you check it, bot the values will be same. 

It is must for the wanted global variable to be present as permission of changing value will depend on the permission 
by global variable x which will change local variable x into global scope. 
"""

# a = 22


# def converter():
#     global a
#     a -= 2
#     print(a)


# converter()
# print(a)

# print(a)


# Nested functions:-
"""
Making function inside a function is called as nested functions.
"""


# def getsofg():
#    x = 20
#    def getsub():
#        x = 23

# The types of variable and global declaration in nested functions is different.

def getadd():
    x = 20   # Local variable
    def getsub():
        global x
        x = 50   # Local variable
        print(x)
        getsub()


getadd()

"""
A simple nested function always includes a variable in local scope. In above code, the function inside function has 
requested global permission for variable x. After code is executed, code will look for existence of x as global variable.
As X doe not exist in global scope, code will fail fetch permission. So, indirectly it will deny the local variable from
converting to global. It is must for a function to keep both types of variables in case of global conversion. 
"""