# If loop
a = 34
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# if num1 > num2:
#    print(num1, "is greater")

# If-else loop
# Var1 = input("Enter number: ")
# Var2 = input("Enter number: ")

# if Var1 > Var2:
#    print(Var1, "is greater!!!")
# else:
#    print(Var2, "is greater!!!")

# If-else-elif ladder

# Num11 = input("Enter the no: ")
# Num22 = input("Enter the no: ")

# if Num11 > Num22:
#    print("Num11 is greater than num22!")
# elif Num11 > Num22:
#    print("Num22 is greater than Num11!")
# else:
#     print("The numbers are equal!!")

# Using If-loop in list,tuple,set,dictionary-


def uniquer(a):
    lister = ["Vishal", "Aakash", "Rohan", "Roshan", "Manas"]
    if a in lister:
        print("It is in the list!!")
    elif a not in lister:
        print("It is not in list!!")
    else:
        print("Wrong element!!")


uniquer("Rohan")