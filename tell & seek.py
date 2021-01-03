# tell() -
"""
tell() function is used to tell where the pointer is actually placed in the content. You should print the tell() in
order to print the place of pointer.
"""

# f = open("Visual.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())


"""
In above code when tell() was printed for the first time, it shows the pointer is at 0 which means the cursor is not set yet. 
After printing readline() it will read first line of the content. When the code reads line, it will automatically push the 
pointer further. The above line has a total length of 22. After covering a complete length of 22, pointer will stop on the 
start of next line , making the total length 23. Again if you print tell() it will show the pointer on length 23 or position 23 
in the content.  
"""

# Seek() -
"""
This function is used to reset the pointer to the previous line.
"""
# print(f.readline())
# print(f.readline())
# print("Previous pointer was at", f.tell())
# print("The last pointer is at", f.seek(1))
# print(f.readline())
"""
Seek function here did the work to reset the pointer at given position. here, Seek() is used in following steps-

1. First 2 lines in the file were print. Then tell() is used to acknowledge the position of pointer. It shows the start 
of 3rd line which is 33.
2. After code executes seek(15), It will reset the pointer to position 15. So, whenever someone print readline() in the 
file, it will print the line from 15, except 4th line, to further one. 


Default value for a seek() is always 0. Seek() will always require at-least one argument so as to reset the pointer at 
desired place. In following code - 

1. 2 lines are printed. Tell() function will show the position of pointer at 33.
2. If we set f.seek(0), then the line printed afterwards it will find the pointer at 0 and print first line again.

"""

# f = open("Visual.txt")
# print(f.readline())
# print(f.readline())

"""

Use readline always rather than readlines function. When you use readlines function, the pointer will straight go to the
end of file. Afterwards use of readline will be then un-affective as there will be no line to print.

"""

# Opening file with a block -
"""
In a block, you don't need to open and close file specifically. A block always contains both.
"""

with open("Visual.txt") as D:
    print(D.readline())
    a = D.read(23)
    print(a)


