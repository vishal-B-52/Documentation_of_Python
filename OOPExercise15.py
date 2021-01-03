# Diamond Shape Problem -
"""
Diamond shape problem is actually a state of confusion where classes get confused about using methods of same name present
in another class.

Note :- Java does not supports multiple inheritance but python and C++ do support such inheritance.

Let's go through some examples to learn multiple inheritance.
"""

# Example:-
"""
We will create 4 classes here namely A, B, C, D. "A" will be a parent class of "B" and "C". On other side, "D" is a child 
class of "B" and "C" which is a perfect example of multiple inheritance. After creation of all classes and inheriting them
accordingly , We will assign a method to class "A" named, method(). Except A, no other class would have anything in them.
Then, Instances will be created and will be used to print the method from "D" class.
In order to see the inheritance strength of classes, we will steadily observe the results with a minute change everytime.  
"""


class A:
    def method(self):
        return "This is class A"


class B(A):
    def method(self):
        return "This is class B"


class C(A):
    def method(self):
        return "This is class C"


class D(B, C):
    def method(self):
        return "This is class D"


a = A()
b = B()
c = C()
d = D()

print(d.method())

"""
We have assigned a method to class 'A' and with each execution ,we are going to apply the same method on next 3 classes.

1. In the first illustration, No other class has method 'method()' other than 'A'. a, b, c, d are the instances of the 4 
   classes. In the end, we have selected instance 'd' to print method() function. Indirectly, we are seeing that whether 
   Python gets confused in selecting exact output as we wanted. After the statement executed, result shows the statement 
   of class 'A', which is correct. Being an instance of class "D", 'd' priority will go for 'D' first. As the wanted method 
   is not there, 'd' will climb up into class 'B' and 'C' due to their inheritance order as parent class. After then, 'B' 
   and 'C' do not contain the method, 'd' will go through "A" as it is the parent of 'B' and 'C' and then after method()
   is found, output will be given.   
   
2. In the second illustration, We will assign the same method to 'B' and 'C'. After the statement is executed, 'd' will 
   first look into it's class 'D' as usual. Upon not finding, 'd' will follow the inheritance order. In class 'D', we have 
   declared 'B' as the parent class which is eventually followed and 'd' searches for the method in 'B'. As method is present 
   in 'B', output will display the statement of method from class 'B'. Suppose method was not present in 'B' but in 'C', 
   then according to inheritance order, 'd' would have presented the statement from method of "C". In short, Python didn't 
   failed to acknowledge the accurate method from respective classes.
   
3. In the last illustration, We will assign method to class 'D'. Aftre statement executes, 'd' will easily find the method 
   in 'D' and respective method will be displayed as output. 
   

This all 3 illustration ,when combined, can create problem which is called as Diamond shape problem. The problem is called 
as Diamond shaped just because of the inheritance orders of classes. The diagram is as follows:-

                                                   ____
                                                   | A | 
                                                   -----  
                                                  /     \   
                                                /        \ 
                                              /           \
                                          | B |          | C |
                                               \         /
                                                \       /
                                                 \    /
                                                   \/
                                                      
                                                   | D |


As the inheritance forms a diamond, the problem was named on that basis.

Diamond shape problem isn't much affective for Python language as due to Python's syntax and resolution power, User can 
easily and without efforts beat the heading problem.

Diamond-shape problem is a real threat to languages like C++,etc. who gets confused in the inheritance mess-up and fail to 
provide exact output.Thus, many times a programmer is asked to avoid multiple inheritance from programs to prevent the problem.  
"""
