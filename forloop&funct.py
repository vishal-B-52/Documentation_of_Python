lister = (18, 2, 12, "Vishal", 5, 6, "Rohan", 77, "name")
for x in lister:
    print(x)

"""For loop is known for it's repititive iteration. I will repeat iteself until the satisfactory condition is reached"""
"""You can consider anything at the place of x. Avoid usage of any used variable again at the place of x"""

# using two separate variables in for loop-

list1 = [["Vishal", 18], ["Rohan", 24], ["Aakash", 14], ["Rajesh", 21]]
for item, age in list1:
    print("name -", item, "; age -", age)


# Making a loop print numbers greater than 18 and will ignore string items-

list22 = ["Vishal", "Busaan", 13, 33, 56, "Mangesh", 18, 2]
for fall in list22:
    if str(fall).isnumeric() and fall >= 18:
        print(fall)



