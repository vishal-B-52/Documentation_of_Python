"""Program to swap values without using 3 variables"""

# a = 45
# b = 33
#
# print("value of a before swapping:", a)
# print("value of b before swapping:", b)
#
# a, b = b, a
#
# print("\nValue of a after swapping:", a)
# print("Value of b after swapping:", b)


"""Program to print only positive numbers from a set of integers"""

# List = [4, 56, -78, 3, -66, -65, 29]
#
# for i in List:
#     if i > 0:
#         print(i)
#     else:
#         continue

# tippler = (23, 44, 55, 63, 2, 31)
# print("\nThe tuple after reversing:-", tippler[:])

# Num = int(input("Enter a number:"))
#
# for i in range(1, 6):
#     print(i * Num, "\t")
#     Num = Num + 1
#     print((i * Num))


"""Accept percentage from user and display their grade"""

# Percentage = float(input("Enter your percentage: "))
#
# if 0 <= Percentage < 100:
#     if 90 < Percentage <= 100:
#         print("Grade A+")
#     elif 80 < Percentage <= 90:
#         print("Grade A")
#     elif 70 < Percentage <= 80:
#         print("Grade B+")
#     elif 60 < Percentage <= 70:
#         print("Grade B")
#     elif 50 < Percentage <= 60:
#         print("Grade C")
#     elif 40 < Percentage <= 50:
#         print("Grade D")
#     elif 35 <= Percentage <= 40:
#         print("Grade E")
#     elif Percentage < 35:
#         print("Grade F")
# elif Percentage < 0:
#     print("\nPercentage cannot be negative. Please enter valid percentage.")
# elif Percentage > 100:
#     print("\nPlease input valid percentage.")


"""Accept age from user and verify it"""

# age = int(input("Enter your age: "))
#
# if 1 <= age < 60:
#     print("\nYou are eligible.")
# elif age == 100:
#     print("\nYou are old.")
# else:
#     print("\nYou are too old.")


"""Find all numbers divisible by 7 between 100 to 200 and sum up them"""

# Lister = []
# for i in range(100, 201):
#     if (i % 7) == 0:
#         Lister.append(i)
#
# print("\nNumbers that are divisible by 7 are:-\n", Lister)
# print("\nThe sum is:", sum(Lister))


"""Volume of cube"""

# length = float(input("Enter length: "))
# breadth = float(input("Enter breadth: "))
# height = float(input("Enter height: "))
#
# Volume_of_Cube = length * breadth * height
# print("\nThe volume of Cube is", Volume_of_Cube, "cubic cm")


"""Pyramid printing"""

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


"""Reverse Pyramid Printing"""

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("@", end=" ")
#     print()


"""Unorthodox Pyramid Printing"""

# for i in range(1, 6):
#     for j in range(2, 6):
#         print(j * i, end=" ")
#     print()


"""Gross salary"""
# Base_salary = 1500
# Bonus_rate = 200
# Commission_rate = 0.02
#
# Computer_Quantity = int(input("Quantity of Computers sold:- "))
# Computer_Price = int(input("Price of one Computer:- "))
#
# Bonus = Bonus_rate * Computer_Quantity
# Commission = Commission_rate * Computer_Quantity * Computer_Price
# Gross_Salary = Base_salary + Bonus + Commission
#
# print("The gross salary of salesperson is: ", Gross_Salary)

# dict1 = {1: 33, 3: 44, 5: 65, 7: 66, 9: 44}
# print(dict1[3])