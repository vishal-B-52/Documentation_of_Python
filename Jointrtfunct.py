# Join function :-
"""
Join function is used to bind words together either it could be a set or collection of few words. Join function is useful
rather than using a for loop to combine a line of words together. Join function requires separate variable, word which
user wants to combine with other words, join function and printing the variable to which join function is assigned.
"""

# Using for loop :-

lister = ["Vishal", "Bawane", "12", "45", "Falcon", "Terrea"]

# for x in lister:
#     print(x + " or", end=" ")

"""
The above loop did exactly whatever I meant to do. For loop checked every element of lister then it added argument at 
place of x with "or" and 'end =""' function made sure that the for loop wil go in a straight line. Indirectly, for loop 
required two lines to manipulate the given condition. Hence, Join function is used to bring an ease in this types of tasks. 
"""

# Using Join():-

Contemplater = " and ".join(lister)
print(Contemplater)

"""
Join() function required only one line to define the exact result while for loop required two lines to define and then order
function to work as depicted code. 

Both function and the loop work similar but it is dependent on user about what he/she wants to use in the code. The rest 
is about reliability and flexibility of code. 
"""