# Faulty Calculator Program

print("Welcome to the calculator!!!")
Num1 = int(input("Enter first No:- "))
Num2 = int(input("Enter second no:- "))
Op = int(input("Choose the operation:-1.Addition\n2.Subtraction\n3.Multiplicaion\n4.Division\nYour Input:- "))
if Op == 1:
    if Num1 == 33 and Num2 == 14:
        print("Sum is :", Num1 - Num2)
    else:
        Num3 = Num1 + Num2
        print("Sum is :", Num3)
elif Op == 2:
    if Num1 == 45 and Num2 == 4:
        print("The result is :", Num1 / Num2)
    else:
        Num3 = Num1 - Num2
        print("Reult is: ", Num3)
elif Op == 3:
    Num3 = Num1 + Num2
    print("The product is: ", Num3)
elif Op == 4:
    if Num1 == 20 and Num2 == 5:
        print('The divison is:', Num1 + Num2)
    else:
        Num3 = Num1 / Num2
        print("The division is: ", Num3)