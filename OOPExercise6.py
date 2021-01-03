# Static Method:-
"""
Static methods are decorators which work for normal functions. If the user do not wants to use "self" or "cls" or class-
method, then user must use static method functions.

As well as, If the user do not wants to use "self" in place of class, static method can be used.

Static methods are made from @Class-method decorator. Ex:- Print_em function in "Officers" class.
"""


class Officers:
    Pension = 15000

    def __init__(self, Rename, Repost, Resalary):
        self.name = Rename
        self.post = Repost
        self.salary = Resalary

    @classmethod
    def string_Converter(cls, string):
        # params = string.split("-")
        # print(params)
        return cls(*string.split("-"))

    @staticmethod
    def print_em(string):
        return f"This is not good ,{string}"


Mukesh = Officers("Mukesh", "Manager", 29999)
Ramesh = Officers("Ramesh", "CEO", 50000)

# print(Mukesh.print_em("Harry"))

"""
Static methods are used as a private function which will work only for the declared class purpose and not for any other 
variables or classes. To make a static function limited to a class, it should be declared inside the class. When a static 
function is declared inside a class, Instances , their properties and class variables are the only thing which can call 
the static function. After it is declared in a particular class, another class and it's properties will not be allowed to
call the static function. This might be a good advantage of using static functions.  

For Ex:- Object "Sarvesh" from Class "Office" can't call the function due to owner issue.
"""


class Office:
    pass


Sarvesh = Office()
