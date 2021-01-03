# Getter, Setters and Property Decorators :-

# Property Decorators :-
"""
Property decorator is a built-in decorator which defines the properties of functions without manually calling them, i.e
via parenthesis.

To reach this feat we are going through a huge example.
"""

# Beta example -
"""
we wil create a class 'Office' here. The class will have an init(0 constructor containing  2 arguments at first. printdetails() 
function, when called, prints complete information of the object. Two instances will be there too. 
"""


class Office:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"Email of Employee is :-{fname}{lname}@gmail.com"

    def print_details(self):
        return f"Employee's name is {self.fname} {self.lname} and has an email account named - {self.Email}"

    def Email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please reset it through Setter."
        return f"Email of Employee is :-{self.fname}{self.lname}@gmail.com"

    @ property
    def Email(self):
        return f"Email of Employee is :-{self.fname}{self.lname}@gmail.com"

    @ Email.setter
    def Email(self, string):
        Name = string.split("@")[0]
        self.fname = Name.split("-")[0]
        self.lname = Name.split("-")[1]

    @ Email.deleter
    def Email(self):
        self.fname = None
        self.lname = None


emp1 = Office("Vishal", "Bawane")
emp2 = Office("Arun", "Kadam")

# print(emp1.print_details())
"""
After above statement is executed, 'emp1' will be decoded and according to print_details , fname's and lname's value will 
be fetched from there.
Let's add another attribute into init() named 'Email' which will receive 'self.fname' and 'self.lname' from particular object
to form an email account.     
"""

# print(emp1.email)
# print(emp2.email)

"""
The email attribute is working accurate as we thought. Suppose, now the user wants to change emp1's first name for some purpose.
He wants the program to update the previous name into new name at every place ,so that he can save his time. It means whenever
user will print 'emp1.fname', user must get 'XXXX' name in return. 

Suppose, User replaced "Vishal" with "Ankit". Now he is printing everything related to fname to ensure himself about the done update.   
"""
# print(emp1.fname)
# emp1.fname = "Ankit"
# print(emp1.fname)
# print(emp1.print_details())
# print(emp1.Email())

"""
Let me explain what happened in the above 5 lines :-
1. User checked the previous fname.
2. User changed emp1's fname from "Vishal" to '"Ankit"
3. User reassured the updated value of fname.
4. User checked complete name of emp1 through print_details()
5. User checked email but surprised to see the email acc. name unchanged.

The email acc. name was unchanged because of constructor's initialization on the emp1.fname's value. When emp1 was created,
constructor was the main thing which assigned "Vishal" to "self.fname". When email attribute was created and it received 
the values of fname and lname through passed arguments, the values of both properties were saved permanently in the attribute.
That means, Even if the fname's value is changed 100 times, fnames's value in "Email" will remain the same, i.e " VishalBawane@gmailcom ". 
As well as assigning 'self' to fname in Email will not show different effect. 
 

As we are concerned about Email variable's updation mis-carriage, we are removing the variable from init() and instead 
'Email' variable, Email() function will handle the updation of 'fname' in Email account and this time fname will get updated 
as the user wants. 
"""

# print(emp1.Email)
# print(emp1.print_details())


# Property Decorator :-
"""
Property decorator is a built-in decorator which defines the properties of functions without manually calling them, i.e
via parenthesis.

Suppose a user do not wants to include parenthesis in Email but still wants to call and use it just by typing the name 
"Email" with associate to any object. In such cases, Property decorators are used. Property decorators helps function hide
it's call and make it look like a variable.

To make 'Email' parenthesis-less, User must create a same named function agin and property should be added with '@' mark \
on that method's head. After property is added to the function, all attributes will start showing error in Email's call
as previous call contained parenthesis. After you remove it and execute function, program will work the same as it was before.
"""

# print(emp2.Email)

"""
On the basis of 'property' decorator, 'Email' will show-up like a variable though it is a function in real. Property decorators 
are used to define the concept of 'encapsulation'. Encapsulation means hiding down the implementation of abstraction 
layers. By hiding down the call of 'Email' method, we have followed encapsulation in a minor manner.    
"""

# Setter method :-
"""
Setter nmethods are basically used to access private attributes from a class and ensure complete encapsulation in a program. 

Suppose a user do not wants to use normal method to update values of 'fname', 'lname' and 'email'. Instead of normal method,
user wants to create a function ,on the basis of which, he will pass an argument in email account format and all 'fname'
and 'lname' values would be changed. For such case, Setter method are useful as they are often used to acess private attributes. 

To create a setter method, User must select a function through which setting can be done. The method should have the same 
name like the host method and should have '@ Email.setter' on head.

Before we create setter function, let's get to know the reason why we actually require setter method. The reason why we 
require setter is just because we can't access private attributes.
If you directly type "emp1.Email = this-that@gmail.com", Python will throw error about not acknowledging the value and argument
format of string. It will clearly say that 'can't set attribute' and will not allow to access and change value of 'fname' 
and 'lname'. Thus, to overcome this things ,setter() are used.
"""
emp1.Email = "this-that@gmailcom"

"""
Now, Here I have set the setter method which will now remove the error of 'can't set the attribute'. The setter method is 
designated in such way that it will receive argument from 'Email'(main method), Email will pass the argument to Email-setter
to break down the arguments into variable-values, Email-setter will properly save the values of "fname" and "lname" to it's 
respective variables and at the next time you print that particular objects's fname or lname, you will get to see the updated 
value.

The mechanism of setter method is -
Before mechanism, user must pass an argument in an email-format because the setter method is designed to break down an email 
into variable values. To pass arguments to Email, User must write the email-format argument in front of 'self.Email'. 'Self' 
will be the particular object ,of which's value the user wants to change. 

For Ex:- Virendra-sehwag@gmail.com   

After user passes the email-format string, setter will start the processing through the following mechanism -
1. Setter will first split the given string from '@' thus there will be two elements formed into list, i.e [Virendra-sehwag,
   gmail.com]. Name acts as the container here which will store the 1st element of the list because name is addressed to 
   store only 0th index of list. In the end, name = [Virendra-Shewag]
   
2. Name will be split into two elements from '-'. Thus, it will form two elements in list, [Virendra, sehwag]. 'Self.fname'
   is the container here and value stored into it will be the new value of 'fname' all-over the program. As Self.fname is 
   addressed to store 0th index element from list, Self.fname's new vale will be 'Virendra".
   
3. Self.lname will be the container here and value stored into it will be the new value of 'lname' in program. The step 
   will work the same as secondstep but instead of 0th index element, 1st index element will be stored into self.lname. 
   In the end, self.lname = "Sehwag".
   
Now, Whenever you will print self.fname or self.lname or email of any setter-modified object, you will be able see new values.                  
"""

# Deleter :-
"""
To delete an attribute/function, deleter can be used. Deleter simply cleans the contents and values inside the particular 
attribute/function and probably, reset the function.

A deleter is an in-built function for any decorative method. In a deleter method, user should set the code which would erase
required values in an instant. To create deleter of a function, you should name the deleter same as the method has, i.e 
Email. The Email should have "@Email.deleter" above it's head. 

Suppose user wants to delete function 'Email" attributes from anything, then he would use deleter to simply to do it. So, 
User just need to run "self.Email" with 'del' keyword to call deleter of Email. self.Email will help program to know what 
object requires deleter. If you run "def emp1.Email" without creation of deleter, python will give an error saying "can't 
delete attributes".   

When deleter is executed , i.e "del emp1.Email" the process will be as follows -
1. deleter will go to main 'Email'(the one without any property or setter) function.
2. As we have set fname's value to 'None', current valueof fname will be replaced to 'None'. 
3. lname's value will be set to 'None'.
4. Now, If we try to get information of emp1's email now then the output will show "None-None@gmailcom" due to deleter.

You can set the value of email again by running setter, i.e emp1.Email = "Vishal-bawane@gmail.com". 

If you do not want to see None in the email, then you can simply put an if condition 'Email'(neither property nor setter) 
function which will give warning if fname or lname are assigned with "None". The warning will be simply ""Email is not set, 
Please reset it through Setter."

After this condition is set into Email, Further whenever user will try to print email of emp1, he will get the above statement 
as warning instead of "None-None@gmail.com".  
"""



