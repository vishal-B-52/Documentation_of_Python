# Fibonacci series-
"""
Fibonacci series is a series in which previous number is added with next number to obtain further result.

"""


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 1)


number = int(input("Enter a number:- "))
print(fibonacci(number))