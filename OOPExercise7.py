# Abstraction and Encapsulation:-

"""
Abstraction means breaking down a task into small pieces or co-tasks. Ex:- Computer is an abstraction because it is divided
into mouse, CPU, key-board, Hard-disk, RAM, etc. This co-tasks are also called sa layer of Abstraction. The combination
of all these components makes the PC a complete abstraction.
For EX:- here "MyComputer" is an abstraction and all the functions and variable are layers of Abstraction.
"""


# class MYComputer:
#     def CPU(self):
#         x = 14
#         y = 12
#         z = 20
#
#     def RAM(self):
#         x = 15
#         y = 19
#         z = 29
#
#     def Hard_disk(self):
#         x = 20
#         y = 30
#         z = 35


"""
It will be an irony to say that the PC too is a layer of abstraction. For Ex:- a server is handing many of the PC's of a 
particular area ata time. Here, Server becomes the abstraction and the PC become layers of abstraction. Now further I won't 
be able to tell that whether server is a complete abstraction or not. 
"""


class AllServer:

    def PC1(self):
        pass

    def PC2(self):
        pass

    def PC3(self):
        pass


"""
TO achieve complete abstraction, OOP suggests Encapsulation method. Encapsulation means hiding the details down of an 
abstraction. For Ex:- A Mouse of a PC. Most of the PC users won't know what lies inside a mouse though they know how it 
works to cover-up the basic needs. In simple words the unnecessary data of the element is filled up in a capsule and what
we learn is the outer core of the capsule. For EX:- Mouse is the capsule, which we know how and when to use but we don't
know how it functions from inside. The indirect definition of Encapsulation could be, Use the class but don't get messed 
up to look into it. From mouse's example, we learnt that Encapsulation is a process of hiding the details of implementation.   
"""

