# Import function -
"""
Import function is mainly used to import modules and it's functions from somewhere to the python interpreter. Import module
works only when the specified module is downloaded within the interpreter otherwise it will throw an error.Import function
allows you to operate a module easily.
"""

# import random
# b = random.randint(1, 55)
# print(b)

# Process behind importing a module :-
"""
import function imports modules from available sources and paths but mainly from System paths. It finds direct ways to 
find a module. Import function searches for he corresponding module in the paths and after search is complete it imports all of it's 
content. You can see the system paths by importing "Sys" module
"""

# import sys
# print(sys.path)

"""
The above code will disclose all the paths in which import function will search for specified modules. Everytime the first
way is your own directory. It means the directory where you save all python codes, files and projects. It will investigate
every path to retrieve module and will throw an error about unavailability of the module if module is not present anywhere.
"""

"""
NOTE :-
As I said above, the import function will check the current directory before looking into another directory or paths for
the module. There are high chances of import function getting confused between a module and a simple python file with same 
names. In such situations, import function can accidentally import a file or project with similar name to the module into
the environment. Hence, You should not name any file by the name of a module. Always try to keep a different and unique 
name for files so that it won't ditch you in future.    
"""

# For printing version of a module :-
"""
import function can print version of a module. To print version of a module, you will need 'as' keyword to represent the
module as a variable and a variable of course. Presence of a variable won't affect the code though you can directly fetch
 "__version__" from any module.
"""
# without variable :-
# import numpy
# print(numpy.__version__)

# AND

# With a variable :-
# import numpy as coke
# print(coke.__version__)

# Importing a file and using it's content :-
"""
import allows users to import files along with modules as well. As per you fetch function from a module, you can fetch 
content from a file. The file must be empty for fast processing and variables with assigned values inside it. Here, we 
will create a new file and then try to import it's content to use them ina different file. It is not mandatory that the 
file should be empty but should have a different name than modules.   
"""

# There are two methods of importing a file -

# 1. Simple method(Using dot(.) method)

# import ifelseloop
# print(ifelseloop.a)

# 2. Using from keyword :-
# from ifelseloop import a
# print(a)

"""
Both method have it's own advantages and disadvantages.
1. The first method does not allows you to import the function fro file as well. You need to use dot extension to fetch 
the variable or functions from variables While It becomes easy to fetch wanted functions from a modules using "from and 
import" functions.
2. "From method" can face the problem of collisions of variable values when two file with same variables are called. 
For Ex:- File1 and file2 are called. From both files, variable 'a' was called and asked to be printed. At the time, 
collision can appear as interpreter will be confused to call a specific value. while this problem doesn't appears in simple 
method. In simple method, file name is mandatory to be entered for fetching a variable using dot extension.  
"""

# Importing a complete function :-
"""
You can import a function of imported file after importing files, variables and modules.
"""

# import ifelseloop
# ifelseloop.uniquer("Vishal")

"""
In above code, I imported a man-made function using import function from file "ifelseloop".
"""

# import betaturn
# print(betaturn.b)

"""
Last note :-
Whenever you import a file, use it's content and execute the code in host file(destination of imported file), the executable
code in the imported file also gets executed in the host file. Let's learn through a last example :-

In below example, betaturn.py file has two variable with some values and along with assigning, we have asked the file to
print variable a's value and make b idle for some time. Here in file import-ent , we import file "betaturn" for using it's 
content. Variable b is imported and asked to print it's value in import-ent. But along with b , a's value will be printed
too. It is because the imported file automatically executes it's code again in the host file without any necessity or 
permission. The result of imported file will always appear on top before the result of host file. Even if b was asked to
print instead of a, import-ent would have printed b's value twice. First will be of imported file's and second value will
be the result of import-ent.     
"""

import betaturn
print(betaturn.b)

"""
The above code will print the result as- 23 , 24. Because In betaturn, "a" was printed and here 'b' was asked to print 
and due to importation, both things were printed together in import-ent.   
"""
