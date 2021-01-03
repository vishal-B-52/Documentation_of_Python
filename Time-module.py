# Time module -
"""
Time modules are often used for time-counting purpose. It can calculate time from date's format to second's format. In below
example, we will measure time taken by while loop and for loop so that we can compare which loop is faster-
"""
import time
initial = time.time()

# k = 0
# while k < 100:
#     print("I am Vishal")
#     k += 1
# print("Time taken by while loop is", initial - time.time(), "seconds")


# initial2 = time.time()
# for i in range(100):
#    print("This is Vishal")
# print("Time taken by for loop is", initial2 - time.time(), "seconds")

"""
In above example, both loops will present the same time or will differ each other by a bit of milliseconds. The time gap
 between the loops depends on complexity of cod and performance of PC's. 
 
time.time() function counts time in milliseconds since universal epoch time. That is 1 January 1970. In the code, Both time 
the function is assigned to a separate variable to keep a stored value of past time. Then the past time will be subtracted by 
the functions in loops which will execute after loop is completed. The final equation here is, time taken = time before 
loop - time after loop. 
"""

# using Localtime() function-
"""
Localtime() function is used to acquire the time zone of your present country. Along with localtime() function, you will
need asctime() function to convert the tuple based format into a date-time format. 
"""

# current_time = time.asctime(time.localtime(time.time()))
# print(current_time)

"""
After printing the whole mess, It will display current date and time according to the country's timezone. Let's print 
all this value separately and let's see what can we get:-
"""
# time.time() - prints current epoch time.
# using time.localtime alone-
"""
It will display the current date and time according to the timezone. But it will display all the values separately assigned 
to a relevant variable. Ex:- tm_year = 2020, tm_day = 5, tm_mday = 16, etc. You can relate further hours , minutes, seconds 
to it.  
Note:- You can use localtime() and asctime() function even without time.time() function. time.localtime() will provide a 
broken date and time format while asctime will provide a accurate current time.  
"""
# current_time = time.localtime()
# print(current_time)

# using time.asctime alone-
"""
Asctime function helps localtime gather together it's broken format and display as result. Even if you didn't entered 
localtime() and time.time() in it's parathesis, it's printing will still give you the perfect date and time format.
"""

# current_time = time.asctime()
# print(current_time)

# Sleep() function-
"""
Sleep() function freeze down the time of exection of code for the specific time. For Ex:- If I want to print "I am Vishal"
10 seconds later after running code, you need to enter 10 in sleep(0 function's paranthesis. 
"""

# Stringer = "I am Vihsal"
# time.sleep(10)
# print(Stringer)

"""
It will take exact 10 seconds to print stringer's content on the screen after code runs.
"""

# Obtaining date and time by entering milliseconds-
"""
As time.time() does not takes any argument, you can use time.ctime() function for it. It is same as time() and asctime()
function. You need to enter a specific amount of milliseconds in it's paranthesis but it will convert an entered value 
into a date and time which will match the entered milliseconds.  
You can enter the values manually or can use input function for innovative purpose. 
"""
converter = float(input("Enter milliseconds:-"))
Inputer = time.ctime(converter)
print(Inputer)