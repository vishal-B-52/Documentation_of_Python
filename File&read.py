#
"""The things which we can save and which could be text, image, doc's in a packet, is called as file in a hard disk.

The way you can open a file-
r -> open file for reading.
w -> open fie for write into the file.
x -> creates file if not exists & fails if exists.
a -> appends the file with new content without deleting contents in a file.
t -> opens file in text mode. Default mode.
b -> binary mode.
+ -> read and write.

"""
"""
For file IO you will need a txt file, a pointer to represent it, corresponding function and sometimes a new variable to 
store the value of pointer in it. After you open a file , it is mandatory to close it. Use close() function along with 
pointer's name. 

 """

# 1. Reading a file-
"""
To read a file, use 'r' mode when you want to open the file. You need to create a text file first in order to read the 
content in it. The 'rt' means 'readable text format' is the default format to read a file. You can even read a specific 
part of content too by just specific word limit in the parenthesis.  
"""

# F = open("Vishal.txt", 'r')
# print(content)

"""
In order to take a jump from the first 5 characters to next 5, paste the F.read(5) statement again after the first on 
stored in a different variable.
"""

# content1 = F.read(10)
# print(content1)

"""
You can decode the memory location of the file  or content by printing pointer only. Here , in order to do that, print(F)
should be used.
"""

# print(F)

"""
As stated above once you open a file, you need to close the file in the end. To close a file, close() function is used
"""

# F.close()

"""
As well as , For reading the content of a file you can use the file pointer in for loop. As the file contents are stored
in variable 'content' and using iteration we can read the contents. You can use a pointer but for that you must have to 
remove the variable and statement in which F.read() is given.  
"""

# for i in F:
#    print(i, end="")

"""
Readine()- Useful to read only a single line at a time from given file. You can print multiple lines in the content just
by using the same function. 
"""
# print(F.readline())
# print(F.readline())
# print(F.readline())

"""
Readlines() - stores the content into a list and displays it with a visible '\n' character wherever it find new line in 
content. It is similar to binary mode.
"""
print(F.readlines())

