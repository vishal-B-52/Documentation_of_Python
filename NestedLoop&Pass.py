"""Nested loops means using if loop inside a if loop, if loop inside a while or for loop or viceversa."""

# Nested if-
a = int(input())
if a < 25:
    if a == 10:
        print("Sorry you can't choose this number")

# Nested while-

i = 0
while i < 23:
    i += 2
    if i == 10:
        continue
    else:
        print(i)

# Nested For-

lister = [23, 45, 1, "name", 34, "Faroff"]
for i in lister:
    if str(i).isalpha():
        print(i)


# Pass Statement-

"""Useful if you want to keep any if ,while or for loop without any code. After entering the above conditions, You need 
to just write PASS there. Pass will avoid any type of errors which occur due to absence of code in the conditional 
statements"""

C = int(input())

if C < 10:
    print("You won")
else:
    pass