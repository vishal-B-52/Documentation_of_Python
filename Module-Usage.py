# Using Modules -

"""
A module contains sub-modules or sub-modules with specific function to help in the program.
"""

# Random Function-

# 1. randint -
"""
It is used to make random choices. To use a module, you should import it first and only after then you can use it and 
it's functions. For more info, hold 'ctrl' key and click on the module or functions.
"""

import random
# number = random.randint(555, 1000)
# print(number)

"""
The above code will print any number from the above given range. Either it will appear twice or multiple times and it 
will print the numbers preset inside the range and not any of those from outside. 
Randint() function takes only integers and will deny any of the strings to be entered inside the paranthesis. The function
will throw an error if only one argument is provided as it is mandatory to provide two arguments to the randint() function.
You just need to provide a start range and an end range to the randint() function.
"""

# 2. random-
"""
random is itself a function in Random module. In randint function, it is mandatory to provide a range while random does 
not requires it. random function ranges itself in decimals except "0" being the predefined first range every-time. If you 
print random.random(), instead printing normal integers It will print floats or an integer(rarest) as result. 
For Ex:-  
"""

# num = random.random()
# print(num)

"""
The above code will print only numbers ranging from '0' to '0.9999999999999999'. In order to increase the range from 
0.99999999999999 to desired number, you must multiply the end range with random.random(). After you multiply it, the final
range of random.random() function will become '0' to '20.9999999999999999999'.
"""

# num = random.random() * -3
# print(num)

"""
The final and invisible range for random.random function is set to (0, 20.99...) now. After you print the variable it will
display different result with different decimals in the end. The random function will remain unaffected until manual 
changes are made. The last range of the function will remain 20.99999... always and won't hit 21 until 21 is multiplied 
into the random function. It will work the same for '0'. The starting range will never change to '-1' until '-1' is 
multiplied to the function.
"""

# Choice-
"""
Choice function is used to make random choices from a collection of elements. Here, the collection could be a list, 
tuple, dictionary or set and elements could be integer, strings, float, double or complex numbers. 

Choice takes only one argument. The argument should be the collection from which you want to make random choices.
 
"""

# collection1 = [23, " Vishal", "Rohan", "Harry", 15.655555787, 1 + 3j, 'D']
# varz = random.choice(collection1)
# print(varz)

"""
Choice function will make random choice from the collection without throwing any error until it finds any.
"""

"""
Python interpreter contains built-in modules which are fixed in numbers. You can download other modules from internet using
PIP command on terminal. You need to type "pip install......." and then hit enter to download the desired package. You should
enter the name of module correctly otherwise terminal will throw error if the respective module does not exist. 
"""

# Examples of two modules and two functions -

# import math
# b = math.degrees(45)
# print(b)
# a = math.cos(b)
# print(a)


# import pyperclip
# pyperclip.copy("I am Vishal and this is a test.")
# pyperclip.paste()

import emojis
# JOMO = emojis.encode("He has a big :smile: when i was wearing a mask :mask:")
# JOMO = emojis.decode("He has a big 😄 when i was wearing a mask 😷")
# print(JOMO)

# import wikipedia
# threats = wikipedia.page("Ninja Hattori")
# print(threats.summary)

# from urllib.request import urlopen
# page = urlopen("https://www.google.com/")
# Chrome = page.read()
# print(Chrome)

import sys
sys.exit()



