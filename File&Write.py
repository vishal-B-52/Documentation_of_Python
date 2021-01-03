
# File Writing
# 2. Writing into a file -

"""
To write into a file, you need write() function. Write function allows you to write into a file.

If a file has old content, write() function will delete all content and write te given one into it. repeat it gain and
it will do the same thing.

Write() function can be also used to create a file if the file does not exists. 'W' mode is use in order to address file
 for writing. Use newline characters so that written file will shift new line to next line.

You can't print content of a file in writing mode.


"""

C = open("Somebody.txt", 'a')
# Contenter = C.write("I am not here")


# Appending into a file -
"""
Appending into helps more than writing into file. Appending means adding the updated content to the end of file. It adds
the content without wiping the old content of file. Appending does not have any specific function, but you should select 
the mode as 'a' and use write() function to append the file. Sometimes, after you append file the next line follows just
next to previous line. To bring it on a new line, use '\n'. It will reduce your efforts to add each character to new 
line rather than doing it manually. Try to use '\n'character in the end of written line.   
"""

# f = open("Vishal.txt", 'a')
# f.write("I am here but you can't see me \n")

# Printing length of content -
"""
In readable format or 'r' mode, if you print(f.read()) it will display all the content. You can limit the content size 
as per your need. But in write or appendable format or 'w' and 'a', if you print f.write() or the variable in which 
function is stored, the code will display the length of content. 
"""

print(C.write("I am Vishal\n")) # OR
# print(C.write("Chandu ki chachi\n"))

"""
Here, after appending, the code is reading length of previous content and then newly added content. Somehow, it does not
prints the length of all content in the file. 
"""