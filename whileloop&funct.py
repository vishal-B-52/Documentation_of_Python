# Using while Loop

"""While loop is mostly same as for loop. But here we have to break the loop and increment it manually while for loop
does no requires it. """

# simple example for While loop

# i = 0
# while i <= 10:
#    print(i)
#    i += 1

"""The every statement matters in while loop. Initializing to 0 sets the initial value. Not doing it will 
stretch the program to - indexes. On other side ,Not incrementing will keep loop continuously repeating till infinite 
numbers. i = i - 1 is same as un-incrementing while loop but it will start loop in negative range"""

# Extending the initial variable
"""After you set the initial variable to zero, you can still extend it. But extending it will affect the final state too.
it will add the exact number to the final state as same you added in the start."""

# s = 0
# while s < 15:
#    print(s + 5)
#    s += 1

# Break Statement-

"""Break statement is used to break a loop from repeating itself after reaching desired condition"""

# N = 0
# while N < 15:
#    if N == 11:
#        break
#    else:
#        print(N)
#        N += 1

# Continue statement-

"""Continue statement is used to keep loop alive even after a specific condition is reached. It will iterate the loop 
till the specific stage, skip it when it comes and will continue from next stage to the destination. When continue key 
is used, the program will forget everything under the keyword."""

n = 0
while n < 10:
    n += 1
    if n == 7:
        continue
    print(n)




