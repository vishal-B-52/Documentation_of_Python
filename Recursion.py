# Recursion -
"""
It means using function inside a function. Mostly like a loop formation.
"""


# def getstr(a):
#    print(getstr(a))
#    print("I am" + a)


# getstr("vishal")

"""
When you print it, it will display an error regarding recursion depth exceeding.When the function was called , it 
completes first time call, and prints "I am Vishal". But as the function was called inside function also, so it will keep
repeating only between first two lines and after some seconds , it will cross the limit of recursion. 
"""

# Using recursion -

# Creating a factorial function by iterative method-


# def factorial(a):
#    fac = 1
#    for i in range(a):
#        fac = fac * (i + 1)
#    print(fac)


# number = int(input("enter number:"))
# factorial(number)

"""

Mechanism of above code-

When the code is executed, it will ask you to enter the number. After entering a specific number, the function is called.
After the number is given as an argument, function will do the rest things as decided. variable 'number' is matched with
argument 'a'. The 'fac' is already set to 1. Value of 'i' will be assigned to the number you have entered for variable 'number'. 
The for loop will keep repeating till the numbers are multiplied till the value of variable 'Number'.  

This function is now able to give a factorial of a number to maximum 1000. As big as the number is entered, the more time
code will take to represent the result. But this function is an iterative and not recursive due to the use of 'FOR" loop
in it.

"""

# Recursive method-


def fact_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)


print(fact_recursive(7))

"""
The above code works as same as iterative method. Only thing that iterative method does not use if statements or calling
function inside same function. 
Mechanism-
when the function is called with specified integer argument, the function executes the code in a order. As per written, 
the typed number will be compared with the first condition. 0 and 1 have a factorial of '1'. If the number is 1, then 
the first condition will become true and result will be printed. If entered number exceeds '1', then it will enter else 
condition. In else condition, the result will be returned. The code following return statement will work as follows-
Ex:-
n = 5  # as it is greater than '1;, it will skip the first condition. In else condition the code will work as follows-

5 * fact_recursive(4) # as n = 5 then n-1 will be 4. fact_recursive() will remain until '1' appears in parenthesis 
                        because enough decrement of 'n' value will be degraded to '1'. As 'n' is 1, the first condition 
                        will be true and the fact_recursive will return 1 before stopping finally. 
                        As well as, fact_recursive's appearance will call the function again and again until n gets equal
                        to '1'. 
5 * 4 * fact_recursive(3)  # as value of n is not '1' still function will keep going on.
5 * 4 * 3 * fact_recursive(2)                       
5 * 4 * 3 * 2 * fact_recursive(1)
5 * 4 * 3 * 2 * 1 # as 'n' is equal to 1, the loop will break and value of fact_recursive(1) will become equal to 1. 
                    After that code will calculate the multiplied value and present the result. 
120 # Final result.

"""

"""
Note - 
If you are using return in the code, then you need to print the called function. If you did not print it, code 
will execute but it won't display the result. 

Ex:- print(fact_recursive(6))

If you are not using return, you do not need to print the called function. The function will still print result even if 
you call it. 
"""