
Num1 = int(input("Enter amount of rows: "))
Num2 = input("Enter the mode of code:- 1.Normal\t 2.Reversed")
print("So you have chosen", Num2, "mode")
if Num2 == "1":
    for i in range(1, Num1 + 1):
        for j in range(i):

            print("@", end="")
        print()
elif Num2 == "2":
    for i in range(Num1, 0, -1):
        for j in range(i):

            print("#", end="")
        print()

