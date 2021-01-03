# Reading and writing file at the same time -
"""

You can read and write a file at the same time by special method. You can read the content of a file and write into it
if required. This thing requires 'r+' mode. This mode will automatically grant you permission to read a file and access
it through various purpose.

"""

D = open("Variant", "r+")
# print(D.read())

"""
Above code will read the contents of a file as given in the file.
"""

D.write("All this was a complete lie.")

"""
Above code will delete all the content and write the following statement in it.
"""
